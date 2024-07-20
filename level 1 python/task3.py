from email_validator import validate_email, EmailNotValidError

email = "ashisingh34@gmail.com"
try:
    valid = validate_email(email)
    print("Valid email:", valid.email)
except EmailNotValidError as e:
    print("Invalid email:", str(e))


