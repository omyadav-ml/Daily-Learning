# Using While loop while true problems/
while True:
    try:
        user_input=int(input("Enter Positive integer:"))

        if user_input>0:
                print(f"Accepted: {user_input}")
                break
        else:
                print("Invalid input! Number must be postive.")
    except ValueError:
        print("Invalid input ! Please Enter a valid integer.")


