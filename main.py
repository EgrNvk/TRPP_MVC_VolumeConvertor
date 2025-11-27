from view import build_gui
from controller import setup_controller

def main():
    root, entry_value, entry_from, entry_to, label_res, button = build_gui()
    setup_controller(entry_value, entry_from, entry_to, label_res, button)
    root.mainloop()

if __name__ == "__main__":
    main()