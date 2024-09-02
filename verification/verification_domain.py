from sinch import SinchClient
from sinch.domains.verification import Verification

sinch_client = SinchClient(
    application_key="YOUR_application_key",
    application_secret="YOUR_application_secret"
)

verification_client = Verification(sinch_client)
