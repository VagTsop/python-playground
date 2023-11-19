# Credit Card Validator and Pattern Generator
This repository contains two Python scripts: one for validating credit card numbers and another for generating a decorative pattern of stars and dots.

## Credit Card Validator
- Usage:
- Run the script credit_card_validator.py to check the validity of a credit card number.

```sh
python credit_card_validator.py
```
## Description:
- The script prompts the user to input a credit card number, removes spaces and hyphens, and validates the number using the Luhn algorithm. If the entered number is valid, it prints a formatted version of the card number and indicates its validity. If the number is invalid, it prints an error message.

## Note:
- The credit card number must be 16 digits long.
- The script supports hyphens and spaces in the input but removes them during processing.
- It checks for non-digit characters and prompts the user to re-enter the card number if invalid characters are detected.
- The program continues running until the user enters a valid 16-digit credit card number.

## Pattern Generator
- Usage:
- Run the script pattern_generator.py to create a decorative pattern of stars and dots.

```sh
python pattern_generator.py
```
##  Description:
- The script prompts the user to input a number n (1-20) and generates a visually appealing pattern with stars (*) and dots (.) based on the user's input. The pattern consists of n lines, with the number of stars increasing and the number of dots decreasing on each line.

Note:
- The script checks if the input is within the valid range of 1-20 and prompts the user to re-enter the number if it is not.
- The program continues running until the user either enters a valid number or leaves the input empty.
Feel free to use and modify these scripts according to your needs. If you encounter any issues or have suggestions for improvement, please create an issue or submit a pull request. Thank you!# python-playground