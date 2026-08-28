# Password Policy Checker

An educational Python project that evaluates whether a password follows a basic set of rules and provides recommendations for missing criteria.

The project includes a terminal interface and a small Streamlit web interface. Passwords are analyzed only while the program is running and are not stored by the application.

## Features

- minimum length verification;
- uppercase and lowercase letter checks;
- numeric character check;
- special character check;
- detection of three consecutive repeated characters;
- score and classification;
- recommendations for failed criteria;
- terminal and web interfaces;
- automated tests with Python's standard library.

## Project Structure

```text
password-policy-checker/
├── app.py                         # Streamlit interface
├── password_checker.py            # validation rules and terminal interface
├── requirements.txt               # web interface dependency
└── tests/
    └── test_password_checker.py    # automated tests
```

## Requirements

- Python 3.10 or newer;
- Streamlit, only for the web interface.

## Running in the Terminal

```bash
python password_checker.py
```

The terminal uses `getpass`, so the typed password is not displayed on the screen.

## Running the Web Interface

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Running the Tests

```bash
python -m unittest discover -s tests -v
```

## Example Policy

The current policy checks six criteria:

1. at least 8 characters;
2. at least one uppercase letter;
3. at least one lowercase letter;
4. at least one number;
5. at least one special character;
6. no character repeated three times consecutively.

## Limitations

This application is a learning project, not a professional password auditing tool. Meeting every rule does not guarantee that a password is strong or resistant to attacks. The checker does not calculate entropy, compare passwords with leaked databases, or replace secure authentication practices.

Do not enter a real password into educational or untrusted applications.

## Learning Goals

This project practices:

- functions;
- strings and loops;
- dictionaries and lists;
- conditionals;
- input validation;
- separation between application logic and interface;
- basic automated testing.
