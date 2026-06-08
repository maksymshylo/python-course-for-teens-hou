import turtle

# Налаштування екрану
screen = turtle.Screen()
screen.title("Керування WASD")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Створення гравця
player = turtle.Turtle()
player.shape("turtle")
player.color("darkgreen")
player.penup()
player.speed(0)  # Найвища швидкість анімації

# Швидкість руху гравця (на скільки пікселів переміщатися за один крок)
STEP = 20

# Функції для руху
def move_up():
    player.setheading(90)  # Повертаємо голову вгору (90 градусів)
    player.forward(STEP)

def move_down():
    player.setheading(270) # Повертаємо голову вниз (270 градусів)
    player.forward(STEP)

def move_left():
    player.setheading(180) # Повертаємо голову ліворуч (180 градусів)
    player.forward(STEP)

def move_right():
    player.setheading(0)   # Повертаємо голову праворуч (0 градусів)
    player.forward(STEP)

# Пов'язуємо клавіші з функціями (літери мають бути маленькими!)
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# ГОЛОВНИЙ СЕКРЕТ: змушуємо екран "слухати" натискання клавіш
screen.listen()

# Запуск гри
screen.mainloop()