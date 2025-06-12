import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

response = sinch_client.numbers.callback_configuration.get()

print("Callback Configuration:\n", response)
