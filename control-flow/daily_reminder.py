#Python script that uses conditional statements, Match Case, and loops to remind the user about a single, 
# priority task for the day based on time sensitivity
# script will ask the user for a single task, its priority level, and if it is time-sensitive


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("")