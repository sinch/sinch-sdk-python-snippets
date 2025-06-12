import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

phone_number = "PHONE_NUMBER"
response = sinch_client.numbers.check_availability(
    phone_number=phone_number
)

print("Released Number:\n", response)
