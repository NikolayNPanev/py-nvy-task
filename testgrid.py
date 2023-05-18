import customtkinter

all_tasks=[]
work="True"

class Task():
    def __init__(self,taskName,urgency = "Normal", isDone:bool = False):
        self.name = taskName
        self.isDone = isDone
        self.urgency = urgency
        print(self)
    
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


def showTask(app,task):
    taskName = customtkinter.CTkTextbox(master=app,height=20)
    taskName.grid(row=app.row+1,column=0,sticky="ew")
    taskName.insert("0.0",task.name)
    taskName.configure(state="disabled")
    compBtn = customtkinter.CTkButton(master=app,text="Complete Task", command=lambda: removeTask(app,task.name))
    compBtn.grid(row=app.row+1,column=1,sticky="ew")
    app.row=app.row+1

def saveTask(app,name,isDone,urgency):
    all_tasks.append(Task(name,isDone,urgency))
    print(f"Task {name} saved")
    showTask(app,all_tasks[-1])

def removeTask(app,name):
    ct=0
    while(ct<len(all_tasks)):
        if(all_tasks[ct].name==name):
            del all_tasks[ct]
            print(f"Task {name} removed")
            refresh()
        ct=ct+1
    

def addAndRemove(name,urgency,isDone):
    saveTask(name,urgency,isDone)
    removeTask(name)

class AppFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        if(work!="False"):
            super().__init__(master, **kwargs)

            # add widgets onto the frame...
            self.row=0


            # create 2x2 grid system
            self.grid_rowconfigure(1, weight=0)
            self.grid_columnconfigure((0, 1), weight=1)

            self.saveBtn= customtkinter.CTkButton(master=self,text="Exit",command=quit)
            self.saveBtn.grid(row=0,column=0,columnspan=2,sticky="ew")
            self.textbox = customtkinter.CTkTextbox(master=self,height=20)
            self.textbox.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="ew")
            self.row=self.row+1

            self.combobox = customtkinter.CTkComboBox(master=self, values=["Normal", "Urgent"])
            self.combobox.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
            self.row=self.row+1
            self.button = customtkinter.CTkButton(master=self, text="Add Task", command=lambda: saveTask(self,f"{self.textbox.get('0.0','end').strip()}",f"{self.combobox.get()}",False))
            self.button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

def refresh():
    global app
    app.quit()
    app.destroy()
    app = App()


def quit():
    global work
    work = "False"
    global app
    app.quit()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("NVy Task")
        self.minsize(607, 108)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.app_frame = AppFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.app_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    global app
    app = App()
    while(work=="True"):
        app.mainloop()