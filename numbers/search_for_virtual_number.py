available_numbers_response = sinch_client.numbers.available.list(
    region_code="YOUR_region_code",
    number_type="YOUR_number_type"
)

print(available_numbers_response)
