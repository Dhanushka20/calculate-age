# Person Class

Welcome to the Person Class repository! This is a Python class implementation that defines a person's attributes such as name, country, and date of birth, and provides methods to set and retrieve these attributes, as well as calculate the person's age.

## Introduction

The Person class is designed to represent individuals with basic personal information and age calculation functionality. It provides a convenient way to manage and retrieve information about a person's identity and age.

## Features

- **Attribute Management**: Set and retrieve a person's name, country, and date of birth.
- **Age Calculation**: Calculate a person's age based on their date of birth.
- **Information Display**: Display a person's details including name, country, and date of birth.

## How to Use

1. **Instantiate the Person Class**: Create a new Person object by providing values for the name, country, and date of birth.
2. **Set and Retrieve Attributes**: Use the provided methods to set and retrieve the person's attributes.
3. **Calculate Age**: Utilize the calculate_person_age() method to determine the person's age.
4. **Display Details**: Use the display_details() method to print the person's information.

## Example Usage

```python
from datetime import date

# Create a Person object
person_1 = Person("John", "America", date(1988, 2, 24))

# Display details and calculate age
person_1.display_details()
print(f"Age is {person_1.calculate_person_age()}")
