import random
import time

print("🐔💣 ЛАБІРИНТ КУРКИ 💣🐔")
print("Ти — курка, яка шукає кукурудзу 🌽")
print("Але десь захована бомба 💥")
print("-" * 35)

cells = ["🌽", "🌽", "🌽", "🌽", "💣"]
random.shuffle(cells)

alive = True
score = 0

while alive:
    print("\n📦 Є 5 коробок:")
    print("1️⃣  2️⃣  3️⃣  4️⃣  5️⃣")

    choice = input("👉 Обери коробку (1-5): ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("🤨 Це не схоже на число від 1 до 5...")
        continue

    choice = int(choice) - 1

    print("\n🐔 Курка йде перевіряти коробку...")
    time.sleep(1)

    if cells[choice] == "💣":
        print("💥 БАБАХ!!!")
        print("🍗 Курка перетворилась на нагетс...")
        print(f"🏆 Твій рахунок: {score}")
        alive = False
    else:
        print("🌽 УРА! Ти знайшов кукурудзу!")
        score += 1

        # новий раунд
        cells = ["🌽", "🌽", "🌽", "🌽", "💣"]
        random.shuffle(cells)

        if score == 3:
            print("🐔 Курка вже підозріло щаслива...")
        elif score == 5:
            print("👑 ТИ КОРОЛЬ КУРЕЙ")
        elif score == 10:
            print("🚨 ТЕБЕ ШУКАЄ KFC 🚨")

print("\n🎮 Гру завершено!")
