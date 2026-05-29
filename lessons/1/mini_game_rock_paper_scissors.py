import random

moves = {
    1: "камінь 🪨",
    2: "ножиці ✂️",
    3: "папір 📄"
}

choose_str = """
🎮 Обери свій хід:
1 — камінь 🪨
2 — ножиці ✂️
3 — папір 📄

👉 Твій вибір: 
"""

computer = random.choice([1, 2, 3])

player = input(choose_str)

n_wrong_inputs = 0

# перевірка вводу
while player not in ["1", "2", "3"]:
    n_wrong_inputs += 1

    if n_wrong_inputs < 2:
        print("❌ Твоя відповідь не зарахована! Спробуй ще раз 😅")

    elif n_wrong_inputs <= 5:
        print("⌨️ Ти точно вмієш користуватись клавіатурою? 😭")

    else:
        print("💀 Ой бідааа... Я вимикаюсь і йду у відпустку 🏖️")
        exit()

    player = input(choose_str)

player = int(player)

print(f"\n🤖 Комп'ютер обрав: {moves[computer]}")
print(f"🧑 Ти обрав: {moves[player]}\n")

# нічия
if player == computer:
    print("🤝 Нічия!")

# перемога гравця
elif (
    (player == 1 and computer == 2) or
    (player == 2 and computer == 3) or
    (player == 3 and computer == 1)
):
    print("🏆 Ти переміг!!! 🎉")

# перемога комп'ютера
else:
    print("💀 Ти програв... 🤖")
