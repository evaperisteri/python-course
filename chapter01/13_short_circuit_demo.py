name = "Bob"
print("---------or----------")
valid_user = None or "User"

print("Hello", valid_user)

print("-" * 20)
valid_user = name or "User"

print("---------and----------")

email = "example@email.com"
valid_email = email and email != "example@email.com"
print("Valid email:", valid_email)
if valid_email:
  print(f"Hello {valid_user}, your email is: {email}")
else:
  print(f"Hello {valid_user}, please provide your email.")