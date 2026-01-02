// Basic Go Functions - Skills for GitHub Copilot CLI
// This file demonstrates basic Go programming skills that Copilot can help with.
package main

import (
	"fmt"
	"strings"
)

// Greet returns a greeting message for the given name
func Greet(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

// CalculateSum calculates the sum of a slice of integers
func CalculateSum(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

// FindMax finds the maximum value in a slice of integers
func FindMax(numbers []int) (int, error) {
	if len(numbers) == 0 {
		return 0, fmt.Errorf("slice cannot be empty")
	}
	max := numbers[0]
	for _, num := range numbers[1:] {
		if num > max {
			max = num
		}
	}
	return max, nil
}

// ReverseString reverses a string
func ReverseString(text string) string {
	runes := []rune(text)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome checks if a string is a palindrome (ignoring case and spaces)
func IsPalindrome(text string) bool {
	cleaned := strings.ToLower(strings.ReplaceAll(text, " ", ""))
	return cleaned == ReverseString(cleaned)
}

// Fibonacci generates Fibonacci sequence up to n terms
func Fibonacci(n int) []int {
	if n <= 0 {
		return []int{}
	}
	if n == 1 {
		return []int{0}
	}
	
	sequence := []int{0, 1}
	for i := 2; i < n; i++ {
		sequence = append(sequence, sequence[i-1]+sequence[i-2])
	}
	return sequence
}

// Factorial calculates factorial of n
func Factorial(n int) (int, error) {
	if n < 0 {
		return 0, fmt.Errorf("factorial not defined for negative numbers")
	}
	if n == 0 || n == 1 {
		return 1, nil
	}
	result, _ := Factorial(n - 1)
	return n * result, nil
}

// FilterEven returns only even numbers from the slice
func FilterEven(numbers []int) []int {
	var evens []int
	for _, num := range numbers {
		if num%2 == 0 {
			evens = append(evens, num)
		}
	}
	return evens
}

// Contains checks if a slice contains a specific value
func Contains(slice []int, value int) bool {
	for _, item := range slice {
		if item == value {
			return true
		}
	}
	return false
}

// UniqueValues returns unique values from a slice
func UniqueValues(numbers []int) []int {
	seen := make(map[int]bool)
	var unique []int
	for _, num := range numbers {
		if !seen[num] {
			seen[num] = true
			unique = append(unique, num)
		}
	}
	return unique
}

func main() {
	fmt.Println(Greet("World"))
	fmt.Printf("Sum: %d\n", CalculateSum([]int{1, 2, 3, 4, 5}))
	
	max, _ := FindMax([]int{1, 5, 3, 9, 2})
	fmt.Printf("Max: %d\n", max)
	
	fmt.Printf("Reversed: %s\n", ReverseString("Hello"))
	fmt.Printf("Is palindrome: %t\n", IsPalindrome("racecar"))
	fmt.Printf("Fibonacci: %v\n", Fibonacci(10))
	
	fact, _ := Factorial(5)
	fmt.Printf("Factorial: %d\n", fact)
	
	fmt.Printf("Even numbers: %v\n", FilterEven([]int{1, 2, 3, 4, 5, 6}))
	fmt.Printf("Contains 3: %t\n", Contains([]int{1, 2, 3, 4}, 3))
	fmt.Printf("Unique: %v\n", UniqueValues([]int{1, 2, 2, 3, 3, 4}))
}
