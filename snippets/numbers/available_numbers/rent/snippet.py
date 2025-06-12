import os
from dotenv import load_dotenv
from sinch.domains.numbers.models.v1.types import SmsConfigurationDict
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

phone_number = "AVAILABLE_PHONE_NUMBER_TO_BE_RENTED"
service_plan_id = "SERVICE_PLAN_ID"
sms_configuration: SmsConfigurationDict = {
    "service_plan_id": service_plan_id
}

rented_number = sinch_client.numbers.rent(
    phone_number=phone_number,
    sms_configuration=sms_configuration
)
print("Rented Number:\n", rented_number)
