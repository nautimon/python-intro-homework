score = int(input ("Enter a number "))

def is_valid_score(score):
    if score >100 or score < 0:
        return False
    elif score >=0 and score <= 100:
        return True

if is_valid_score(score):
    print("Valid score")
else:
    print("Invalid score - must be between 0 and 100")
