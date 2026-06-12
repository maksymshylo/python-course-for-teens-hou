import tkinter as tk
from tkinter import simpledialog, messagebox


# ==============================================================================
# КЛАС СЛАЙДА
# ==============================================================================
class Slide:
    def __init__(self, title, content, bg_color="#ffffff", fg_color="#222222"):
        self.title = title
        self.content = content
        self.bg_color = bg_color
        self.fg_color = fg_color

    def get_formatted_text(self):
        return f"=== {self.title} ===\n\n{self.content}"


# ==============================================================================
# КЛАС ПРЕЗЕНТАЦІЇ (Універсальний плеєр)
# ==============================================================================
class Presentation:
    # Тепер другим аргументом обов'язково передаємо список об'єктів Slide
    def __init__(self, root, slides_list):
        self.root = root
        self.slides = slides_list  # Зберігаємо отримані слайди
        self.current_slide = 0

        # Якщо передали порожній список, створюємо заглушку, щоб програма не зламалася
        if not self.slides:
            self.slides = [Slide("Порожня презентація", "Будь ласка, додайте слайди.")]

        self.root.title("Інтерактивний ООП Конспект-Слайдшоу")
        self.root.geometry("650x500")
        self.root.configure(bg="#f4f4f6")

        self.create_widgets()
        self.bind_events()
        self.update_slide()

    def create_widgets(self):
        """Створює всі графічні елементи вікна."""
        self.text_area = tk.Text(
            self.root, font=("Courier New", 13), wrap=tk.WORD, bd=2, relief=tk.GROOVE
        )
        self.text_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.tools_frame = tk.Frame(self.root, bg="#f4f4f6")
        self.tools_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

        self.btn_add = tk.Button(
            self.tools_frame,
            text="➕ Додати слайд",
            font=("Arial", 10),
            bg="#e1f5fe",
            command=self.add_slide,
        )
        self.btn_add.pack(side=tk.LEFT)

        self.label_counter = tk.Label(
            self.tools_frame, text="", font=("Arial", 10, "italic"), bg="#f4f4f6"
        )
        self.label_counter.pack(side=tk.RIGHT)

        self.nav_frame = tk.Frame(self.root, bg="#f4f4f6")
        self.nav_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)

        button_font = ("Arial", 10, "bold")

        self.btn_first = tk.Button(
            self.nav_frame, text="⏮ Початок", font=button_font, command=self.go_to_first
        )
        self.btn_first.grid(row=0, column=0, padx=5, sticky="ew")

        self.btn_prev = tk.Button(
            self.nav_frame, text="◀ Назад", font=button_font, command=self.prev_slide
        )
        self.btn_prev.grid(row=0, column=1, padx=5, sticky="ew")

        self.btn_next = tk.Button(
            self.nav_frame, text="Вперед ▶", font=button_font, command=self.next_slide
        )
        self.btn_next.grid(row=0, column=2, padx=5, sticky="ew")

        self.btn_last = tk.Button(
            self.nav_frame, text="Кінець ⏭", font=button_font, command=self.go_to_last
        )
        self.btn_last.grid(row=0, column=3, padx=5, sticky="ew")

    def bind_events(self):
        self.root.bind("<Left>", self.prev_slide)
        self.root.bind("<Right>", self.next_slide)
        self.root.bind("<Home>", self.go_to_first)
        self.root.bind("<End>", self.go_to_last)

    def update_slide(self):
        slide = self.slides[self.current_slide]

        self.text_area.config(state=tk.NORMAL, bg=slide.bg_color, fg=slide.fg_color)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, slide.get_formatted_text())
        self.text_area.config(state=tk.DISABLED)

        self.label_counter.config(
            text=f"Слайд {self.current_slide + 1} із {len(self.slides)}"
        )

        is_first = self.current_slide == 0
        is_last = self.current_slide == len(self.slides) - 1

        self.btn_first.config(state=tk.DISABLED if is_first else tk.NORMAL)
        self.btn_prev.config(state=tk.DISABLED if is_first else tk.NORMAL)
        self.btn_next.config(state=tk.DISABLED if is_last else tk.NORMAL)
        self.btn_last.config(state=tk.DISABLED if is_last else tk.NORMAL)

    def next_slide(self, event=None):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.update_slide()

    def prev_slide(self, event=None):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.update_slide()

    def go_to_first(self, event=None):
        if self.current_slide != 0:
            self.current_slide = 0
            self.update_slide()

    def go_to_last(self, event=None):
        if self.current_slide != len(self.slides) - 1:
            self.current_slide = len(self.slides) - 1
            self.update_slide()

    def add_slide(self):
        title = simpledialog.askstring(
            "Новий крок", "Введіть заголовок слайда:", parent=self.root
        )
        if not title:
            return

        content = simpledialog.askstring(
            "Новий крок",
            "Введіть текст слайда (використовуйте '\\n' для переносу):",
            parent=self.root,
        )
        if not content:
            return

        formatted_content = content.replace("\\n", "\n")
        new_slide = Slide(title=title, content=formatted_content)
        self.slides.append(new_slide)

        if messagebox.askyesno("Успішно", "Слайд додано! Перейти на нього?"):
            self.current_slide = len(self.slides) - 1

        self.update_slide()


# ==============================================================================
# ЗАПУСК ПРОГРАМИ ТА ПІДГОТОВКА ДАНИХ (Зовні класів)
# ==============================================================================
if __name__ == "__main__":
    # Створюємо конкретний контент для уроку по Python
    python_course_slides = [
        Slide(
            title="Урок 1: Введення даних",
            content="Функція input() завжди повертає рядок (тип str).\n\nПриклад:\nname = input('Введіть ім'я: ')",
            bg_color="#e8f5e9",  # Світло-зелений фон
        ),
        Slide(
            title="Урок 2: Приведення типів",
            content="Щоб математично працювати з числами з input(), їх треба конвертувати:\n\nage = int(input('Вік: '))\nheight = float(input('Зріст: '))",
        ),
        Slide(
            title="Урок 3: Функція len()",
            content="len() рахує кількість елементів:\n- У рядках: кількість символів.\n- У списках: кількість елементів.\n\nПриклад: len('Python') поверне 6.",
            bg_color="#e1f5fe",  # Світло-блакитний фон
        ),
    ]

    # Створюємо вікно Tkinter
    window = tk.Tk()

    # Запускаємо презентацію, ПЕРЕДАЮЧИ список слайдів на вхід
    app = Presentation(window, python_course_slides)

    window.mainloop()
