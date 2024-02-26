def is_valid_province_code(code):
    valid_codes = [
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "31", "32", "33", "34", "35", "36", "51", "52", "53", "61", "62", "63", "64", "71", "72", "73", "74", "75", "76", "81", "82", "91", "94"
    ]
    return code in valid_codes

def validate_nik(nik):
    # Check if NIK is 16 digits
    if len(nik) != 16:
        return False
    
    # Check if all characters are digits
    if not nik.isdigit():
        return False
    
    # Extract components
    province_code = nik[:2]
    city_code = nik[2:4]
    sub_district_code = nik[4:6]
    dob_code = nik[6:12]
    
    # Check if province code is valid (01-91)
    if not (is_valid_province_code(province_code)):
        return False
    
    # Check if city/district code is valid (01-99 -> EXAMPLE ONLY, can be matched with the is_valid_province_code validation)
    if not (1 <= int(city_code) <= 99):
        return False
        
    # Check if sub-district code is valid (01-40 -> EXAMPLE ONLY, can be matched with the is_valid_province_code validation)
    if not (1 <= int(sub_district_code) <= 40):
        return False
    
    # Check date of birth validity
    dob_day = int(dob_code[:2])
    
    if dob_day > 40:  # For women, day is original day + 40
        dob_day -= 40
    dob_month = int(dob_code[2:4])
    dob_year = int(dob_code[-2:])
    
    if not (1 <= dob_day <= 31):
        return False
    if not (1 <= dob_month <= 12):
        return False
        
    # Assuming reasonable range for year, adjust this as needed
    if not (0 <= dob_year <= 99):
        return False
    
    # If all checks passed, return True
    return True

# Test Cases
test_cases = [
    ("TC01", "Valid NIK", "Positive", "3102064401910006", "Enter the given valid NIK", "NIK OK"),
    ("TC02", "Invalid NIK (incorrect length)", "Negative", "1234567890", "Enter an NIK with incorrect length", "NIK FAIL"),
    ("TC03", "Invalid NIK (non-numeric characters)", "Negative", "1234ABCD567890EF", "Enter an NIK with non-numeric characters", "NIK FAIL"),
    ("TC04", "Invalid NIK (invalid province code)", "Negative", "9923082803890003", "Enter an NIK with an invalid province code", "NIK FAIL"),
    ("TC05", "Invalid NIK (invalid city code)", "Negative", "3100012803890003", "Enter an NIK with an invalid city code", "NIK FAIL"),
    ("TC06", "Invalid NIK (invalid birth date format)", "Negative", "3173089903890003", "Enter an NIK with an invalid birth date format", "NIK FAIL"),
    ("TC07", "Invalid NIK (invalid birth date)", "Negative", "3173083203890003", "Enter an NIK with an invalid birth date", "NIK FAIL"),
    ("TC08", "Sequence number is maximum", "Positive", "3102064401919999", "Enter an NIK with an invalid sequence number", "NIK OK"),
    ("TC09", "Edge Case: Minimum NIK Length", "Negative", "1", "Enter a valid NIK with minimum length", "NIK FAIL"),
    ("TC10", "Edge Case: Maximum NIK Length", "Negative", "9999999999999999", "Enter a valid NIK with maximum length", "NIK FAIL"),
    ("TC11", "Invalid NIK (empty input)", "Negative", "", "Leave NIK field empty", "NIK FAIL"),
    ("TC12", "Invalid NIK (leading zeros)", "Negative", "123456789000", "Enter an NIK with leading zeros", "NIK FAIL"),
    ("TC13", "Invalid NIK (out of range province code)", "Negative", "9982082803890003", "Enter an NIK with an out of range province code", "NIK FAIL"),
    ("TC14", "Invalid NIK (out of range city code)", "Negative", "3173002803890003", "Enter an NIK with an out of range city code", "NIK FAIL"),
    ("TC15", "Invalid NIK (out of range birth date)", "Negative", "3173083203890003", "Enter an NIK with an out of range birth date", "NIK FAIL"),
    ("TC16", "Invalid NIK (invalid characters in birth date)", "Negative", "3173AB2803890003", "Enter an NIK with invalid characters in birth date", "NIK FAIL"),
    ("TC17", "Invalid NIK (invalid characters in sequence number)", "Negative", "31730828038900A3", "Enter an NIK with invalid characters in sequence number", "NIK FAIL"),
    ("TC18", "Edge Case: Non-existent province code", "Negative", "9999082803890003", "Enter an NIK with a non-existent province code", "NIK FAIL"),
    ("TC19", "Edge Case: Non-existent city code", "Negative", "3173992803890003", "Enter an NIK with a non-existent city code", "NIK FAIL"),
]

# Run test cases
for tc_id, scenario, scenario_type, test_data, steps, expected_result in test_cases:
    result = "NIK OK" if validate_nik(test_data) else "NIK FAIL"
    print(f"{tc_id}: {scenario} - {scenario_type} - Test Result: {result}")
