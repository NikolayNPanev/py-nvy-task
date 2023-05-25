import customtkinter
import datetime
from tkinter import messagebox
import csv

all_tasks=[]
work="True"

class Task():

    def __init__(self,taskName, isDone:bool = False, urgency = "Normal",deadline="1/1/1970"):
        self.name = taskName
        self.isDone = isDone
        self.urgency = urgency
        self.deadline = deadline
        self.ParseDeadline()
        print(self)

    def ParseDeadline(self):
        dline = self.deadline.split("/")
        self.day=dline[0]
        self.month=dline[1]
        self.year=dline[2]

    def __eq__(self,name):
        return self.name == name

    def __str__(self) -> str:
        str=f"Task: {self.name}"
        if(self.isDone == "True"):
            str= str+(" : Done!")
        else:
            str= str+(" : Not Done!")
        if(self.urgency == "Urgent"):
            str= str+(" : Urgent!!!")
        if(self.urgency == "Normal"):
            str= str+(" : Normal")
        return str  
    
    
def TasksToCSV():
    global all_tasks
    tfile = open("Tasks.csv","w")
    tfile.writelines("Task,IsDone,Urgency,Deadline\n")
    for t in all_tasks:
        tfile.writelines(f"{t.name},{t.isDone},{t.urgency},{t.deadline}\n")
    tfile.close

def CSVToTasks():
    global all_tasks
    with open("Tasks.csv","r") as f:
        treader = csv.reader(f)
        header = next(treader)
        for row in treader:
            all_tasks.append(Task(row[0],row[1],row[2],row[3]))
    f.close()

def showTask(task):
    global app
    taskName = customtkinter.CTkTextbox(master=app.app_frame,height=20)
    taskName.grid(row=app.app_frame.row+1,column=0,sticky="ew")
    taskName.insert("0.0",task.name)
    taskName.configure(state="disabled")
    if(task.urgency=="Urgent"):
        urgency = customtkinter.CTkTextbox(master=app.app_frame,height=20,text_color="red")
    else:
        urgency = customtkinter.CTkTextbox(master=app.app_frame,height=20)
    urgency.grid(row=app.app_frame.row+1,column=1,sticky="ew")
    urgency.insert("0.0",task.urgency)
    urgency.configure(state="disabled")

    late="False"
    if(int(task.year)<=int(datetime.datetime.now().year)):
        if(int(task.year)<int(datetime.datetime.now().year)):
            late="True"
        elif(int(task.month)<=int(datetime.datetime.now().month)):
            if(int(task.month)<int(datetime.datetime.now().month)):
                late="True"
            elif(int(task.day)<int(datetime.datetime.now().day)):
                late="True"
            elif(int(task.day)>int(datetime.datetime.now().day)-8):
                late="Upcoming"

    if(late=="True"):    
        deadline = customtkinter.CTkTextbox(master=app.app_frame,height=20,text_color="red")
    elif(late=="Upcoming"):
        deadline = customtkinter.CTkTextbox(master=app.app_frame,height=20,text_color="yellow")
    elif(task.urgency=="Urgent"):
        deadline = customtkinter.CTkTextbox(master=app.app_frame,height=20,text_color="yellow")
    else:
        deadline = customtkinter.CTkTextbox(master=app.app_frame,height=20)
    deadline.grid(row=app.app_frame.row+1,column=2,sticky="ew")
    deadline.insert("0.0",task.deadline)
    deadline.configure(state="disabled")
    compBtn = customtkinter.CTkButton(master=app.app_frame,text="Complete Task", command=lambda: removeTask(app.app_frame,task.name))
    compBtn.grid(row=app.app_frame.row+1,column=3,sticky="ew")
    app.app_frame.row=app.app_frame.row+1
    

