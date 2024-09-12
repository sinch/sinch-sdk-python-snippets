activate_number_response = sinch_client.numbers.available.rent_any(
    region_code="YOUR_region_code",
    type_="YOUR_number_type",
    sms_configuration={
        "servicePlanId": "YOUR_service_plan_id"
    }
)

print(activate_number_response)
