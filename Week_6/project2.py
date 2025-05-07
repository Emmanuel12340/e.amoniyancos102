
admitted = []
not_admitted = []

def check_admission():

    name = input("Enter your name: ")
    department = input("Enter your preferred department (Computer Science/Mass Communication): ").strip().lower()
    jamb_score = int(input("Enter your JAMB score: "))
    credits = int(input("How many key subject credits do you have? "))
    interview_passed = input("Did you pass the interview? (yes/no): ").strip().lower()

    if department == "computer science":
        if jamb_score >= 250 and credits >= 5 and interview_passed == "yes":
            print(f"Congratulations, {name}! You are admitted into Computer Science.")
            admitted.append(name)
        else:
            print(f"Sorry, {name}. You did not meet the requirements for Computer Science.")
            not_admitted.append(name)
    
    elif department == "mass communication":
        if jamb_score >= 230 and credits >= 5 and interview_passed == "yes":
            print(f"Congratulations, {name}! You are admitted into Mass Communication.")
            admitted.append(name)
        else:
            print(f"Sorry, {name}. You did not meet the requirements for Mass Communication.")
            not_admitted.append(name)
    

    else:
        print(f"Sorry, {name}. The department '{department}' is not recognized.")
        not_admitted.append(name)

check_admission()

print("\nAdmitted candidates:", admitted)
print("Not admitted candidates:", not_admitted)