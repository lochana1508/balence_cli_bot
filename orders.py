import logging
from client import client


def place_order(symbol, side, order_type, quantity, price=None):
    """
    Places a MARKET or LIMIT order on Binance Futures Testnet.
    """

    try:
        logging.info(
            f"Placing order | Symbol: {symbol}, Side: {side}, "
            f"Type: {order_type}, Quantity: {quantity}, Price: {price}"
        )

        # MARKET Order
        if order_type.upper() == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )

        # LIMIT Order
        elif order_type.upper() == "LIMIT":

            if price is None:
                raise ValueError("Price is required for LIMIT orders")

            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type. Must be MARKET or LIMIT")

        logging.info(f"Order successful | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logging.error(f"Order failed | Error: {str(e)}")
        print(" Order failed. Check logs for details.")
        return None