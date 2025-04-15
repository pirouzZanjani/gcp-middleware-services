def get_order(request):
    customer_id = request.args.get("customerId")
    if not customer_id:
        return ("Missing customerId", 400)

    order = {
        "orderId": "A123",
        "customerId": customer_id,
        "items": ["item1", "item2"],
        "status": "Shipped"
    }

    return order


def refund_order(request):
    order_id = request.args.get("orderId")
    reason = request.args.get("reason", "No reason provided")

    if not order_id:
        return ("Missing orderId", 400)

    refund_response = {
        "orderId": order_id,
        "refunded": True,
        "refundReason": reason,
        "status": "Refund initiated"
    }

    return refund_response
