import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

phone_number = "PHONE_NUMBER_TO_BE_RELEASED"
released_number = sinch_client.numbers.release(
    phone_number=phone_number
)

print("Released Number:", released_number)
