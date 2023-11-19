active = True  # This flag controls whether the loop should continue
rollback = False

while active:
    # Prompt the user for input and remove spaces and hyphens from the card number
    if not rollback:
        card_number = input('Πληκτρολογήστε τον αριθμό της κάρτας: ').replace(" ", "", ).replace("-", "")

    if rollback:
        card_number = input('Παρακαλώ επαναλάβετε την εισαγωγή.\nΠληκτρολογήστε τον αριθμό της κάρτας: ').replace(" ", "", ).replace("-", "")

    rollback = False  # This flag is used to indicate if a rollback is needed

    original_card_number = card_number  # Store the original card number for later
    card_number_count = len(card_number)  # Get the length of the card number

    # Check for empty input
    if card_number == '':
        print('Κενή Είσοδος')
        continue  # Skip the rest of the loop and prompt for input again

    # Initialize lists and variables for processing
    two_digit_list = []  # List to store doubled digits
    new_card_number = ''  # A modified version of the card number
    total_sum = 0  # The total sum of the digits in the card number

    # Check for non-digit or non-hyphen characters
    for char in card_number:
        if char != '-' and char != ' ' and not char.isdigit():
            print('Μη επιτρεπτός χαρακτήρας: ' + char)
            rollback = True  # Set the rollback flag if an invalid character is found
            break

    # If non-digit characters are found, continue to the next iteration
    if rollback:
        continue

    # Check for the card number length and empty input
    if card_number_count != 16 or card_number == ' ':
        print('Ο αριθμός πρέπει να έχει 16 ψηφία. ')
        rollback = True
        continue  # Skip the rest of the loop and prompt for input again

    # Process the card number
    for i in range(0, len(card_number)):
        char = card_number[i]
        digit = int(char)

        if i == 0 or i % 2 == 0:  # Check if the index is odd
            digit *= 2
            if digit > 9:
                two_digit_list.append(digit)
            new_card_number += str(digit)
        else:
            new_card_number += char

    card_number = new_card_number  # Update the card number with the processed one

    # Replace doubled digits greater than 9 with their sum
    for item in two_digit_list:
        str_item = str(item)
        replacement = int(str_item[0]) + int(str_item[1])
        card_number = card_number.replace(str_item, str(replacement))

    # Recalculate the card number count
    card_number_count = len(card_number)

    # Calculate the total sum of digits
    for i in range(card_number_count):
        char = card_number[i]
        if char.isdigit():
            digit = int(char)
            total_sum += digit

    # Format the card number with hyphens every four digits
    formatted_card_number = '-'.join([original_card_number[i:i + 4] for i in range(0, len(original_card_number), 4)])

    # Check if the card number is valid
    if total_sum % 10 == 0:
        print("Ο αριθμός " + formatted_card_number + " είναι ΕΓΚΥΡΟΣ.\nΤέλος προγράμματος.")
        active = False  # Set active False to exit the loop
    else:
        print("Ο αριθμός " + formatted_card_number + " είναι ΑΚΥΡΟΣ.")