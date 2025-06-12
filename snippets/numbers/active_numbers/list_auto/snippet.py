import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

active_numbers = sinch_client.numbers.list(
   region_code="US",
   number_type="LOCAL"
)

print("List of numbers printed one by one:\n")
for number in active_numbers.iterator():
    print(number)
