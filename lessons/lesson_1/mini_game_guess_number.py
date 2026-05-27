import random

secret = random.randint(1, 10)

print("🎮 Вгадай число від 1 до 10")

while True:
    guess = int(input("Твоя відповідь: "))

    if guess == secret:
        print("🏆 Ти переміг!")
        break

    elif guess < secret:
        print("⬆ Загадане число більше")

    else:
        print("⬇ Загадане число менше")