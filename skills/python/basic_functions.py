"""
Basic Python Functions - Skills for GitHub Copilot CLI
This file demonstrates basic Python programming skills that Copilot can help with.
"""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


def find_max(numbers: list[int]) -> int:
    """Find the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> list[int]:
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Test the functions
    print(greet("World"))
    print(f"Sum: {calculate_sum([1, 2, 3, 4, 5])}")
    print(f"Max: {find_max([1, 5, 3, 9, 2])}")
    print(f"Reversed: {reverse_string('Hello')}")
    print(f"Is palindrome: {is_palindrome('racecar')}")
    print(f"Fibonacci: {fibonacci(10)}")
    print(f"Factorial: {factorial(5)}")
