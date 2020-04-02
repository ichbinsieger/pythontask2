import random
import string
print("Fill this form accordingly")
def form():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")


    def randomstring(stringlength=5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringlength))


    random_password = f'{first_name[0:2]}{last_name[-2:]}{randomstring()}'
    print('Password: ',random_password)
    decision = input("Do you wish to use the above generated password?(yes/no) ")
    if decision == "yes":
        print(" Here is a summary of your details ")
        print((f'First name: {first_name}     '
               f'Last name: {last_name}     '
               f'Email: {email}     '
               f'your password: {random_password} '))
    elif decision == "no":
        user_password = input("Enter preferred password: ")
        while len(user_password) < 7:
            print("your password must be a minimum of 7 characters")
            user_password = input("Enter preferred password: ")
        print("Here is a summary of your details: ")
        print((f'First name: {first_name}     '
               f'Last name: {last_name}     '
               f'Email: {email}     '
               f'your password: {user_password} '))
        new = input("Do you wish to enter details of a new user?(yes/no) ")

form()
new = input("Do you wish to enter details of a new user?(yes/no) ")
if new == "no":
    print("End of form")
elif new == "yes":
    form()