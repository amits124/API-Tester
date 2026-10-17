# JSONPlaceholder API Tester

A Python-based tool for interacting with and testing the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) REST API. The project includes an interactive command-line interface (CLI) and automated tests using pytest.

## Features

### API Operations
- Retrieve all posts.
- Retrieve a post by ID.
- Retrieve comments for a post.
- Retrieve posts by user ID.
- Create a post using POST.
- Replace a post using PUT.
- Partially update a post using PATCH.
- Delete a post using DELETE.

### Automated Testing
- Automated API tests using pytest.
- Validation of HTTP status codes and response content.
- Tests covering successful requests, data integrity, and edge cases.

### Interactive CLI
- Menu-driven interface for executing API operations.
- Formatted output for easier response inspection.
- Basic handling of unsuccessful HTTP responses and nonexistent posts.

## Technologies

- Python
- Requests
- pytest
- JSONPlaceholder REST API

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amits124/JSONPlaceholder-API-Tester.git
   cd JSONPlaceholder-API-Tester
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell)**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the CLI

From the project root, run:

```bash
python cli.py
```

Choose an operation from the menu and follow the prompts.

### Run the automated tests

From the project root, run:

```bash
pytest
```

## Project Structure

```text
JSONPlaceholder-API-Tester/
├── api/
│   ├── __init__.py
│   └── main.py
├── Tests/
│   ├── __init__.py
│   └── test_*.py
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

## API Limitations

This project currently uses JSONPlaceholder, a fake online REST API intended for testing and experimentation.

- POST, PUT, and PATCH requests return simulated results; changes are not permanently stored.
- DELETE requests return simulated responses; deleted resources remain available on subsequent requests.
- Some nonexistent resources may return successful HTTP status codes with empty or unexpected response bodies, depending on the endpoint.

These behaviors are characteristics of JSONPlaceholder and are not necessarily representative of a production REST API.

## Future Improvements

- Expand API test coverage.
- Refactor and improve code reusability.
- Extend the tool to support configurable endpoints and other REST APIs.
- Develop a graphical user interface (GUI).
