while True:  
    grade_str = input("Please enter your grade (0-100%): ")

    if not grade_str:  # Check for empty input
        print("Hey! You forgot to enter a grade!")
        continue  # Go back to the beginning of the outer loop

    try:
        grade = float(grade_str)  # Convert input to a number
        if 0 <= grade <= 100:  # Check if grade is within valid range
            if grade >= 90:
                letter_grade = 'A'
                description = "🎉 Awesome!"
            elif grade >= 80:
                letter_grade = 'B'
                description = "🌟 Brilliant!"
            elif grade >= 65:
                letter_grade = 'C'
                description = "👍 Cool!"
            elif grade >= 50:
                letter_grade = 'D'
                description = "😐 Dandy!"
            else:
                letter_grade = 'F'
                description = "🚫 Frown town!"

            print(f"Grade: {grade_str}%")
            print(f"Letter Grade: {letter_grade} - {description}")
            break  # Exit the outer loop if input is valid
        else:
            print("Invalid input. Grade must be between 0 and 100%.")

    except ValueError:
        print("Invalid input. Please enter a number.")