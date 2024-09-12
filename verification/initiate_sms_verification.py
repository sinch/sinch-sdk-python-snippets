from sinch.domains.verification.models import VerificationIdentity

response = sinch_client.verification.verifications.start_sms(
    identity=VerificationIdentity(
        type="number",
        endpoint="YOUR_phone_number"
    )
)
print(response)
