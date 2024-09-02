from sinch import Client
from sinch.domains.voice import Voice

sinch_client = Client(
    application_key="YOUR_application_key",
    application_secret="YOUR_application_secret"
)

voice_client = Voice(sinch_client)
