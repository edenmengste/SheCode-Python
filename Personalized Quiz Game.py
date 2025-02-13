score = 0

def greet_player(name="Player"):
    print(f"Hey, {name}! Welcome to Personalized Quiz Game")

def question_one(answer1):
    if answer1.lower() == "east":
        return True
    else:
        return False

def question_two(answer2):
    try:  # Handle potential ValueError if input is not a number
        if int(answer2) == 100:  # Convert to integer for comparison
            return True
        else:
            return False
    except ValueError:
        return False 

def update_score(is_correct):
    global score
    if is_correct:
        score += 1
        print("correct!")
    else:
        print("incorrect!")

def play_quiz():
    name = input("Enter your name here or press enter for default: ") 
    if name == "":
        greet_player()
    else:
        greet_player(name)

    answer1 = input("From which direction does the sun rise? ") 
    is_correct1 = question_one(answer1)
    update_score(is_correct1)
    print(f"your current score is: {score}")

    answer2 = input("Water boils at ___ degree celsius:(enter in number)")
    is_correct2 = question_two(answer2)
    update_score(is_correct2)
    print(f"your current score is: {score}")

    print(f"Thank you for playing! your final score is: {score}")

play_quiz()