# 5 Testing

## 5.1 Testing link
The suite of test cases is contained in a separate file:

## 5.2 Known Bugs
1. Blah

## 5.3 Linting
Each piece of code was put through a "checker" to review the quality of the code.

### 5.3.1 HTML
- Website: https://validator.w3.org/nu/#textarea
- Result: All code passed, primarily with the exception of lines containing Jinja2 code. An repeated ID error was also ignored because the line of code is added dynamically and only one of the lines of code will be included.

### 5.3.2 CSS
- Website: https://jigsaw.w3.org/css-validator/validator
- Result: No errors or issues found

### 5.3.3 JavaScript
- Website: https://jslint.com/
- Result: Instances of "Double Quotes" ignored as a decision was made to use single quotes

### 5.3.4 Python
- Website: http://pep8online.com/
- Results: No errors or issues found


# 1 Header
- 1 - If a User is not logged in, is "Register/Login" link displayed?
- 1.1 - Does clicking the link open a drop down
- 1.2 - Does the dropdown contain
    - Register link
    - Login Link
- 1.3 - As a new User is "Cart Empty" displayed
- 1.4 - Does clicking the header logo bring the User to the home page
- 

- 1.5 - On mobile devices with screens below 375, do My Account and Cart sit on opposite sides of teh screen

# 2 Register
- 2.1 - Does clicking the Register link bring me to the "Sign Up" page
- 2.2 - Does clicking the "sign in" above the form link bring me to the "Sign In" page
- 2.3 - Can I add my data into each of the sign up fields
- 2.4 - Do I get an error if any of the fields are empty
- 2.5 - Clicking the Sign Up Button
    - 2.5.1 - Am I brought to a page "Verify Your Email Address"
    - 2.5.2 - Do I receive an email confirmation email
    - 2.5.3 - Does clicking the link bring me to a "Confirm E-Mail Address" page
    - 2.5.4 - Does clicking "Confirm" bring me to the sign in page
    - 2.5.5 - Is a new User added to the Admin section
- If I had products in my cart prior to signing up does the total still display in the header
- If I had products in my cart prior to signing up do I get a "Success" toast

# 3 Login
- 3.1 - Does clicking the Login link bring me to the "Sign In" page?
- 3.2 - Does clicking the "sign up" above the form link bring me to the "Sign Up" page
- 3.3 - Can I add my data into each of the sign up fields
- 3.4 - Do I get an error if any of the fields are empty
- 3.5 - Does clicking the "Sign In " button sign me in and bring me to the home page?

# 4 Nav and Search Bar
- 4.1