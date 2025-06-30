"""
Sinch Python Snippet

This snippet is available at https://github.com/sinch/sinch-sdk-python-snippets
"""

import os
from dotenv import load_dotenv
from sinch import SinchClient
from sinch.domains.numbers.models.v1.types import SmsConfigurationDict

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ.get("SINCH_PROJECT_ID") or "MY_PROJECT_ID",
    key_id=os.environ.get("SINCH_KEY_ID") or "MY_KEY_ID",
    key_secret=os.environ.get("SINCH_KEY_SECRET") or "MY_KEY_SECRET"
)

phone_number_to_be_rented = os.environ.get("SINCH_PHONE_NUMBER") or "MY_SINCH_PHONE_NUMBER"
service_plan_id = os.environ.get("SINCH_SERVICE_PLAN_ID") or "MY_SERVICE_PLAN_ID"
sms_configuration: SmsConfigurationDict = {
    "service_plan_id": service_plan_id
}

rented_number = sinch_client.numbers.rent(
    phone_number=phone_number_to_be_rented,
    sms_configuration=sms_configuration
)
print("Rented Number:\n", rented_number)
