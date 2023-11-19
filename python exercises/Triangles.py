active = True
while active:

    number_of_lines = input('Δώστε το n (1-20): ')

    if number_of_lines == '':
        break

    if int(number_of_lines) < 1 or int(number_of_lines) > 20:
        print('Οι αριθμοί πρέπει να είναι στο διάστημα 1-20')
        continue

    for line_number in range(1, int(number_of_lines) + 1):
        print("*" * line_number + "." * ((int(number_of_lines) - line_number) * 2 + 1) + "*" * line_number)

print('Τέλος προγράμματος.')