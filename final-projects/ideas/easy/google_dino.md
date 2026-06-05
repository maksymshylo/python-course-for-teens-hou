# 🏆 Фінальний проєкт: Гра «Черепашка-динозавр»

## 📝 Опис проєкту

Гравець керує черепашкою-динозавром 🐢, яка постійно рухається вперед по “пустелі”.

На шляху з’являються перешкоди (камені або кактуси).
Завдання гравця — **вчасно стрибати**, щоб не врізатися.

Якщо зіткнення сталося — гра закінчується.

Посилання на оригінальну гру
https://trex-runner.com/
---

## 🧠 Основна ідея механіки

* Черепашка завжди рухається вперед
* Натискання клавіші **Space** → стрибок
* Перешкоди рухаються зліва направо
* Якщо дистанція мала → програш

---

## 🛠️ Що використовується

* `turtle`
* `random`
* `onkeypress`
* цикл `while`
* координати `xcor()`, `ycor()`
* перевірка колізій (`distance` або координати)

---

## 🧱 Етапи створення

### 1. Ігрове поле

Темний фон (пустеля/ніч):

* жовтий або темно-пісочний фон
* заголовок гри

---

### 2. Гравець (динозавр-черепашка)

```python
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-200, -100)
```

---

### 3. Стрибок

```python
def jump():
    y = player.ycor()
    player.sety(y + 50)
```

Потім повернення вниз:

```python
def gravity():
    y = player.ycor()
    if y > -100:
        player.sety(y - 5)
```

---

### 4. Перешкода

```python
obstacle = turtle.Turtle()
obstacle.shape("square")
obstacle.color("brown")
obstacle.penup()
obstacle.goto(300, -100)
```

---

### 5. Рух перешкоди

```python
obstacle.setx(obstacle.xcor() - 5)

if obstacle.xcor() < -300:
    obstacle.goto(300, -100)
```

---

### 6. Стрибок + керування

```python
screen.listen()
screen.onkeypress(jump, "space")
```

---

### 7. Перевірка програшу

```python
if player.distance(obstacle) < 20:
    print("💥 Гру закінчено!")
    break
```

---

## 📄 Базовий шаблон

```python
import turtle
import random

screen = turtle.Screen()
screen.title("Dino Turtle Game")
screen.bgcolor("tan")
screen.setup(800, 400)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-200, -100)

```

---

## 🚀 Додатковий функціонал

 - Рахунок очок
    ```python
    score += 1
    ```

- Прискорення гри

    Кожні 10 секунд:
    
    ```python
    speed += 1
    ```

- Різні перешкоди
  * маленькі (легко стрибнути)
  * високі (потрібен точний таймінг)

- Два стани стрибка
  * короткий
  * високий (double jump)
