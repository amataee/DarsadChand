from tabulate import tabulate

while True:
    try:
        data = []
        lessons_amount = int(input("Number of your exam lessons: "))
        for i in range(1, lessons_amount + 1):
            lesson_name = input("Lesson name: ")
            total_questions = int(input("Total: "))
            answered = int(input("Correct: "))
            incorrect = int(input("Incorrect: "))
            print()
            lesson_percentage = round(((3 * answered - incorrect) / (3 * total_questions)) * 100, 2)
            data.append([lesson_name, lesson_percentage])
        print()
        print(tabulate(data, headers=["Lesson", "Percentage"]))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")