# Sahara Smith
# filename: Student GPAs
# This app will take students names and their GPAs to test if they qualify for the Dean's List or the Honor Roll.
last_name = input("Enter Last Name: ")
if last_name  == 'ZZZ':
    exit("Exiting Program...")
first_name = input("Enter First Name: ")
point_average = float(input("Enter GPA: "))
if point_average >= 3.5:
    print(first_name, last_name, ", you've made the Dean's List!")
elif point_average >= 3.25:
    print(first_name, last_name, ", you've made the Honor Roll!")
else:           # Code for those who do not qualify
    print("Sorry, you did not make the Dean's List or the Honor Roll")