def get_grade(average):
    if average >= 90 :
        return "A"
    elif average >= 80 :
            return "B"
    elif average >= 70 :
        return "C"
    elif average >= 60 : 
        return "D"
    else:
        return "F"
def get_valid_greade(subject):
    while True:
        try:
            grade = float(input(f"enter {subject} grade (0-100):"))
            if 0<= grade <=100 :
                return grade
            else:
                print("please enter a grade between 0 and 100 .")
        except ValueError:
            print("please enter a valid number.")
print("="*50)
print("STUDENT GRADE CALCULATOR ")
print("="*40)
name = input("enter student's name :")
while True:
    try:
        num_subject = int(input ("enter number of subject : "))
        if num_subject>0:
            break
        else:
            print ("number of subject must be greater than zero .")
    except ValueError :
        print("please enter a valid number .")
subjects = []
greads = []
for i in range(num_subject):
    print(f"\n--- subject {i+1} ---")
    subject = input("enter subject name :")
    grade = get_valid_greade(subject)
    subjects.append( subject)
    greads.append(grade)
average= sum(greads)/len(greads)
highest_grade = max(greads)
lowest_grade = min(greads)
highest_index = greads.index(highest_grade)
lowest_index = greads.index(lowest_grade)
highest_subject = subjects[highest_index]
lowest_subject = subjects[lowest_index]
final_grade = get_grade(average)
print("\n"+ "="*50)
print(f"Student Name : { name}")
print (f"Average : {average :.2f}")
print(f"Final Grade : {final_grade}")
print(f"Highest      : {highest_grade:.2f} ({highest_subject})")
print(f"Lowest       : {lowest_grade:.2f} ({lowest_subject})")

print("=" * 45)
print(" Thank you for using the calculator!")
print("=" * 45)

