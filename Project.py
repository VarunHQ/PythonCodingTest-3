# Part 1
students_score = {"Dev": 80, "Pradeep": 79, "Ravi": 90, "Booshan": 88, "Ganesh": 70}
# Part 2
for average in students_score.values():
    total = sum(students_score.values())
    strength = len(students_score)
    average = total / strength
# Part 3
print("Highest score is: ", max(students_score.values()))
print("Lowest score is: ", min(students_score.values()))
print("Average score: ", average)
# Part 4
name = input("Enter name of student to check their score: ")
# Part 5
print("Score of", name, "is: ", students_score.get(name, "The specified student name is missing in the mark list. Please try again with a valid name in the mark list."))
    