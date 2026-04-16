def validate_order(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol is required")

    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a positive number")

    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        try:
            float(price)
        except (ValueError, TypeError):
            raise ValueError("Invalid price format")