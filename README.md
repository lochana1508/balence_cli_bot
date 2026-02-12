# Binance Futures Testnet CLI Trading Bot

##  Project Overview

This is a Command Line Interface (CLI) trading bot built using Python that allows users to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

##  Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- Input validation using argparse
- Clean order summary output
- Proper error handling
- Uses Binance Futures Testnet

---

##  Installation

### 1. Clone Repository

git clone <your-repo-link>

### 2. Install Requirements

pip install -r requirements.txt

---

##  Setup API Keys

Create a `.env` file in the project folder and add:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

Make sure you use Binance Futures Testnet keys.

---

##  Usage Examples

### MARKET BUY

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### MARKET SELL

python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01

### LIMIT BUY

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 50000

### LIMIT SELL

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

---

##  Project Structure

TRADING_BOT/
│
├── cli.py
├── orders.py
├── client.py
├── config.py
├── logging_config.py
├── .env
├── requirements.txt
└── README.md

---

##  Validation Rules

- Quantity must be greater than 0
- LIMIT orders require price
- Order type must be MARKET or LIMIT
- Side must be BUY or SELL

---

##  Tested Scenarios

- MARKET BUY 
- MARKET SELL
- LIMIT BUY 
- LIMIT SELL 
- Error handling 

---
## Error Handling

Displays error if LIMIT order price is missing
Displays error if quantity is less than or equal to 0
Handles Binance API errors gracefully
Prevents crash when API returns no response
 ---
##  Author

B.V.Lochana