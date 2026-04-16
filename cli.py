import argparse
import sys
import time
from bot.client import get_client
from bot.validators import validate_order
from bot.orders import execute_order
from bot.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--order-type", dest="order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT)")

    args = parser.parse_args()

    logger = setup_logger()

    try:
        # Normalize symbol
        symbol = args.symbol.upper()

        # Validate input
        validate_order(symbol, args.side, args.order_type, args.quantity, args.price)

        client = get_client()

        print("\n🚀 Binance Testnet Trading Bot")

        print("\n📌 Order Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.order_type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        print("\n⏳ Confirming order in 3 seconds...")
        time.sleep(3)

        confirm = input("\nProceed with order? (yes/no): ")
        if confirm.lower() not in ["yes", "y"]:
            print("❌ Order cancelled by user.")
            sys.exit()

        result = execute_order(
            client,
            logger,
            symbol,
            args.side,
            args.order_type,
            args.quantity,
            args.price
        )

        if "error" in result:
            print("\n❌ Order Failed")
            print("Reason:", result["error"])
        else:
            print("\n✅ Order Placed Successfully")
            print(f"Order ID: {result.get('orderId')}")
            print(f"Status: {result.get('status')}")
            print(f"Executed Qty: {result.get('executedQty')}")
            print(f"Avg Price: {result.get('avgPrice')}")

    except Exception as e:
        print("\n❌ Error:", str(e))
        logger.error(str(e))

if __name__ == "__main__":
    main()