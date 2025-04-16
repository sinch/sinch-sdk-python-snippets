from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

available_regions = sinch_client.numbers.regions.list(
    number_types=["MOBILE"]
)

print("Available regions:\n")
for region in available_regions.iterator():
    print(region)
