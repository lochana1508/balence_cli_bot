import argparse
from orders import place_order


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet CLI Trading Bot"
    )

    # =============================
    # CLI Arguments
    # =============================

    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading pair symbol (e.g., BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        type=str,
        choices=["BUY", "SELL"],
        required=True,
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        type=str,
        choices=["MARKET", "LIMIT"],
        required=True,
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity (must be greater than 0)"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required only for LIMIT orders)"
    )

    args = parser.parse_args()

    # =============================
    # Input Validation
    # =============================

    args.symbol = args.symbol.upper()

    if args.quantity <= 0:
        parser.error("Quantity must be greater than 0")

    if args.type == "LIMIT":
        if args.price is None:
            parser.error("LIMIT orders require --price")

        if args.price <= 0:
            parser.error("Price must be greater than 0")

    # =============================
    # Print Order Summary
    # =============================

    print("\n======================================")
    print("        ORDER REQUEST SUMMARY")
    print("======================================")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Type       : {args.type}")
    print(f"Quantity   : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price      : {args.price}")

    print("======================================\n")

    # =============================
    # Place Order
    # =============================

    try:
        order = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        
        if not order:
            print("Order failed. No response returned from Binance.")
            return

        print(" ORDER PLACED SUCCESSFULLY\n")

        print("=========== BINANCE RESPONSE ===========")
        print(f"Order ID        : {order.get('orderId')}")
        print(f"Status          : {order.get('status')}")
        print(f"Client Order ID : {order.get('clientOrderId')}")
        print(f"Executed Qty    : {order.get('executedQty')}")
        print(f"Original Qty    : {order.get('origQty')}")
        print(f"Price           : {order.get('price')}")
        print(f"Update Time     : {order.get('updateTime')}")
        print("========================================\n")

    except Exception as e:
        print("\n ERROR PLACING ORDER")
        print(str(e))


if __name__ == "__main__":
    main()