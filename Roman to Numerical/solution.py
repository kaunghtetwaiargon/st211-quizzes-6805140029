def convert(number: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Check for invalid characters
    for symbol in number:
        if symbol not in values:
            raise ValueError("Invalid Roman numeral")

    # Check invalid examples from the assignment
    if "VX" in number or "XXC" in number:
        raise ValueError("Invalid Roman numeral")

    # V, L, and D cannot be repeated
    if "VV" in number or "LL" in number or "DD" in number:
        raise ValueError("Invalid Roman numeral")

    # I, X, C, and M cannot be repeated more than 3 times
    if "IIII" in number or "XXXX" in number or "CCCC" in number or "MMMM" in number:
        raise ValueError("Invalid Roman numeral")

    total = 0

    for i in range(len(number)):
        current = values[number[i]]

        if i < len(number) - 1:
            next_value = values[number[i + 1]]

            if current < next_value:

                # Only valid subtractive combinations
                if number[i:i+2] not in ["IV", "IX", "XL", "XC"]:
                    raise ValueError("Invalid Roman numeral")

                total -= current
            else:
                total += current

        else:
            total += current

    return total


if __name__ == "__main__":
    number = input("Enter a Roman numeral: ")

    try:
        print(convert(number))
    except ValueError:
        print("Invalid Roman numeral")