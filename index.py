import tkinter as tk

bg_color='skyblue'
radio_fg_color='#0a4d68'
result_color='#0a4d68'

root=tk.Tk()
root.title('Temperature Converter')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg=bg_color)


def convert():
    temperature=float(entry.get())

    if var.get()==1:
        converted_temp=(temperature*9/5)+32
        result_label.config(text=f"{converted_temp:.2f} F")

    elif var.get()==2:
        converted_temp=(temperature-32)*5/9
        result_label.config(text=f"{converted_temp:.2f} C")     

main_label=tk.Label(root,text='Temperature Converter', font=('Rockwell',17,'bold'),bg=bg_color,fg='#2a2f4f')
main_label.pack(pady=20)

entry_label=tk.Label(root,text='Enter temperature',font=('Rockwell',15,'bold'),bg=bg_color)
entry_label.pack()

entry=tk.Entry(root,font=('Rockwell',15))
entry.pack(pady=15)

var= tk.IntVar()

frame=tk.Frame(root,bg=bg_color)
frame.pack(pady=15)

cTof=tk.Radiobutton(frame,text='Celsius to Fahrenheit',variable=var,value=1,font=('Rockwell',12),
                    bg=bg_color,activebackground=bg_color,activeforeground=radio_fg_color)
cTof.grid(row=0,column=0)




fToc=tk.Radiobutton(frame,text=' Fahrenheit to Celsius',variable=var,value=2,font=('Rockwell',12),
                    bg=bg_color,activebackground=bg_color,activeforeground=radio_fg_color)
fToc.grid(row=1,column=0)

cnvrtBtn=tk.Button(root,text='convert',font=('Rockwell',15),bg=bg_color,command=convert)
cnvrtBtn.pack()

result_label=tk.Label(root,text="",font=('Rockwell',17,'bold'),bg=bg_color,fg=result_color)
result_label.pack(pady=15)

root.mainloop()