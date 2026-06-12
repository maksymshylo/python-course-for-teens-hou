import random

QUESTIONS = [

    # -------------------
    # Арифметика
    # -------------------

    ("1 + 1", "2"),
    ("5 - 2", "3"),
    ("3 * 4", "12"),
    ("8 // 2", "4"),
    ("7 % 3", "1"),
    ("2 ** 3", "8"),
    ("10 + 15", "25"),
    ("20 - 7", "13"),
    ("9 * 9", "81"),
    ("100 // 10", "10"),

    # -------------------
    # Порівняння
    # -------------------

    ("5 > 3", "True"),
    ("5 < 3", "False"),
    ("10 == 10", "True"),
    ("10 != 10", "False"),
    ("7 >= 7", "True"),
    ("2 <= 1", "False"),
    ("15 > 20", "False"),
    ("8 == 4 * 2", "True"),
    ("9 != 3 * 3", "False"),
    ("100 < 200", "True"),

    # -------------------
    # bool
    # -------------------

    ("bool(0)", "False"),
    ("bool(1)", "True"),
    ("bool(-1)", "True"),
    ("bool(100)", "True"),
    ("bool(0.0)", "False"),
    ("bool(0.1)", "True"),
    ("bool(False)", "False"),
    ("bool(True)", "True"),

    # -------------------
    # int
    # -------------------

    ("int(True)", "1"),
    ("int(False)", "0"),
    ("int(3.9)", "3"),
    ("int(5.0)", "5"),
    ("int(-2.8)", "-2"),
    ("int(bool(0))", "0"),
    ("int(bool(5))", "1"),

    # -------------------
    # float
    # -------------------

    ("float(5)", "5.0"),
    ("float(True)", "1.0"),
    ("float(False)", "0.0"),
    ("float(10)", "10.0"),
    ("float(-3)", "-3.0"),
    ("float(int(True))", "1.0"),

    # -------------------
    # str
    # -------------------

    ("str(5)", "5"),
    ("str(0)", "0"),
    ("str(True)", "True"),
    ("str(False)", "False"),
    ("str(3.14)", "3.14"),
    ("str(-10)", "-10"),

    # -------------------
    # len
    # -------------------

    ("len('cat')", "3"),
    ("len('Python')", "6"),
    ("len('12345')", "5"),
    ("len(str(123))", "3"),
    ("len(str(True))", "4"),
    ("len('')", "0"),

    # -------------------
    # Конкатенація рядків
    # -------------------

    ("'Py' + 'thon'", "Python"),
    ("'1' + '2'", "12"),
    ("'Hello ' + 'World'", "Hello World"),
    ("str(5) + str(6)", "56"),
    ("'A' + 'B' + 'C'", "ABC"),

    # -------------------
    # Множення рядків
    # -------------------

    ("'a' * 3", "aaa"),
    ("'ab' * 2", "abab"),
    ("'Python' * 2", "PythonPython"),
    ("'5' * 4", "5555"),
    ("'Hi' * 3", "HiHiHi"),

    # -------------------
    # Індексація
    # -------------------

    ("'Python'[0]", "P"),
    ("'Python'[1]", "y"),
    ("'Python'[5]", "n"),
    ("'Cat'[2]", "t"),
    ("'12345'[3]", "4"),

    # -------------------
    # and
    # -------------------

    ("True and True", "True"),
    ("True and False", "False"),
    ("False and True", "False"),
    ("False and False", "False"),
    ("5 > 3 and 2 < 1", "False"),
    ("10 > 5 and 1 == 1", "True"),

    # -------------------
    # or
    # -------------------

    ("True or False", "True"),
    ("False or False", "False"),
    ("5 > 10 or 3 < 5", "True"),
    ("1 == 2 or 2 == 3", "False"),
    ("bool(0) or bool(5)", "True"),

    # -------------------
    # not
    # -------------------

    ("not True", "False"),
    ("not False", "True"),
    ("not(5 > 3)", "False"),
    ("not(5 < 3)", "True"),
    ("not(bool(0))", "True"),

    # -------------------
    # Комбінації типів
    # -------------------

    ("bool(int(0.0))", "False"),
    ("bool(int(5.0))", "True"),
    ("int(bool(100))", "1"),
    ("float(bool(0))", "0.0"),
    ("bool(float(0))", "False"),
    ("bool(float(1))", "True"),

    # -------------------
    # Хитрі питання
    # -------------------

    ("bool('False')", "True"),
    ("bool('0')", "True"),
    ("bool(' ')", "True"),
    ("len(str(False))", "5"),
    ("str(1 + 2)", "3"),
    ("int('10') + int('20')", "30"),
    ("str(10 + 20)", "30"),
    ("'5' + str(5)", "55"),
    ("str(bool(''))", "False"),
    ("bool(str(False))", "True"),

    # -------------------
    # Складні комбінації
    # -------------------

    ("(5 > 3) and (10 < 20)", "True"),
    ("(5 > 10) or (2 < 3)", "True"),
    ("not((5 > 3) and (1 == 1))", "False"),
    ("bool(int(bool(5)))", "True"),
    ("int(bool(float(0)))", "0"),
    ("float(int(bool(True)))", "1.0"),
    ("not(bool(int(0)))", "True"),
    ("bool(5) and not(bool(0))", "True"),
    ("(10 > 5) and not(3 > 7)", "True"),
    ("not((2 > 1) or (5 < 1))", "False"),
]


def get_random_question():
    return random.choice(QUESTIONS)


def normalize_answer(answer: str) -> str:
    answer = answer.strip()

    if len(answer) >= 2:
        if (answer[0] == '"' and answer[-1] == '"') or \
           (answer[0] == "'" and answer[-1] == "'"):
            answer = answer[1:-1]

    return answer


def check_answer(correct, user):
    return normalize_answer(correct) == normalize_answer(user)


if __name__ == "__main__":

    print("Привіт. Давай вирішимо простенькі задачки!")

    while True:
        question, answer = get_random_question()

        print("Що поверне вираз:")
        print(question)

        user_answer = input("\nВаша відповідь: ")

        if check_answer(correct=answer, user=user_answer):
            print("✅ Правильно!")
        else:
            print(f"❌ Неправильно. Правильна відповідь: {answer}")