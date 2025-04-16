from sinch import SinchClient
from sinch.domains.numbers.models.v1.types import VoiceConfigurationDictType

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

phone_number = "PHONE_NUMBER"
app_id = "APP_ID"
display_name = "DISPLAY_NAME"
voice_configuration: VoiceConfigurationDictType = {
    "app_id": app_id,
    "type": "RTC"
}

response = sinch_client.numbers.update(
    phone_number=phone_number,
    display_name=display_name,
    voice_configuration=voice_configuration
)

print("Updated Number:\n", response)
