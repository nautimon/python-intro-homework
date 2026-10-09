name = input("What is your name? ")
print(f"Hello, {name}!")
hobby = input("What is your favorite hobby? ")
print(f"Your favorite hobby is {hobby}.")

# Error message:
# NameError: name 'Hobby' is not defined. Did you mean: 'hobby'?

# Cause:
# I defined the variable as 'hobby' with a lowercase h, but later used
# 'Hobby' with a capital H. Python variable names are case-sensitive.

# Fix:
# I changed 'Hobby' to 'hobby', and the script worked.