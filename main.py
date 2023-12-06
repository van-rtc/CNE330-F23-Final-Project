# CNE330 Fall 2023
# Student name: Van Luong Vuong

from cryptography.fernet import Fernet

# Check if the password is strong
def check_strong_password(password):

    upper_count = 0
    lower_passed = False
    symbol_passed = False
    digit_passed = False
    # Check upper, lower, digit and symbol in the password
    for char in password:
        if char.islower():
            lower_passed = True
        elif char.isupper():
           upper_count +=1
        elif char in "!#%@^&*()-+=_.":
           symbol_passed = True
        elif char.isdigit():
           digit_passed = True
    # Check if strong  password
    if lower_passed and upper_count >=3 and symbol_passed and digit_passed:
        print("Password is strong!")
        return True
    else:
        print("Password does not meet the criteria for a strong password for the following reasons:")
        if lower_passed == False:
            print('Password does NOT contain at least 1 lowercase letter')
        if upper_count<3:
            print('Password contain less than 3 uppercase letters from A to Z')
        if symbol_passed == False:
            print('Password does NOT contain at least 1 symbol (!, #, %, @, $, ^, &, *, (, ), -, +, =).')
        if digit_passed == False:
            print('Password does NOT contain at least 1 number (0-9)')
        return False
  
#Encrypt password
def encrypt_password(password, key):
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password

#Main
if __name__ == "__main__":
    #Step 1: Input password
    print("Please enter a password:", end=" ")
    user_password = input()

    # Step 2: Check if the password is strong
    if check_strong_password(user_password):

    # Step 3: Encrypt password using Fernet and save it to a file
        key = Fernet.generate_key()
        encrypted_password = encrypt_password(user_password, key)
        with open("encrypted_password.key", "wb") as file:
            file.write(key)
            file.write(encrypted_password)
            print("Password encrypted and saved to 'encrypted_password.key' file.")
    else:
        print("Password is not strong. Please ensure it meets the criteria:")
        print("•	No less than 3 uppercase letters from A to Z.")
        print("•	At least 1 uppercase letter.")
        print("•	At least 1 number (0-9).")
        print("•	At least 1 symbol (!, #, %, @, $, ^, &, *, (, ), -, +, =).")

