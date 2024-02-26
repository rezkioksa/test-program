def is_triangle(a, b, c):
    try:
        # Attempt to convert sides to floats
        a, b, c = float(a), float(b), float(c)
        # Check if the sum of any two sides is greater than the third side
        return a + b > c and a + c > b and b + c > a
    except ValueError:
        # If conversion to float fails, return False
        return False


def main():
    # Test Cases
    test_cases = [
        ("Equilateral Triangle", 10, 10, 10),
        ("Scalene Triangle", 8, 6, 9),
        ("Isosceles Triangle", 5, 5, 3),
        ("Right-Angled Triangle", 3, 4, 5),
        ("Large Values", 100000, 200000, 250000),
        ("All Sides Equal to 1", 1, 1, 1),
        ("All Sides Equal to 0", 0, 0, 0),
        ("One Side Zero, Other Sides Positive", 0, 3, 4),
        ("Negative Values", -2, 4, 5),
        ("One Side Negative, Others Positive", -3, 4, 5),
        ("Non-Numeric Characters", 2, "abc", 5),
        ("Zero Values", 0, 4, 5),
        ("Degenerate Triangle", 4, 3, 7),
        ("A + B = C (Two sides sum to third)", 3, 4, 7),
        ("A + C = B (Two sides sum to third)", 4, 7, 3),
        ("B + C = A (Two sides sum to third)", 7, 3, 4),
        ("Large Negative Values", -10000, -20000, -25000),
        ("One Side Negative, Other Sides Zero", -3, 0, 0),
        ("Large Positive Values", 9999999, 10000000, 20000000),
        ("Small Positive Values", 0.00001, 0.00002, 0.00003)
    ]
    
    # Iterate through test cases
    for scenario, a, b, c in test_cases:
        print(f"Scenario: {scenario}")
        try:
            # Check if the lengths form a triangle
            if is_triangle(a, b, c):
                print("Test Result: TRIANGLE OK")
            else:
                print("Test Result: TRIANGLE FAIL")
        except ValueError:
            print("Test Result: Please enter valid numeric values for the side lengths.")
        print()

if __name__ == "__main__":
    main()
