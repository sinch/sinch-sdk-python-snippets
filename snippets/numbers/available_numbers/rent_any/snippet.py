import os
from dotenv import load_dotenv
from sinch import SinchClient
from sinch.domains.numbers.models.v1.types import (
    NumberPatternDict, SmsConfigurationDict, VoiceConfigurationDictType
)

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ.get("SINCH_PROJECT_ID") or "MY_PROJECT_ID",
    key_id=os.environ.get("SINCH_KEY_ID") or "MY_KEY_ID",
    key_secret=os.environ.get("SINCH_KEY_SECRET") or "MY_KEY_SECRET"
)

sms_configuration: SmsConfigurationDict = {
    "service_plan_id": "SERVICE_PLAN_ID"
}
voice_configuration: VoiceConfigurationDictType = {
    "app_id": "APP_ID",
    "type": "RTC"
}
number_pattern: NumberPatternDict = {
    "pattern": "+1234",
    "search_pattern": "START"
}
response = sinch_client.numbers.rent_any(
    region_code="US",
    type_="LOCAL",
    capabilities=["SMS", "VOICE"],
    sms_configuration=sms_configuration,
    voice_configuration=voice_configuration,
    number_pattern=number_pattern
)

print("Rented Number:\n", response)
