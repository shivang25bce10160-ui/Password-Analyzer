# Password Analyzer
Password Analyzer is a real-world application of Python programming and cybersecurity which is used to give a technical solution designed to address the widespread issue of weak user credentials in digital environments.
## Project Overview
This project is a cybersecurity tool created to evaluate the strength of passwords using a rule-based heuristic approach inspired by cybersecurity principles to protect the users from online vulnerable attacks. Unlike common basic length checkers, this application uses weighted heuristic engine to analyze ccharacter diversity, randomness, and common keyboard patterns to analyze risk and give feedback to the user to create more secure password.
## Features
### Weighted Scoring Engine
Assigns specific values to uppercase, lowercase, digits, and special characters.
### Pattern Recognition
Detects and penalizes sequential characters (e.g., "abc", "123") and character repetition (e.g., "aaa").
### Entropy Analysis
Evaluates the uniqueness of characters relative to the total length to simulate "randomness" checks.
### Dynamic Feedback
Provides actionable suggestions for users to improve their password security in real-time.
### Risk Rating
Maps scores to descriptive security levels (Strong, Moderate, or Weak).
## Technologies and Tools used
* Language: Python 3.x
* Libraries: string (Standard Library)
* Architecture: Modular Object-Oriented Design
* Standard command-line interface (CLI) for input/output.
* Version Control: Git & GitHub
## Steps to Install and Run the Project
Follow these steps to run the project locally:
1. Ensure you have Python 3.6 or higher installed.
2. Clone the Repository: Use Git to download all project files into a folder on your computer.
3. Run the Application: Execute the main script to start the interactive CLI: python main.py
### How to use
1. Enter the password
2. Review the risk score and security level
3. Follow the Suggestions (e.g., "Missing upper characters") to strengthen your password.
## Instructions for testing
To validate the logic, try the following test cases:
* Weak: 12345 (Should trigger length and sequence penalties).
* Moderate: Password123 (Should trigger a sequence penalty).
* Strong: K9#zL2!pQx (Should receive a high score and "Strong" rating).
## Project Structure
* `main.py`: The entry point of the application (User Interface).
* `analyzer.py`: The core logic class (PasswordAnalyzer) for security calculations.
* `README.md`: Project documentation and setup guide.
* `statement.md`: Detailed problem statement and project scope.
