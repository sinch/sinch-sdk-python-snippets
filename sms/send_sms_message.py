send_batch_response = sinch_client.sms.batches.send(
    body="Hello from Sinch!",
    to=["YOUR_to_number"],
    from_="YOUR_Sinch_number",
    delivery_report="none"
)

print(send_batch_response)
