from presentation import Presentation, Slide
import tkinter as tk


def main():
    course_slides = [
        Slide(
            title="Завдання 1: Чистий Код",
            content="Виправляємо хакерський злам та називаємо змінні правильно!\n\n"
            "Ей, поглянь — одну з програм, яку написав наш друг, випадково зламали хакери!\n"
            "Хтось змінив усі назви змінних на ось такий безлад:\n\n"
            "80 = 'Adrienne'\n"
            "98_cookie_39 = 'Chocolate chip cookies'\n"
            "fIrSt_NAMe = 20\n"
            "LAST_name = 'Blue'\n"
            "309384 = 'Adrienne Tacke'\n"
            "Hellllooooooooooooo_8392982r = 'Software Engineer'\n"
            "aPPles_23 = '45'\n"
            "_Cittty_43 = 'Stockholm'\n"
            "0_sTRRRRREEET_34211 = 'Horward 45'\n\n"
            "Джерело: Coding for Kids: Python | Авторка: Адрієнн Такке",
            bg_color="#ffe0b2",  # Orange color
        ),
        Slide(
            title="Золоті правила іменування",
            content="Зверни увагу на ці правила, коли будеш виправляти код хакерів:\n\n"
            "📌 Описовість:\n   Назва має 'говорити' про дані всередині.\n\n"
            "📌 snake_case:\n   Використовуй малі літери та підкреслення '_'.\n\n"
            "📌 Жодних цифр спочатку:\n   Змінна не може починатися з числа.\n\n"
            "📌 Стиль:\n   Будь послідовним у всьому проєкті.",
            bg_color="#fff9c4",  # Yellow color for rules
        ),
    ]

    # Create GUI
    window = tk.Tk()
    app = Presentation(window, course_slides)
    window.mainloop()


if __name__ == "__main__":
    main()
