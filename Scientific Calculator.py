import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import cmath
import matplotlib.pyplot as plt
from sympy import symbols, simplify, solve, sympify, diff, integrate, lambdify
from sympy.plotting import plot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ========================
# متغيرات عامة
# ========================
x = symbols('x')
user_vars = {}
angle_mode = "deg"  # deg or rad
history = []
shift_mode = False

# ========================
# دالة التعامل مع الأزرار
# ========================
def click(event):
    global angle_mode, shift_mode
    btn_text = event.widget.cget("text")

    if btn_text == "SHIFT":
        shift_mode = not shift_mode
        update_shift_button()
        return

    if btn_text == "=":
        expression = entry.get()
        try:
            if "=" in expression:
                var, val = expression.split("=")
                var = var.strip()
                val = val.strip()
                val_eval = eval(val, {}, user_vars)
                user_vars[var] = val_eval
                entry.delete(0, tk.END)
                entry.insert(tk.END, f"{var} = {val_eval}")
                history.append(f"{var} = {val_eval}")
            else:
                # دعم الدوال بالرموز والمعادلات
                expr = sympify(expression, locals=user_vars)
                # التقييم العددي النهائي:
                result = expr.evalf()
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
                history.append(f"{expression} = {result}")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "خطأ")

    elif btn_text == "C":
        entry.delete(0, tk.END)

    elif btn_text == "√":
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, math.sqrt(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "خطأ")

    elif btn_text == "π":
        entry.insert(tk.END, str(math.pi))

    elif btn_text == "e":
        entry.insert(tk.END, str(math.e))

    elif btn_text == "Rad/Deg":
        angle_mode = "rad" if angle_mode == "deg" else "deg"
        mode_label.config(text=f"الوضع: {'راديان' if angle_mode == 'rad' else 'درجات'}")

    elif btn_text == "HIST":
        show_history()

    elif btn_text == "VARS":
        show_variables()

    elif btn_text == "RESETVARS":
        user_vars.clear()
        show_message("🚫 تم مسح جميع المتغيرات.")

    elif btn_text == "sin":
        if shift_mode:
            entry.insert(tk.END, "asin(")
        else:
            entry.insert(tk.END, "sin(")

    elif btn_text == "cos":
        if shift_mode:
            entry.insert(tk.END, "acos(")
        else:
            entry.insert(tk.END, "cos(")

    elif btn_text == "tan":
        if shift_mode:
            entry.insert(tk.END, "atan(")
        else:
            entry.insert(tk.END, "tan(")

    elif btn_text == "log":
        if shift_mode:
            entry.insert(tk.END, "10**")
        else:
            entry.insert(tk.END, "log(")

    elif btn_text == "ln":
        entry.insert(tk.END, "ln(")  # يمكنك تطوير ln لاحقاً

    elif btn_text == "GRAPH":
        plot_function()

    elif btn_text == "DeMoivre":
        apply_de_moivre()

    elif btn_text == "Roots of Unity":
        roots_of_unity()

    else:
        entry.insert(tk.END, btn_text)

def update_shift_button():
    if shift_mode:
        shift_btn.config(bg="#FFA500")  # برتقالي
    else:
        shift_btn.config(bg="#f0ad4e")  # أصفر داكن

# ========================
# دوال الرياضيات والرسوميات
# ========================

def show_history():
    if not history:
        messagebox.showinfo("التاريخ", "لا توجد عمليات سابقة.")
    else:
        messagebox.showinfo("التاريخ", "\n".join(history[-20:]))

def show_variables():
    if not user_vars:
        messagebox.showinfo("المتغيرات", "لا توجد متغيرات حالياً.")
    else:
        vars_text = "\n".join([f"{k} = {v}" for k, v in user_vars.items()])
        messagebox.showinfo("المتغيرات الحالية", vars_text)

def show_message(msg):
    messagebox.showinfo("معلومة", msg)

def plot_function():
    expr = simpledialog.askstring("📈 رسم دالة", "أدخل دالة مثل sin(x) أو a*x**2:")
    try:
        expr_sym = sympify(expr, locals=user_vars)
        plot(expr_sym, (x, -10, 10))
        history.append(f"Plot({expr})")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ في الرسم")

