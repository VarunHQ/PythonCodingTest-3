students_score = {"Yugesh": 70, "Arav": 50, "Kavin": 80, "Rohit": 88, "Varun": 90}
for average in students_score.values():
    total = sum(students_score.values())
    strength = len(students_score)
    average = total / strength
print("Highest score in class:  ", max(students_score.values()))
print("Lowest score in class: ", min(students_score.values()))
print("Average score of the class:  ", average)
name = input("Enter name of the student to check their score: ")
print("Score of the name of ", name, "is: ", students_score.get(name, "The specified student name is missing in the mark list. Please try again with a valid name in the mark list."))
    