def saveTask(name,isDone,urgency,deadline):
    global all_tasks
    for task in all_tasks:
        if(task.name==name):
            messagebox.showinfo("Error","Task already exists!")
            return
    all_tasks.append(Task(name,isDone,urgency,deadline))
    print(f"Task {name} saved")
    showTask(all_tasks[-1])

def removeTask(app,name):
    ct=0
    while(ct<len(all_tasks)):
        if(all_tasks[ct].name==name):
            del all_tasks[ct]
            print(f"Task {name} removed")
            refresh()
        ct=ct+1

class AppFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        if(work!="False"):

            super().__init__(master, **kwargs)

            # add widgets onto the frame...


            # create 2x2 grid system
            self.grid_rowconfigure(1, weight=0)
            self.grid_columnconfigure((0, 1), weight=1)

            self.row=0

            self.namelable=customtkinter.CTkLabel(master=self,text="ENTER TASK")
            self.namelable.grid(row=self.row, column=0,columnspan=4)

            self.row=self.row+1 
            self.textbox = customtkinter.CTkTextbox(master=self,height=20)
            self.textbox.grid(row=self.row, column=0, columnspan=4, padx=0, pady=0, sticky="ew")

            self.row=self.row+1
            self.daylable=customtkinter.CTkLabel(master=self,text="DAY")
            self.daylable.grid(row=self.row, column=0)
            self.monthlable=customtkinter.CTkLabel(master=self,text="MONTH")
            self.monthlable.grid(row=self.row, column=1)
            self.yearlable=customtkinter.CTkLabel(master=self,text="YEAR")
            self.yearlable.grid(row=self.row, column=2,columnspan=2)

            self.row=self.row+1
            self.timeday = customtkinter.CTkComboBox(master=self, values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
            self.timeday.grid(row=self.row, column=0, padx=10, pady=10, sticky="ew")
            self.timemonth = customtkinter.CTkComboBox(master=self, values=["1","2","3","4","5","6","7","8","9","10","11","12"])
            self.timemonth.grid(row=self.row, column=1, padx=10, pady=10, sticky="ew")
            years = []
            for y in range(datetime.datetime.now().year,datetime.datetime.now().year+50):
                years.append(f"{y}")
            self.timeyear = customtkinter.CTkComboBox(master=self, values=years)
            self.timeyear.grid(row=self.row, column=2,columnspan=2, padx=10, pady=10, sticky="ew")

            self.row=self.row+1
            self.urgencylable=customtkinter.CTkLabel(master=self,text="URGENCY")
            self.urgencylable.grid(row=self.row, column=0)
            self.combobox = customtkinter.CTkComboBox(master=self, values=["Normal", "Urgent"])
            self.combobox.grid(row=self.row, column=1, padx=10, pady=10, sticky="ew")
            self.button = customtkinter.CTkButton(master=self, text="Add Task", command=lambda: saveTask(f"{self.textbox.get('0.0','end').strip()}",False,f"{self.combobox.get()}",self.timeday.get()+"/"+self.timemonth.get()+"/"+self.timeyear.get()))
            self.button.grid(row=self.row, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
            printAllTasks()

def printAllTasks():
    global all_tasks
    for task in all_tasks:
        showTask(task)

def refresh():
    global app
    app.app_frame.row=4
    for task in app.app_frame.grid_slaves():
        if int(task.grid_info()["row"])>4:
            task.grid_forget()
    printAllTasks()


def quit():
    TasksToCSV()
    global work
    work = "False"
    global app
    app.quit()

def on_closing(app):
    if(messagebox.askokcancel("Quit","Do you want to quit?")):
        quit()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("NVy Task")
        self.minsize(607, 800)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.app_frame = AppFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.app_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    global app
    app = App()
    time = datetime.datetime.now()
    app.wm_protocol("WM_DELETE_WINDOW", lambda:on_closing(app))
    try:
        CSVToTasks()
        printAllTasks()
    except:
        print("File not found")
    while(work=="True"):
        app.mainloop()                   