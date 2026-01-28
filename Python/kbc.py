import datetime
import math


def load_question(document):
    with open(document, "r", encoding="utf-8") as file:
        questions = []
        lines = [line.strip() for line in file if line.strip() != ""]
        for i in range(0, len(lines), 7):
            questions.append({
                "Questions": lines[i],
                "Options": lines[i + 1:i + 5],
                "Answer": lines[i + 5],
                "Amount": lines[i + 6]
            })
        return questions


def save_log(amount, duration):
    now = datetime.datetime.now()
    with open("kbc.txt", "a", encoding="utf-8") as file:
        file.write(f"Date Time: {now}\n")
        file.write(f"Total Duration: {duration}\n")
        file.write(f"Total Amount: {amount}\n\n")


def play_kdc():
    print("Welcome to KBC With AB")
    questions = load_question("question.txt")

    total_amount = 0
    start_time = datetime.datetime.now()
    print(f"Game Started At: {start_time.strftime('%d:%m:%y %H:%M:%S')}")

    for i in range(min(15, len(questions))):
        print(f"\nQuestion {i + 1} | Amount: {questions[i]['Amount']}")
        print(questions[i]["Questions"])

        for idx, opt in enumerate(questions[i]["Options"], 1):
            print(f"{idx}. {opt}")

        try:
            choice = int(input("Enter Choice (1-4): "))
        except ValueError:
            print("Invalid input! Game Over.")
            break

        if choice == int(questions[i]["Answer"]):
            total_amount += int(questions[i]["Amount"])
            bonus = math.sqrt(total_amount)
            print("Correct Answer!")
            print(f"Total Amount: {total_amount}")
            print(f"Bonus Points: {bonus:.2f}")
        else:
            print(" Incorrect Answer! Game Over.")
            break

    endtime = datetime.datetime.now()
    duration = endtime - start_time
    print("\n--- Game Over ---")
    print(f"Total Duration: {duration}")
    print(f"Total Winning Amount: {total_amount}")

    save_log(total_amount, duration)


play_kdc()
