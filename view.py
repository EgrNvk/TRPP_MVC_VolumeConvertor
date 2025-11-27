import tkinter as tk

def build_gui():
    root = tk.Tk()
    root.title("Конвертор об'ємів (метрична система)")
    root.geometry("800x800")
    root.configure(bg="#f2f2f2")

    label_title = tk.Label(root, text="Конвертор об'ємів",
                           font=("Arial", 15, "bold"), bg="#f2f2f2")
    label_title.pack(pady=(50, 10))

    label_value = tk.Label(root, text="Введіть значення:",
                           font=("Arial", 14), bg="#f2f2f2")
    label_value.pack(pady=(10, 10))

    entry_value = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    entry_value.pack(pady=10)

    frame_units = tk.Frame(root, bg="#f2f2f2")
    frame_units.pack(pady=20)

    label_from = tk.Label(frame_units, text="із одиниці:",
                          font=("Arial", 12), bg="#f2f2f2")
    label_from.pack(pady=10)

    entry_from = tk.Entry(frame_units, font=("Arial", 12),
                          width=10, justify="center")
    entry_from.pack(pady=10)

    label_to = tk.Label(frame_units, text="В одиницю:",
                        font=("Arial", 12), bg="#f2f2f2")
    label_to.pack(pady=10)

    entry_to = tk.Entry(frame_units, font=("Arial", 12),
                        width=10, justify="center")
    entry_to.pack(pady=10)

    text = (
        "Конвертор використовує метричні одиниці об'єму:\n"
        "м3 — кубічний метр\n"
        "дм3 — кубічний дециметр\n"
        "см3 — кубічний сантиметр\n"
        "мм3 — кубічний міліметр"
    )
    label_hint = tk.Label(root, text=text, font=("Arial", 12),
                          fg="gray", bg="#f2f2f2", justify="left")
    label_hint.pack(pady=10)

    label_res = tk.Label(root, text="", font=("Arial", 18, "bold"),
                         fg="blue", bg="#f2f2f2")
    label_res.pack(pady=30)

    button = tk.Button(root, text="Конвертувати",
                       font=("Arial", 14), fg="green")
    button.pack(pady=80)

    return root, entry_value, entry_from, entry_to, label_res, button