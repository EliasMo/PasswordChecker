# password_checker.py 

# Password criteria 
MIN_LENGTH = 8
MIN_UPPERCASE = 1
MIN_LOWERCASE = 1
MIN_DIGITS = 1
MIN_SPECIAL_CHARACTERS = 1
SPECIAL_CHARACTERS = "!@#$%^&*()_[]|;:'<>,.?/~`"

# Get user input 
user_password = input("Enter your password: ")

# Check password strength
if len(user_password) < MIN_LENGTH:
	print("Weak: Password should be at least 8 characters long.")
elif sum(1 for char in user_password if char.isupper()) < MIN_UPPERCASE:
	print("Weak: Password should contain at least one uppercase letter.")
elif sum(1 for char in user_password if char.islower()) < MIN_LOWERCASE:
	print("Weak: Password should contain at least one lowercase letter.")
elif sum(1 for char in user_password if char.isdigit()) < MIN_DIGITS:
	print("Weak: Password should contain at least one digit.")
elif sum(1 for char in user_password if char in SPECIAL_CHARACTERS) < MIN_SPECIAL_CHARACTERS:
	print("Weak: Password should contain at least one special character.")
else:
	print("Strong: Password meets all criteria")


