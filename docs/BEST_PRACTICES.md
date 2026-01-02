# Best Practices for Using GitHub Copilot CLI

## General Principles

### 1. Be Intentional with Context
Copilot works best when it understands your intent:

```python
# ✅ Good: Clear context
# Calculate compound interest with monthly compounding
# Formula: A = P(1 + r/n)^(nt)
def calculate_compound_interest(principal, rate, time, frequency=12):
    pass

# ❌ Bad: No context
def calc(p, r, t, f):
    pass
```

### 2. Write Descriptive Names
Good names help Copilot understand what you're building:

```javascript
// ✅ Good
function validateEmailAddress(email) { }

// ❌ Bad
function validate(e) { }
```

### 3. Use Type Hints (Python)
Type hints improve suggestion quality:

```python
# ✅ Good
def process_user_data(users: list[dict]) -> dict[str, int]:
    pass

# ❌ Bad
def process_user_data(users):
    pass
```

## Code Organization

### File Structure
Organize your code to help Copilot understand context:

```
project/
├── models/          # Data models
├── services/        # Business logic
├── utils/           # Helper functions
└── tests/           # Test files
```

### Docstrings and Comments
Good documentation helps Copilot generate better code:

```python
def binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of integers
        target: Value to find
    
    Returns:
        Index of target, or -1 if not found
    
    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3], 5)
        -1
    """
    # Copilot will provide accurate implementation
    pass
```

## Working with Different Languages

### Python Best Practices

```python
# Use type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Use descriptive variable names
user_count = 0
active_sessions = []

# Follow PEP 8
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user: dict) -> None:
        self.users.append(user)
```

### JavaScript Best Practices

```javascript
// Use JSDoc comments
/**
 * Calculate the average of numbers
 * @param {number[]} numbers - Array of numbers
 * @returns {number} The average
 */
function calculateAverage(numbers) {
    // Copilot will suggest good implementation
}

// Use modern ES6+ features
const filterActive = (users) => users.filter(u => u.active);

// Use descriptive names
const fetchUserData = async (userId) => {
    const response = await fetch(`/api/users/${userId}`);
    return response.json();
};
```

### Go Best Practices

```go
// Use clear type definitions
type User struct {
    ID       int
    Username string
    Email    string
}

// Document exported functions
// GetUserByID retrieves a user by their ID
func GetUserByID(id int) (*User, error) {
    // Copilot will suggest implementation
    return nil, nil
}

// Use proper error handling
func processData(data []byte) error {
    if len(data) == 0 {
        return fmt.Errorf("data cannot be empty")
    }
    // Process data
    return nil
}
```

## Testing

### Write Test Cases First
Test-driven development works well with Copilot:

```python
# Write the test first
def test_calculate_total_price():
    items = [
        {"price": 10.0, "quantity": 2},
        {"price": 5.0, "quantity": 3}
    ]
    assert calculate_total_price(items) == 35.0
    assert calculate_total_price([]) == 0.0

# Then let Copilot help implement
def calculate_total_price(items: list[dict]) -> float:
    # Copilot will suggest implementation based on tests
    pass
```

### Test Edge Cases
```python
def test_divide_numbers():
    # Normal case
    assert divide(10, 2) == 5.0
    
    # Edge case: division by zero
    with pytest.raises(ValueError):
        divide(10, 0)
    
    # Edge case: negative numbers
    assert divide(-10, 2) == -5.0
```

## Error Handling

### Be Explicit About Error Cases
```python
def fetch_user_data(user_id: int) -> dict:
    """
    Fetch user data from database.
    
    Raises:
        ValueError: If user_id is invalid
        ConnectionError: If database is unreachable
        NotFoundError: If user doesn't exist
    """
    # Copilot will suggest proper error handling
    pass
```

### Use Try-Except Blocks
```python
def safe_json_load(filepath: str) -> dict:
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in: {filepath}")
        return {}
```

## Performance Optimization

### Comment Your Performance Requirements
```python
# Need O(log n) time complexity for large datasets
def binary_search_optimized(arr, target):
    pass

# This function will be called millions of times, optimize for speed
def calculate_distance(x1, y1, x2, y2):
    pass
```

### Ask for Specific Optimizations
```python
# TODO: Optimize this loop to use list comprehension
result = []
for item in items:
    if item.active:
        result.append(item.name)

# Copilot might suggest:
# result = [item.name for item in items if item.active]
```

## Security Considerations

### Request Secure Implementations
```python
# TODO: Implement secure password hashing with bcrypt
def hash_password(password: str) -> str:
    pass

# TODO: Sanitize user input to prevent SQL injection
def search_users(search_term: str):
    pass

# TODO: Validate and sanitize HTML to prevent XSS
def render_user_content(content: str) -> str:
    pass
```

### Be Explicit About Validation
```python
def process_payment(amount: float, card_number: str):
    """
    Process payment with validation.
    
    Must:
    - Validate amount is positive
    - Validate card number format
    - Use secure connection
    - Log transaction
    """
    pass
```

## Refactoring

### Ask for Refactoring Help
```python
# TODO: Refactor this function to be more readable
def process(d):
    r = []
    for i in d:
        if i["a"] > 0:
            r.append(i["b"])
    return r

# Better version:
def extract_positive_values(data: list[dict]) -> list:
    """Extract 'value' field from items where 'amount' is positive."""
    return [item["value"] for item in data if item["amount"] > 0]
```

## Common Patterns

### Factory Pattern
```python
# Factory pattern for creating different types of notifications
class NotificationFactory:
    """Create notifications based on type."""
    
    @staticmethod
    def create(notification_type: str):
        # Copilot will suggest implementations
        pass
```

### Singleton Pattern
```python
# Singleton pattern for database connection
class DatabaseConnection:
    """Singleton database connection."""
    _instance = None
    
    def __new__(cls):
        # Copilot will suggest singleton implementation
        pass
```

### Observer Pattern
```python
# Observer pattern for event handling
class EventEmitter:
    """Event emitter with observers."""
    
    def __init__(self):
        self.observers = []
    
    # Copilot will suggest add_observer, remove_observer, notify methods
```

## Debugging Tips

### Add Debug Comments
```python
# Debug: Print intermediate values
# Debug: Log execution time
# Debug: Check if list is empty
def complex_calculation(data):
    pass
```

### Request Logging
```python
# TODO: Add comprehensive logging for debugging
def process_order(order_id: int):
    pass
```

## Summary

1. **Write clear, descriptive code** - Copilot works best with good context
2. **Use comments strategically** - Guide Copilot with your intent
3. **Follow language conventions** - Copilot is trained on best practices
4. **Test thoroughly** - Use Copilot to generate test cases
5. **Iterate and refine** - Use Copilot's suggestions as starting points
6. **Think about security** - Request secure implementations explicitly
7. **Document as you go** - Good docs help both humans and AI

Remember: Copilot is a tool to augment your abilities, not replace your judgment. Always review and understand the code it suggests.
