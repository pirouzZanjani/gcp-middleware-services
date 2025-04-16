from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_order():
    customer_id = request.args.get("customerId")
    if not customer_id:
        return "Missing customerId", 400

    order = {
        "orderId": "A123",
        "customerId": customer_id,
        "items": ["item1", "item2"],
        "status": "Shipped"
    }
    return jsonify(order)

@app.route('/refund', methods=['GET'])
def refund_order():
    order_id = request.args.get("orderId")
    reason = request.args.get("reason", "No reason provided")

    if not order_id:
        return "Missing orderId", 400

    response = {
        "orderId": order_id,
        "refunded": True,
        "refundReason": reason,
        "status": "Refund initiated"
    }
    return jsonify(response)

# GCP will call this function
def main(request):
    return app(request)
