"""
This module provides functionality for filtering user data from a `users.json`
file based on specified attributes such as name, age, or email. It includes
separate functions for filtering by each attribute and displays the filtered
results. The module is designed for command-line interaction.

Functions
---------
filter_users_by_name(name):
    Filters the user data based on the provided name parameter.

filter_by_age(age):
    Filters the user data based on the provided age parameter.

filter_by_email(email):
    Filters the user data based on the provided email parameter.
"""
import json


def filter_users_by_name(name):
    """
    Filters the users from a JSON file based on a provided name and prints the
    filtered users.

    :param name: The name used to filter the users
    :type name: str
    :return: None
    """
    with open("users.json", "r", encoding='utf8') as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    """
    Filters a list of users by their age and prints the filtered users.

    :param age: The age to filter users by
    :type age: int
    :return: None
    """
    with open("users.json", "r", encoding='utf8') as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """
    Filters a list of users loaded from a JSON file based on a provided email address.

    :param email: Email address to filter users by
    :type email: str
    :return: None
    """
    with open("users.json", "r", encoding='utf8') as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name, age, email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter a age to filter users: ").strip())
        filter_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
