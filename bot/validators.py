def validate_inputs(symbol: str, side: str, order_type: str, price: float, quantity: float):
    """Checks for simple formatting errors before we call the exchange"""
    errors = []
    if side.upper() not in ["BUY", "SELL"]:
        errors.append("Side must be either 'BUY' or 'SELL'.")
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        errors.append("Order type must be either 'MARKET' or 'LIMIT'.")
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        errors.append("A valid positive price is required for LIMIT orders.")
    if quantity <= 0:
        errors.append("Quantity must be greater than 0.")

    return errors
