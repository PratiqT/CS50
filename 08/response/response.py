from validator_collection import email
try:
    address = input("What's your email address? ")
    validate_email = email(address)
    print("Valid")
except ValueError:
    print("Invalid")

