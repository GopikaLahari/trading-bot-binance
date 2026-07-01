import sys
from rich.console import Console
from rich.panel import Panel
from bot.client import get_futures_client
from bot.validators import validate_inputs
from bot.orders import place_futures_order

console = Console()


def main():
    # Expecting: python cli.py BTCUSDT SELL LIMIT 0.005 95000
    # sys.argv collects these inputs directly as a raw list
    args = sys.argv[1:]

    if len(args) < 4:
        console.print("[bold red]Error:[/bold red] Missing arguments.")
        console.print(
            "Usage: python cli.py [SYMBOL] [SIDE] [TYPE] [QUANTITY] [PRICE_IF_LIMIT]")
        return

    symbol = args[0].upper().strip()
    side = args[1].upper().strip()
    order_type = args[2].upper().strip()
    quantity = float(args[3])

    # Check if a 5th argument (price) was provided
    price = float(args[4]) if len(args) > 4 else None

    # 1. Run local structural checks
    validation_errors = validate_inputs(
        symbol, side, order_type, price, quantity)
    if validation_errors:
        for error in validation_errors:
            console.print(f"[bold red]Validation Error:[/bold red] {error}")
        return

    # 2. Execute order
    try:
        client = get_futures_client()
        console.print(
            "[yellow]Submitting order to Binance Futures...[/yellow]")

        result = place_futures_order(
            client, symbol, side, order_type, quantity, price)

        # 3. Print out the success/failure card
        if result["success"]:
            data = result["data"]
            summary_text = (
                f"[bold green]✔ Order Successfully Executed![/bold green]\n\n"
                f"• [b]Order ID:[/b] {data.get('orderId')}\n"
                f"• [b]Status:[/b] {data.get('status')}\n"
                f"• [b]Executed Qty:[/b] {data.get('executedQty')}\n"
                f"• [b]Avg Price:[/b] {data.get('avgPrice', 'N/A') or data.get('price')}"
            )
            console.print(
                Panel(summary_text, title="Receipt Details", border_style="green"))
        else:
            console.print(Panel(
                f"[red]Execution Failed:[/red] {result['error']}", title="Error Status", border_style="red"))

    except Exception as e:
        console.print(f"[bold red]Critical Failure:[/bold red] {str(e)}")


if __name__ == "__main__":
    main()
