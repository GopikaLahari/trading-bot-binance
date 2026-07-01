# Simplified Binance Futures Trading Bot

A structured Python CLI application built to interact with Binance Futures endpoints using clean execution logging and robust validation logic.

## Features Included
- Market and Limit Order execution structures (supporting both BUY and SELL sides).
- Pre-execution input validation layer.
- Structured code design separating client, business logic, and interface layers.
- Diagnostic logging mapped cleanly to `bot_activity.log`.
- Enhanced terminal response UX using Rich cards.

## Setup Instructions
1. Install project dependencies:
   ```bash
   pip install -r requirements.txt