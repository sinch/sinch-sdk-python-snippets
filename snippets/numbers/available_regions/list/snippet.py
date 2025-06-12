import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

available_regions = sinch_client.numbers.regions.list(
    number_types=["MOBILE"]
)

print("Available regions:\n")
for region in available_regions.iterator():
    print(region)
