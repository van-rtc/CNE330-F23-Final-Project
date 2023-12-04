
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
        print("Password does not meet the criteria for a strong password for the following reasons:.")
        if lower_passed == False:
            print('Password does NOT contain at least 1 lowercase letter')
        if upper_count<3:
            print('Password contain less than 3 uppercase letters from A to Z')
        if symbol_passed == False:
            print('Password does NOT contain at least 1 symbol (!, #, %, @, $, ^, &, *, (, ), -, +, =).')
        if digit_passed == False:
            print('Password does NOT contain at least 1 number (0-9)')
        return False
  
              


if __name__ == "__main__":
    print("Create a strong password:")
    password = input("Password: ")
    check_strong_password(password)