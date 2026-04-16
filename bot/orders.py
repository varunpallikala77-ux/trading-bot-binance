def execute_order(client, logger, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing order: {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

        logger.info(f"Order Success: {response}")
        return response

    except Exception as e:
        logger.error(f"Order Failed: {str(e)}")
        return {"error": str(e)}
