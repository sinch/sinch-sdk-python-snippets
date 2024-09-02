from sinch import SinchClient

sinch_client = SinchClient(
    key_id="YOUR_key_id",
    key_secret="YOUR_key_secret",
    project_id="YOUR_project_id"
)

activate_number_response = sinch_client.numbers.available.rent_any(
    region_code="YOUR_region_code",
    type_="YOUR_number_type",
    sms_configuration={
        "servicePlanId": "YOUR_service_plan_id"
    }
)

print(activate_number_response)
