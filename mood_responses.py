def mood_response ():
    while True:
        mood = input ("Please enter your mood today: \n").lower()
        if mood == ("happy"):
            return "Great that you're feeling happy!"
        elif mood == ("sad"):
            return "Sucks that you're sad :("
        elif mood == ("excited"):
            return "Why are you so excited?"
        else:
            print("Sorry, I didn't understand that mood. Please try again.")
