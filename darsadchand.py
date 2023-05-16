from tabulate import tabulate

lessons_percentage = []
showTable = True


def calculatePercentage(correct, incorrect, total_questions):
    return round(((3 * correct - incorrect) / (3 * total_questions)) * 100, 2)


def getLessons():
    global showTable

    lessons_amount = int(input("Number of your exam lessons: "))
    for i in range(1, lessons_amount + 1):
        lesson_name = input("Lesson name: ")
        total_questions = int(input("Total: "))
        correct = int(input("Correct: "))
        incorrect = int(input("Incorrect: "))
        print()
        if (correct + incorrect) <= total_questions:
            lesson_percentage = calculatePercentage(correct, incorrect, total_questions)
            lessons_percentage.append([lesson_name, lesson_percentage])
        else:
            showTable = False
            break


def printPercentages():
    getLessons()
    if showTable:
        print()
        print(tabulate(lessons_percentage, headers=["Lesson", "Percentage"]))
    else:
        print("You entered too many amount of questions, try again...")


while True:
    try:
        printPercentages()
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
