while True:
    name = input("Hey! Please enter your name: ")

    if name == "": 
        print("You forgot to enter your name!")
        continue

    confirm = input(f"Is {name} your name? (yes/no) ") 

    if confirm.lower() == "yes": 
        print("Complete!")
        break
    else:
        print("Please enter your correct name.")