#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:19:49 2022

@author: rachnashaw
"""

from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning(" Warning! ", " Please enter some task ")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do')
ws.config(bg='#8dc63f')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=19)

#we are adding the list box 

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('times', 18),
    bd=0,
    fg='red',
    highlightthickness=7,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)
task_list = [
    'Wake up early',
    'Excercise',
    'Meditate',
    'Drink 4litres of water',
    'Attend the lectures',
    'Complete the assingments',
    'Make lab report',
    'Attend club sessions',
    'Invest in learning a skill',
    'Refesh yourself or just do your hobby',
    'Have sound sleep'
    ]

for item in task_list:
    lb.insert(END, item)
#assighning scroll bar

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)



#This button is for adding a task
#The fontsize, textfont, background, Padding in x and y are mentioned
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Helvetica'),
    bg='#c5f776',
    padx=25,
    pady=15,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)



#This button is for deleting a task
#The fontsize, textfont, background, Padding in x and y are mentioned

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Helvetica'),
    bg='#ff8b61',
    padx=25,
    pady=15,
    command=deleteTask
)


delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()