def apply_de_moivre():
    try:
        r = float(simpledialog.askstring("📐", "أدخل r (القيمة المطلقة):"))
        theta = float(simpledialog.askstring("📐", "أدخل θ (الزاوية):"))
        n = int(simpledialog.askstring("🔢", "أدخل n (الأس):"))

        theta_rad = theta if angle_mode == "rad" else math.radians(theta)

        rn = r ** n
        cos_part = math.cos(n * theta_rad)
        sin_part = math.sin(n * theta_rad)

        real = rn * cos_part
        imag = rn * sin_part
        result = f"{rn:.4f} × (cos({n}θ) + i·sin({n}θ))\n" \
                 f"= {real:.4f} + {imag:.4f}i"

        messagebox.showinfo("📈 مبرهنة دي موفر", result)
        history.append(f"De Moivre: r={r}, θ={theta}, n={n} → {result}")

        plt.figure(figsize=(5, 5))
        plt.axhline(0, color='gray', lw=1)
        plt.axvline(0, color='gray', lw=1)
        plt.plot([0, real], [0, imag], marker='o', color='purple', label='النتيجة')
        plt.text(real, imag, f" {real:.2f} + {imag:.2f}i", fontsize=10)
        plt.title("تمثيل دي موفر المركب")
        plt.xlabel("Re")
        plt.ylabel("Im")
        plt.grid(True)
        plt.axis("equal")
        plt.legend()
        plt.show()

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ في مبرهنة دي موفر")

def roots_of_unity():
    try:
        n = int(simpledialog.askstring("🔢 جذور الوحدة", "أدخل n (عدد الجذور):"))
        roots = [cmath.exp(2j * math.pi * k / n) for k in range(n)]
        roots_str = "\n".join([f"Root {k}: {root.real:.4f} + {root.imag:.4f}i" for k, root in enumerate(roots)])

        messagebox.showinfo("جذور الوحدة", roots_str)
        history.append(f"Roots of Unity n={n}")

        plt.figure(figsize=(6, 6))
        circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='dotted')
        plt.gca().add_artist(circle)
        plt.axhline(0, color='gray', lw=1)
        plt.axvline(0, color='gray', lw=1)
        for root in roots:
            plt.plot(root.real, root.imag, 'ro')
            plt.text(root.real, root.imag, f"({root.real:.2f},{root.imag:.2f})")
        plt.title(f"جذور الوحدة ل n={n}")
        plt.xlabel("Re")
        plt.ylabel("Im")
        plt.axis('equal')
        plt.grid(True)
        plt.show()

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ في جذور الوحدة")

# ========================
# إنشاء الواجهة (محاكاة كاسيو)
# ========================

root = tk.Tk()
root.title("حاسبة كاسيو العلمية - EcoSentinel")
root.geometry("480x660")
root.configure(bg="#e1e1e1")

entry = tk.Entry(root, font=("Consolas", 24), bd=0, justify="right", bg="white", fg="black", insertbackground="black")
entry.pack(fill=tk.X, padx=15, pady=15, ipady=14)

mode_label = tk.Label(root, text="الوضع: درجات", font=("Arial", 14), bg="#e1e1e1", fg="#333")
mode_label.pack(pady=(0, 10))

btn_font = ("Arial", 16, "bold")
btn_fg_num = "#000000"
btn_bg_num = "#ffffff"
btn_bg_func = "#dcdcdc"
btn_bg_shift = "#f0ad4e"
btn_bg_special = "#ffa500"
btn_active_bg = "#b0b0b0"

btn_frame = tk.Frame(root, bg="#e1e1e1")
btn_frame.pack(padx=10, pady=10)

button_texts = [
    ["SHIFT", "(", ")", "√", "C", "VARS", "RESETVARS"],
    ["sin", "cos", "tan", "log", "ln", "π", "e"],
    ["7", "8", "9", "/", "*", "Rad/Deg", "HIST"],
    ["4", "5", "6", "-", "+", "DeMoivre", "Roots of Unity"],
    ["1", "2", "3", ".", "0", "=", "GRAPH"],
]

for r, row in enumerate(button_texts):
    row_frame = tk.Frame(btn_frame, bg="#e1e1e1")
    row_frame.pack(fill=tk.X, pady=4)
    for c, txt in enumerate(row):
        bg_color = btn_bg_num if txt.isdigit() or txt == "." else btn_bg_func
        if txt == "SHIFT":
            bg_color = btn_bg_shift
        if txt in ["DeMoivre", "Roots of Unity", "GRAPH", "Rad/Deg", "HIST", "RESETVARS", "VARS", "C"]:
            bg_color = btn_bg_special

        btn = tk.Button(row_frame, text=txt, font=btn_font, bg=bg_color, fg=btn_fg_num,
                        activebackground=btn_active_bg, relief=tk.RAISED, bd=2, padx=8, pady=8)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=3)
        btn.bind("<Button-1>", click)

        if txt == "SHIFT":
            shift_btn = btn

root.mainloop()
