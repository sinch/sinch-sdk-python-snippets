from sinch import SinchClient

sinch_client = SinchClient(
    key_id="YOUR_key_id",
    key_secret="YOUR_key_secret",
    project_id="YOUR_project_id"
)

activate_number_response = sinch_client.numbers.available.activate(
    phone_number="YOUR_phone_number",
    sms_configuration={
        "servicePlanId": "YOUR_service_plan_id",
        "campaignId": "YOUR_10DLC_campaign_id"
    },
    voice_configuration={
        "appId": "YOUR_app_id"
    }
)
