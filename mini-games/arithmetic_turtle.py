import turtle
import random
import time

# --------------------
# Вибір складності
# --------------------
difficulty = input(
    "Оберіть складність (easy, medium, hard): "
).lower()

if difficulty == "easy":
    MAX_NUM = 20
    SHARK_SPEED = 20
    TIME_LIMIT = 15

elif difficulty == "hard":
    MAX_NUM = 1000
    SHARK_SPEED = 40
    TIME_LIMIT = 7

else:
    MAX_NUM = 100
    SHARK_SPEED = 30
    TIME_LIMIT = 10

# --------------------
# Вікно
# --------------------
screen = turtle.Screen()
screen.setup(1000, 500)
screen.title("Втеча від акули")

# --------------------
# Черепаха
# --------------------
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-400, 50)

# --------------------
# Акула
# --------------------
shark = turtle.Turtle()
shark.shape("triangle")
shark.color("gray")
shark.penup()
shark.goto(-400, -50)
shark.setheading(0)

# --------------------
# Інформаційна панель
# --------------------
info = turtle.Turtle()
info.hideturtle()
info.penup()

# --------------------
# Фініш
# --------------------
finish = 400

# --------------------
# Генератори задач
# --------------------
def arithmetic_task():
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)

    op = random.choice(["+", "-", "*"])

    if difficulty == "hard":
        op = random.choice(["+", "-", "*", "%"])

    if op == "+":
        return f"{a} + {b}", str(a + b)

    elif op == "-":
        return f"{a} - {b}", str(a - b)

    elif op == "*":
        return f"{a} * {b}", str(a * b)

    else:
        return f"{a} % {b}", str(a % b)


def conversion_task():

    task_type = random.choice([
        "int_to_float",
        "float_to_int",
        "int_to_bool",
        "float_to_bool",
        "bool_to_int"
    ])

    if task_type == "int_to_float":
        n = random.randint(0, MAX_NUM)
        return f"Що поверне float({n}) ?", str(float(n))

    elif task_type == "float_to_int":
        n = round(random.uniform(0, MAX_NUM), 1)
        return f"Що поверне int({n}) ?", str(int(n))

    elif task_type == "int_to_bool":
        n = random.choice([0, 1, 2, 5, 10])
        return f"Що поверне bool({n}) ?", str(bool(n))

    elif task_type == "float_to_bool":
        n = random.choice([0.0, 0.5, 1.2, -3.4])
        return f"Що поверне bool({n}) ?", str(bool(n))

    else:  # bool_to_int
        b = random.choice([True, False])
        return f"Що поверне int({b}) ?", str(int(b))


def logic_task():
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)
    c = random.randint(1, MAX_NUM)
    d = random.randint(1, MAX_NUM)

    expr = f"{a}>{b} and {c}<{d}"

    if difficulty == "hard":
        expr = f"({a}>{b}) or ({c}=={d})"

    return expr, str(eval(expr))


def generate_task():
    return random.choice([
        arithmetic_task,
        conversion_task,
        logic_task
    ])()

# --------------------
# Гра
# --------------------
score = 0

while True:

    task, answer = generate_task()

    info.clear()
    info.goto(0, 180)
    info.write(
        f"Очки: {score}   Час: {TIME_LIMIT} сек",
        align="center",
        font=("Arial", 16, "bold")
    )

    start = time.time()

    user_answer = screen.textinput(
        "Задача",
        f"{task}\n\nУ вас {TIME_LIMIT} секунд"
    )

    elapsed = time.time() - start

    # Час вийшов
    if elapsed > TIME_LIMIT:

        info.clear()
        info.goto(0, 150)
        info.write(
            "⏰ Час вийшов!",
            align="center",
            font=("Arial", 20, "bold")
        )

        shark.forward(SHARK_SPEED + 20)

    elif user_answer and user_answer.lower() == answer.lower():

        score += 1
        player.forward(50)

    else:

        shark.forward(SHARK_SPEED)

    # Акула рухається кожен раунд
    shark.forward(SHARK_SPEED)

    # Перемога
    if player.xcor() >= finish:

        info.clear()
        info.goto(0, 0)
        info.write(
            f"🏆 Перемога! Очки: {score}",
            align="center",
            font=("Arial", 24, "bold")
        )
        break

    # Поразка
    if shark.xcor() >= player.xcor():

        info.clear()
        info.goto(0, 0)
        info.write(
            "🦈 Акула наздогнала черепаху!",
            align="center",
            font=("Arial", 24, "bold")
        )
        break

screen.mainloop()