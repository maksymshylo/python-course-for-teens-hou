# Кроки 1-5: Розрахунок кавових запасів
cafe_name = "Кава та Код"
baristas_count = 2
coffee_bags = 15
cups_per_bag = 40
total_cups = coffee_bags * cups_per_bag

# Кроки 6-10: Логіка бару та розподіл чайових
daily_consumption = 60 * 2
days_of_coffee = total_cups / daily_consumption
print(days_of_coffee)
coffee_machine_ready = True
water_filter_clogged = False
bar_ready = coffee_machine_ready and water_filter_clogged == False
print(bar_ready)
tips_per_barista = 300 / baristas_count
print(tips_per_barista)

# Кроки 11-15: Очищення сигналу, довжина та зрізи
raw_title = "   ☕ COFFEE_OF_THE_DAY: cappuccino   "