from flask import Flask, request, jsonify
import uuid
from faker import Faker

fake = Faker()
app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_order():
    order_number = request.args.get("orderNumber")
    if not order_number:
        return "Missing orderNumber", 400

    fake_order = {
        "Result": {
            "GlobalID": str(uuid.uuid4()),
            "ID": int(fake.random_int(min=100000000, max=999999999)),
            "Customer": {
                "EmailAddress": fake.email(),
                "FirstName": fake.first_name(),
                "LastName": fake.last_name(),
                "PhoneNumber": fake.phone_number(),
                "DateOfBirth": fake.date_of_birth().isoformat() + "T00:00:00Z",
                "Street": fake.street_name(),
                "ZipCode": fake.postcode(),
                "City": fake.city(),
                "CountryID": fake.country_code()
            },
            "Lines": [
                {
                    "Description": fake.text(max_nb_chars=30),
                    "ProductID": fake.random_int(min=10000, max=99999),
                    "UnitPrice": round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2)
                }
            ]
        }
    }

    return jsonify(fake_order)


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

# Entry point for GCP Functions Framework
def main(request):
    return app(request)