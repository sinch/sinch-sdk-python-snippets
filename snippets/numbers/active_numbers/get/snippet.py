import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

phone_number = "YOUR_RENTED_PHONE_NUMBER"
response = sinch_client.numbers.get(phone_number=phone_number)

print(f"Rented number details:\n{response}")
