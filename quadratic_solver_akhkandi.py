
import customtkinter as ctk
import tkinter.messagebox
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def format_number(n):
    return str(int(n)) if n == int(n) else f"{n:.2f}"

class QuadraticApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("حل معادله درجه دوم")
        self.geometry("920x820")
        self.resizable(False, False)
        self.center_window()

        self.label_title = ctk.CTkLabel(self, text="حل معادله ax² + bx + c = 0", font=("B Nazanin", 28, "bold"))
        self.label_title.pack(pady=10)

        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10)

        self.label_a = ctk.CTkLabel(self.input_frame, text="a ضریب :", font=("B Nazanin", 20))
        self.label_a.grid(row=0, column=0, padx=10, pady=5)
        self.entry_a = ctk.CTkEntry(self.input_frame, width=100, font=("B Nazanin", 18))
        self.entry_a.grid(row=0, column=1)

        self.label_b = ctk.CTkLabel(self.input_frame, text="b ضریب :", font=("B Nazanin", 20))
        self.label_b.grid(row=1, column=0, padx=10, pady=5)
        self.entry_b = ctk.CTkEntry(self.input_frame, width=100, font=("B Nazanin", 18))
        self.entry_b.grid(row=1, column=1)

        self.label_c = ctk.CTkLabel(self.input_frame, text="c ضریب :", font=("B Nazanin", 20))
        self.label_c.grid(row=2, column=0, padx=10, pady=5)
        self.entry_c = ctk.CTkEntry(self.input_frame, width=100, font=("B Nazanin", 18))
        self.entry_c.grid(row=2, column=1)

        self.calc_button = ctk.CTkButton(self, text="محاسبه معادله", command=self.solve_equation, font=("B Nazanin", 20))
        self.calc_button.pack(pady=15)

        self.language_note = ctk.CTkLabel(self, text=" لطفاً ضرایب را در حالت صفحه کلید انگلیسی وارد کنید ⚠️", font=("B Nazanin", 16), text_color="red")
        self.language_note.pack(pady=2)
        self.language_note = ctk.CTkLabel(self, text=" طراح : عادل آخکندی", font=("B Nazanin", 16), text_color="blue")
        self.language_note.pack(pady=2)

        self.delta_label = ctk.CTkLabel(self, text="", font=("B Nazanin", 20), text_color="darkblue", anchor="w", justify="left")
        self.delta_label.pack(pady=5)

        self.roots_label = ctk.CTkLabel(self, text="", font=("B Nazanin", 20), text_color="#004d00", anchor="w", justify="left")
        self.roots_label.pack(pady=5)

        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.pack(pady=20, fill="both", expand=True)

    def solve_equation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            if a == 0:
                raise ValueError("ضریب a نمی‌تواند صفر باشد.")

            delta = b**2 - 4*a*c
            delta_text = f"""فرمول دلتا :
Δ = b×b - 4ac = ({format_number(b)})×({format_number(b)}) - 4×({format_number(a)})×({format_number(c)}) = {format_number(delta)}"""
            self.delta_label.configure(text=delta_text)

            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            if delta < 0:
                roots_text = "  منفی است Δ ⇒ این معادله ریشه حقیقی ندارد "
            elif delta == 0:
                x = -b / (2*a)
                roots_text = f""" Δ = 0 ⇒ یک ریشهٔ حقیقی داریم :

x = -b ÷ 2a = -({format_number(b)}) ÷ 2×{format_number(a)} = {format_number(x)}"""
            else:
                sqrt_d = math.sqrt(delta)
                x1 = (-b + sqrt_d) / (2*a)
                x2 = (-b - sqrt_d) / (2*a)
                roots_text = f"""Δ > 0 ⇒ دو ریشه حقیقی داریم :  

x₁ = (-b + √Δ) ÷ 2a = (-({format_number(b)}) + √{format_number(delta)}) ÷ 2×{format_number(a)} = {format_number(x1)}
x₂ = (-b - √Δ) ÷ 2a = (-({format_number(b)}) - √{format_number(delta)}) ÷ 2×{format_number(a)} = {format_number(x2)}"""

            self.roots_label.configure(text=roots_text)

            x_vals = np.linspace(-10, 10, 400)
            y_vals = a * x_vals**2 + b * x_vals + c

            fig, ax = plt.subplots(figsize=(7.5, 4.5))
            ax.plot(x_vals, y_vals, color='darkred', label='y = ax² + bx + c')
            ax.axhline(0, color='black')
            ax.axvline(0, color='black')
            ax.set_title("نمودار سهمی", fontsize=15, fontproperties="Arial")
            ax.grid(True)
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        except ValueError as e:
            tkinter.messagebox.showerror("خطا", str(e))

    def center_window(self):
        self.update_idletasks()
        width = 920
        height = 820
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = QuadraticApp()
    app.mainloop()
