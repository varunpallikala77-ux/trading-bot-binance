# Binance Futures Trading Bot (Testnet)

## About

This project is a simple command line trading bot built using Python. It allows users to place MARKET and LIMIT orders on Binance Futures Testnet.

The main goal of this project is to understand how APIs work and how trading systems send and process orders.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports both BUY and SELL
* Takes input from command line
* Validates user input
* Logs all requests and responses

---

## How to Run

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Create .env file

Add your API keys like this:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

## Example Commands

### MARKET order

py cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

### LIMIT order

py cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 80000

---

## Output

After running, it will show order details like:

* Order ID
* Status
* Executed quantity
* Price (if available)

---

## Notes

* Since this uses testnet, sometimes orders stay in NEW state
* LIMIT orders must follow price rules:

  * SELL price should be higher than market
  * BUY price should be lower than market

---

## Logs

All logs are saved in:
trading.log

---

## Final

This project helped me understand API integration, input validation, and basic trading concepts.
