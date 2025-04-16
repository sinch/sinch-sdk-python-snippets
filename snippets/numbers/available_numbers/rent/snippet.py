from sinch.domains.numbers.models.v1.types import SmsConfigurationDict
from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
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
