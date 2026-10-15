day = input("What day is it? ").lower()
time = input("What time of day? ").lower()

if day != "monday" and day != "tuesday" and day != "wednesday" and day !="thursday" and day !="friday" and day != "saturday" and day != "sunday":
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday")
elif time != "morning" and time != "afternoon" and time != "evening":
    print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")
else:
    if day == "monday" and time == "morning":
        print("Suggestion: Great time for a matcha latte!")
    elif day == "monday" and time == "afternoon":
        print("Suggestion: Time for a healthy lunch!")
    elif day == "monday" and time == "evening":
        print("Suggestion: Time to wind down with some T.V.!")
    elif day == "tuesday" and time == "morning":
        print("Suggestion: A blueberry muffin sounds great for breakfast!")
    elif day == "tuesday" and time == "afternoon":
        print("Suggestion: Time for a break!")
    elif day == "tuesday" and time == "evening":
        print("Suggestion: Time to relax & decompress!")
    elif day == "wednesday" and time == "morning":
        print("Suggestion: Great time for a morning stretch!")
    elif day == "wednesday" and time == "afternoon":
        print("Suggestion: Time for an afternoon tea!")
    elif day == "wednesday" and time == "evening":
        print("Suggestion: Great time for an evening walk!")
    elif day == "thursday" and time == "morning":
        print("Suggestion: Great morning for pilates!")
    elif day == "thursday" and time == "afternoon":
        print("Suggestion: Time for a sandwich break!")
    elif day == "thursday" and time == "evening":
        print("Suggestion: Great night for a movie!")
    elif day == "friday" and time == "morning":
        print("Suggestion: Time for a sweet treat!")
    elif day == "friday" and time == "afternoon":
        print("Suggestion: Great time for a mindfulness practice!")
    elif day == "friday" and time == "evening":
        print("Suggestion: Great time for karaoke night!")
    elif day == "saturday" and time == "morning":
        print("Suggestion: Great morning for some yoga!")
    elif day == "saturday" and time == "afternoon":
        print("Suggestion: Time to go out to brunch!")
    elif day == "saturday" and time == "evening":
        print("Suggestion: Great time to meet with friends!")
    elif day == "sunday" and time == "morning":
        print("Suggestion: Great time to go to the farmer's market!")
    elif day == "sunday" and time == "afternoon":
        print("Suggestion: Great time for some snacks!")
    elif day == "sunday" and time == "evening":
        print("Suggestion: Great time to choose an outfit for tomorrow!")
