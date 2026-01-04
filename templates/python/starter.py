#!/usr/bin/env python3
"""
Starter template for Python 3.11+
Entrypoint: Run with `python3 starter.py`
"""


def main():
    """
    Main entry point.
    Sample I/O:
      Input: (via stdin or args)
      Output: (via stdout)
    """
    # Read input
    user_input = input("Enter your name: ")
    
    # Process
    result = f"Hello, {user_input}!"
    
    # Write output
    print(result)


if __name__ == "__main__":
    main()
