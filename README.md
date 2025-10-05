# Branching Out

A simple Python command-line tool for filtering and searching user data from a JSON file based on various attributes.

## About

This project provides an interactive way to filter user information stored in a `users.json` file. You can search for users by their name, age, or email address through a simple command-line interface.

## Features

- **Filter by Name**: Case-insensitive name search
- **Filter by Age**: Exact age matching
- **Filter by Email**: Exact email address matching
- **Interactive CLI**: User-friendly prompts for easy filtering
- **Multiple Searches**: Option to perform multiple filters in one session

## Getting Started

### Prerequisites

- Python 3.x
- A `users.json` file in the same directory as the script

### users.json Format

Your `users.json` file should follow this structure:

```json
[
  {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
  },
  {
    "name": "Jane Smith",
    "age": 25,
    "email": "jane.smith@example.com"
  }
]
```

### Installation

```bash
# Clone the repository
git clone https://github.com/henrikhorn106/branching-out.git

# Navigate to the project directory
cd branching-out

# Ensure you have a users.json file in the directory
```

## Usage

Run the script from the command line:

```bash
python filter_users.py
```

Follow the interactive prompts:

1. Choose a filter option (name, age, or email)
2. Enter the search value
3. View the filtered results
4. Optionally continue with another search

### Example Session

```
What would you like to filter by? (name, age, email): name
Enter a name to filter users: John Doe
{'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}

Do you want to continue filter for data? (y/n) n
```

## Functions

- `filter_users_by_name(name)`: Filters users by name (case-insensitive)
- `filter_by_age(age)`: Filters users by age (exact match)
- `filter_by_email(email)`: Filters users by email (exact match)

## Contributing

Contributions are welcome! Feel free to submit a Pull Request or open an issue.

## License

This project is open source and available under the MIT License.

## Contact

Henrik Horn - [@henrikhorn106](https://github.com/henrikhorn106)

Project Link: [https://github.com/henrikhorn106/branching-out](https://github.com/henrikhorn106/branching-out)
