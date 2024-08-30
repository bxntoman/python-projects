def selection():
    sex = input("Please enter your sex (m/f): ")
    if sex == 'm':
        calculateM()
    elif sex == 'f':
        calculateF()
    else:
        print("Invalid input, please enter either 'm' or 'f'.")
        selection()
        
def calculateM():
    age = int(input("How old are you?: "))
    meSystem = input("Metric or Imperial system? ('m' or 'i'): ")
    if meSystem == 'm':
        weight = float(input("How much do you weigh in kg?: "))
        height = float(input("How tall are you in cm?: "))
        bmr = (10 * weight + 6.25 * height - 5 * age + 5)
        activitiesC(bmr)
    elif meSystem == 'i':
        weight = float(input("How much do you weigh in pounds: "))
        height = float(input("How tall are you in inches?: "))
        bmr = (10 * (weight / 2.205) + 6.25 * (height * 2.54) - 5 * age + 5)
        activitiesC(bmr)
    else:
        print("Invalid input, please enter either 'm' or 'i'.")
        return calculateM()
   

def calculateF():
    age = int(input("How old are you?: "))
    meSystem = input("Metric or Imperial system? ('m' or 'i'): ")
    if meSystem == 'm':
        weight = float(input("How much do you weigh in kg?: "))
        height = float(input("How tall are you in cm?: "))
        bmr = (10 * weight + 6.25 * height - 5 * age - 161)
        activitiesC(bmr)
    elif meSystem == 'i':
        weight = float(input("How much do you weigh in pounds: "))
        height = float(input("How tall are you in inches?: "))
        bmr = (10 * (weight / 2.205) + 6.25 * (height * 2.54) - 5 * age - 161)
        activitiesC(bmr)
    else:
        print("Invalid input, please enter either 'm' or 'i'.")
        return calculateF()

def activitiesC(bmr):
    print("How much is your activity in a week?")
    print("--------------------")
    print("Enter '1' if you are sedentary (little or no exercise)")
    print("Enter '2' if you are lightly active (light exercise/sports 1-3 days​/week)")
    print("Enter '3' if you are moderately active (moderate exercise/sports 3-5 days/week)")
    print("Enter '4' if you are very active (hard exercise/sports 6-7 days a week)")
    print("Enter '5' if you are extra active (very hard exercise/sports & physical job)")
    activityLevel = input("")
    if activityLevel == '1':
        print("--------------------")
        print(f"Your Basal Metabolic Rate (BMR) is {round(bmr)} calories a day while")
        print(f"your maintenance calories are {round(bmr * 1.2)} calories a day")
    elif activityLevel == '2':
        print("--------------------")
        print(f"Your Basal Metabolic Rate (BMR) is {round(bmr)} calories a day while")
        print(f"your maintenance calories are {round(bmr * 1.375)} calories a day") 
    elif activityLevel == '3':
        print("--------------------")
        print(f"Your Basal Metabolic Rate (BMR) is {round(bmr)} calories a day while")
        print(f"your maintenance calories are {round(bmr * 1.55)} calories a day") 
    elif activityLevel == '4':
        print("--------------------")
        print(f"Your Basal Metabolic Rate (BMR) is {round(bmr)} calories a day while")
        print(f"your maintenance calories are {round(bmr * 1.725)} calories a day") 
    elif activityLevel == '5':
        print("--------------------")
        print(f"Your Basal Metabolic Rate (BMR) is {bmr} calories a day while")
        print(f"your maintenance calories are {round(bmr * 1.9)} calories a day") 
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
        return activitiesC(bmr)
         

print("--------------------")
print("Calorie Calculator")
print("--------------------")
print("Press 'f' to start")
start = input("")
if start == "f":
    selection()
else:
    print("Invalid input, please enter 'f' to start.")