
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

def get_even_numbers(numbers):
    """Return only the even numbers."""
    return [number for number in numbers if number % 2 == 0]

def main():
    numbers = [10, 15, 20, 25, 30]

    average = calculate_average(numbers)
    even_numbers = get_even_numbers(numbers)

    print("Numbers:", numbers)
    print("Average:", average)
    print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()