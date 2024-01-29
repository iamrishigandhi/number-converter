def convert_and_display(number, base):
    try:
        decimal_number = int(number, base)

        binary_result = bin(decimal_number)[2:]
        octal_result = oct(decimal_number)[2:]
        decimal_result = decimal_number
        hexadecimal_result = hex(decimal_number)[2:]

        print(f"\nDecimal: {decimal_result}")
        print(f"Binary: {binary_result}")
        print(f"Octal: {octal_result}")
        print(f"Hexadecimal: {hexadecimal_result}")
    except ValueError:
        pass  # Ignore conversion errors for bases that are not applicable to the input

def main():
    try:
        user_input = input("Enter a number: ")

        # Try converting as binary, decimal, and hexadecimal
        for base in [2, 8, 10, 16]:
            convert_and_display(user_input, base)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()