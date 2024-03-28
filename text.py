def calculate_check_digit(sequential_number, year, judicial_body, region, origin_unit):
    # Dummy implementation for check digit calculation
    # Replace with the specific algorithm used by the court system
    return (sequential_number * year * judicial_body * region * origin_unit) % 100

def generate_case_numbers(year, judicial_body, region, origin_unit_range):
    case_numbers = []
    sequential_number = 1  # Starting from 1 for simplification

    for origin_unit in origin_unit_range:
        check_digit = calculate_check_digit(sequential_number, year, judicial_body, region, origin_unit)
        case_number = f"{sequential_number:07d}-{check_digit:02d}.{year}.{judicial_body}.{region:02d}.{origin_unit}00"
        case_numbers.append(case_number)

    return case_numbers

# Configure your parameters here
year = 2023
judicial_body = 4  # Federal Court
region = 3  # 3rd Region
origin_unit_range = [60, 61, 62, 63, 64, 65]

case_numbers = generate_case_numbers(year, judicial_body, region, origin_unit_range)
for number in case_numbers:
    print(number)