from tkinter import *

window=Tk()
window.title("Miles to Kilometer Converter" )

miles_label=Label(text="Miles",font=("Arial",10,"normal"))
miles_label.grid(column=2,row=0)
window.config(padx=20,pady=20)


miles_input= Entry(width=10)
miles_input.grid(column=1,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label=Label(text="0")
km_result_label.grid(column=1,row=1)

km_label=Label(text="km")
km_label.grid(column=2,row=1)


def button_clicked():
    new_text=miles_input.get()
    km_result_label.config(text=str(round(int(new_text)*1.609,2)))

button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=5)





window.mainloop()