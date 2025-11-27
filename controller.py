from model import convert_volume

def setup_controller(entry_value, entry_from, entry_to, label_res, button):
    def on_convert():
        text_value = entry_value.get()

        try:
            value=float(text_value)
        except ValueError:
            label_res.config(text="Помилка: введіть число!", fg="red")
            return

        from_unit=entry_from.get()
        to_unit=entry_to.get()

        try:
            result=convert_volume(value, from_unit, to_unit)
        except ValueError as e:
            label_res.config(text=str(e), fg="red")
            return

        label_res.config(text=f"Результат: {result:.6f} {to_unit}", fg="green")

    button.config(command=on_convert)