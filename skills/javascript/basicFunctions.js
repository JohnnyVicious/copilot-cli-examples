/**
 * Basic JavaScript Functions - Skills for GitHub Copilot CLI
 * This file demonstrates basic JavaScript programming skills that Copilot can help with.
 */

/**
 * Return a greeting message for the given name
 */
function greet(name) {
    return `Hello, ${name}!`;
}

/**
 * Calculate the sum of an array of numbers
 */
function calculateSum(numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
}

/**
 * Find the maximum value in an array of numbers
 */
function findMax(numbers) {
    if (numbers.length === 0) {
        throw new Error("Array cannot be empty");
    }
    return Math.max(...numbers);
}

/**
 * Reverse a string
 */
function reverseString(text) {
    return text.split('').reverse().join('');
}

/**
 * Check if a string is a palindrome (ignoring case and spaces)
 */
function isPalindrome(text) {
    const cleaned = text.replace(/\s/g, '').toLowerCase();
    return cleaned === cleaned.split('').reverse().join('');
}

/**
 * Generate Fibonacci sequence up to n terms
 */
function fibonacci(n) {
    if (n <= 0) return [];
    if (n === 1) return [0];
    
    const sequence = [0, 1];
    for (let i = 2; i < n; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
    }
    return sequence;
}

/**
 * Calculate factorial of n
 */
function factorial(n) {
    if (n < 0) {
        throw new Error("Factorial not defined for negative numbers");
    }
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

/**
 * Filter array to only even numbers
 */
function filterEven(numbers) {
    return numbers.filter(num => num % 2 === 0);
}

/**
 * Map array of strings to their lengths
 */
function stringLengths(strings) {
    return strings.map(str => str.length);
}

/**
 * Check if all elements in array satisfy condition
 */
function allPositive(numbers) {
    return numbers.every(num => num > 0);
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        greet,
        calculateSum,
        findMax,
        reverseString,
        isPalindrome,
        fibonacci,
        factorial,
        filterEven,
        stringLengths,
        allPositive
    };
}

// Test the functions if running directly
if (require.main === module) {
    console.log(greet("World"));
    console.log(`Sum: ${calculateSum([1, 2, 3, 4, 5])}`);
    console.log(`Max: ${findMax([1, 5, 3, 9, 2])}`);
    console.log(`Reversed: ${reverseString('Hello')}`);
    console.log(`Is palindrome: ${isPalindrome('racecar')}`);
    console.log(`Fibonacci: ${fibonacci(10)}`);
    console.log(`Factorial: ${factorial(5)}`);
    console.log(`Even numbers: ${filterEven([1, 2, 3, 4, 5, 6])}`);
    console.log(`String lengths: ${stringLengths(['a', 'ab', 'abc'])}`);
    console.log(`All positive: ${allPositive([1, 2, 3])}`);
}
