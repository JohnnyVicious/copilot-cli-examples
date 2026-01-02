"""
Complete Example: REST API Client
This example demonstrates how to build a simple REST API client using Python.
"""

import requests
from typing import Dict, List, Optional
import json


class APIClient:
    """Simple REST API client with common operations."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize API client
        
        Args:
            base_url: Base URL for the API
            api_key: Optional API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request
        
        Args:
            endpoint: API endpoint
            params: Query parameters
        
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Dict) -> Dict:
        """
        Make a POST request
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data: Dict) -> Dict:
        """
        Make a PUT request
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str) -> bool:
        """
        Make a DELETE request
        
        Args:
            endpoint: API endpoint
        
        Returns:
            True if successful
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url)
        response.raise_for_status()
        return True


class TodoAPIClient(APIClient):
    """Example client for a Todo API."""
    
    def get_todos(self) -> List[Dict]:
        """Get all todos."""
        return self.get('todos')
    
    def get_todo(self, todo_id: int) -> Dict:
        """Get a specific todo by ID."""
        return self.get(f'todos/{todo_id}')
    
    def create_todo(self, title: str, completed: bool = False) -> Dict:
        """Create a new todo."""
        data = {
            'title': title,
            'completed': completed
        }
        return self.post('todos', data)
    
    def update_todo(self, todo_id: int, title: Optional[str] = None, 
                    completed: Optional[bool] = None) -> Dict:
        """Update an existing todo."""
        data = {}
        if title is not None:
            data['title'] = title
        if completed is not None:
            data['completed'] = completed
        return self.put(f'todos/{todo_id}', data)
    
    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo."""
        return self.delete(f'todos/{todo_id}')


def main():
    """Example usage of the API client."""
    # Using JSONPlaceholder as example API
    client = TodoAPIClient('https://jsonplaceholder.typicode.com')
    
    # Get all todos
    print("Fetching all todos...")
    todos = client.get_todos()
    print(f"Found {len(todos)} todos")
    
    # Get specific todo
    print("\nFetching todo #1...")
    todo = client.get_todo(1)
    print(f"Todo: {todo['title']}")
    
    # Create new todo
    print("\nCreating new todo...")
    new_todo = client.create_todo("Test Todo from API Client")
    print(f"Created todo with ID: {new_todo.get('id', 'N/A')}")
    
    # Update todo
    print("\nUpdating todo...")
    updated = client.update_todo(1, completed=True)
    print(f"Updated todo: {updated['title']} - Completed: {updated['completed']}")
    
    print("\nAPI client example completed!")


if __name__ == "__main__":
    main()
