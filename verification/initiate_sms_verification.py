from sinch import SinchClient
from sinch.domains.verification.models import VerificationIdentity

sinch_client = SinchClient(
    application_key="YOUR_application_key",
    application_secret="YOUR_application_secret"
)

response = sinch_client.verification.verifications.start_sms(
    identity=VerificationIdentity(
        type="number",
        endpoint="YOUR_phone_number"
    )
)
print(response)
