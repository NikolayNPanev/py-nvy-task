import tkinter
import customtkinter
import csv

# System settings


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
alltasks = []


# Task functions

class Task():
    def __init__(self,taskName, isDone:bool = False):
        self.name = taskName
        self.isDone = isDone
    
    def __str__(self) -> str:
        if(self.isDone == "True"):
            return f"Task:\n\t{self.name} \: Done!"
        return f"Task:\n\t{self.name} \: Not Done!"

def CreateTask():
    name = taskName.get()
    newTask=Task(name,True)
    alltasks.append(newTask)
    print(newTask)
    del newTask
    del name



def TasksToCSV():
    tfile = open("Tasks.csv","w")
    tfile.writelines("Task,IsDone\n")
    for t in alltasks:
        tfile.writelines(f"{t.name},{t.isDone}\n")
    tfile.close

def CSVToTasks():
    alltasks = []
    with open("Tasks.csv","r") as f:
        treader = csv.reader(f)
        header = next(treader)
        for row in treader:
            alltasks.append(Task(row[0],row[1]))
    return alltasks



# App frame
app = customtkinter.CTk()
app.geometry(f"{(int)(1080/3)}x720")
app.title("NVY-Task")




# UI
saveTasks=customtkinter.CTkButton(app, text="Save Tasks",command=TasksToCSV)
saveTasks.pack()

title = customtkinter.CTkLabel(app,text="Enter task name")
title.pack(padx=10,pady=10)

# UIO

inputTaskName= tkinter.StringVar()
taskName = customtkinter.CTkEntry(app,width=app._max_width,height=40,textvariable=inputTaskName)
taskName.pack()

# Create task button


task=customtkinter.CTkButton(app, text="Create",command=CreateTask)
task.pack(padx=10,pady=10)

def showTask(task:Task):
    title = customtkinter.CTkLabel(app,text=task.name)
    title.pack()
    if(task.isDone == "False"):
        compButton = customtkinter.CTkButton(app,text="Complete")
        compButton.pack()
        return
    title = customtkinter.CTkLabel(app,text="=== COMPLETED ===")
    title.pack()


# Run app

alltasks=CSVToTasks()

for t in alltasks:
    print(t)
    showTask(t)



app.mainloop()

print("\n\n\n\tSaving tasks.....")
TasksToCSV()
