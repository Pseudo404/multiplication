import customtkinter
import tkinter
import random

app = tkinter.Tk()
app.geometry("200x400")
app.title("Multiplication - Quiz")
app.config(bg="white", borderwidth=0)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app.config(bg="#1a1a1a")
app.resizable(False, False)

def button_event():
    global a, b, nb_correct, nb_questions
    rep = entry.get()
    ret = a * b
    nb_questions += 1
    label3.configure(text=f"{nb_correct} / {nb_questions}")
    if rep.isdigit() and int(rep) == int(ret):
        nb_correct += 1
        label3.configure(text=f"{nb_correct} / {nb_questions}")
        label2.configure(text="+1 bonne réponse")
    else:
        label2.configure(text="-1 mauvaise réponse")
    entry.delete(0, tkinter.END)
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    label.configure(text=f"{a} x {b} =")

a = random.randint(2, 9)
b = random.randint(2, 9)
nb_correct = 0
nb_questions = 1

button = customtkinter.CTkButton(app, text="Confirmer", command=button_event, corner_radius=5, fg_color="#2b2b2b", hover_color="#3c3c3c", bg_color="#1a1a1a")
button.pack(fill='x')
button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(app, text=f"{a} x {b} =", text_color="#ffffff", fg_color="#1a1a1a", bg_color="#000000", font=customtkinter.CTkFont("Serif", 18, "bold"))
label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

label2 = customtkinter.CTkLabel(app, text="", text_color="#ffffff", bg_color="#1a1a1a", font=customtkinter.CTkFont("Serif", 18, "bold"))
label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label3 = customtkinter.CTkLabel(app, text="0 / 1", text_color="#ffffff", bg_color="#1a1a1a", font=customtkinter.CTkFont("Serif", 18, "bold"))
label3.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

result = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, textvariable=result, text_color="black", fg_color="white", bg_color="#aaaaaa", border_color="#aaaaaa")
entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
entry.lift()

app.mainloop()
