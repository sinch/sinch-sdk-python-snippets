import sinch
from flask import Flask, request


app = Flask(__name__)

sinch_client = sinch.SinchClient(
    key_id="YOUR_KEY_ID",
    key_secret="YOUR_KEY_SECRET",
    project_id="YOUR_PROJECT_ID"
)


@app.route('/', methods=['POST'])
def result():
    inbound_message = request.get_json()
    print(inbound_message)

    if all(key in inbound_message for key in ["body", "to", "from"]):
        sinch_client.sms.batches.send(
            body="Thank you for using the Sinch SDK. You sent: " + inbound_message["body"],
            delivery_report="none",
            to=[inbound_message["from"]],
            from_=inbound_message["to"]
        )

        return "Inbound message received", 200

    else:
        return "Invalid data", 400
