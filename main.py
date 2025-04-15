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