import os
from sinch import SinchClient

sinch_client = SinchClient(
    application_key=os.getenv("APPLICATION_KEY"),
    application_secret=os.getenv("APPLICATION_SECRET")
)
