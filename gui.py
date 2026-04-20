import tkinter
import main

# Veeti

#from data import oppilaat

root = tkinter.Tk()
root.title("Student Management System")
root.geometry("700x500")

label = tkinter.Label(root, text="Tervetuloa oppilasjärjestelmään", font=("Arial", 14))
label.pack(pady=10)

#entry = tkinter.Entry(root, font=("Arial", 12))
#entry.pack(pady=10)

#button = tkinter.Button(root, text="Paina tästä", font=("Arial", 12), command=main.valikko)
#button.pack(pady=10)

button = tkinter.Button(root, text="Etsi oppilas", font=("Arial", 12), command=main.valikko)
button.pack(pady=10)

button = tkinter.Button(root, text="Näytä arvosanat", font=("Arial", 12), command=main.valikko)
button.pack(pady=10)

button = tkinter.Button(root, text="Poista oppilas", font=("Arial", 12), command=main.valikko)
button.pack(pady=10)

button = tkinter.Button(root, text="Lisää oppilas", font=("Arial", 12), command=main.valikko)
button.pack(pady=10)

button = tkinter.Button(root, text="Näytä oppilaat", font=("Arial", 12), command=main.valikko)
button.pack(pady=10)

result_label = tkinter.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)



root.mainloop()
