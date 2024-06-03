import tkinter

window = tkinter.Tk()
window.title("Miles to Km converter")


# Entry

input = tkinter.Entry()
input.grid(column=1, row=0)

# label

label_1 = tkinter.Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = tkinter.Label(text="is equal to ")
label_2.grid(column=0, row=1)

label_3 = tkinter.Label(text="        ")
label_3.grid(column=1, row=1)

label_4 = tkinter.Label(text="Km")
label_4.grid(column=2, row=1)


def is_clicked():
    value = input.get()
    km = int(value)*1.609
    label_3.config(text=km)



# Button

button1 = tkinter.Button(text="Calculate", command=is_clicked)
button1.grid(column=1,row=2)

window.mainloop()
