import tkinter as tk
from tkinter import filedialog, Text
import os

main=tk.Tk()
main.title("appProfiler")
main.geometry("350x350")
main.configure(bg="Grey15")

def appProfiler(num):
    main.destroy()

    root = tk.Tk()

    if num==1:
        root.title("Work")
    if num==2:
        root.title("Game")
    if num==3:
        root.title("Other")

    apps = []
    root.configure(bg="Grey15")

    if num==1:
        if os.path.isfile('work.txt'):
            with open('work.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]

    if num==2:
        if os.path.isfile('game.txt'):
            with open('game.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]

    if num==3:
        if os.path.isfile('other.txt'):
            with open('other.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]

    def addApp():
        for widget in frame.winfo_children():
            widget.destroy()

        file = filedialog.askopenfile(initialdir='/', title='Select file',
                                      filetypes=[("Executables", ' *.exe'), (
                                      "Documents", ['*.doc', '*.docx', '*.txt', '*.pdf', '*.ppt', '*.pptx ']),
                                                 ("All Files", ["*.*"])])
        apps.append(file.name)
        for app in apps:
            label = tk.Label(frame, text=os.path.basename(app),font=("arial",10), bg="Grey23", fg="White")
            label.pack()

    def runApp():
        for app in apps:
            os.startfile(app)

    def deleteApp():
        delApps = tk.Tk()
        delApps.title("Delete")

        def onClick():
            for app in apps:
                deleted = delEntry.get()
                if deleted == os.path.basename(app):
                    apps.remove(app)

            for widget in frame.winfo_children():
                widget.destroy()

            for app in apps:
                 label = tk.Label(frame, text=os.path.basename(app),font=("arial",10), bg="Grey23", fg="White")
                 label.pack()

        delCanvas = tk.Canvas(delApps, height=500, width=500, bg="Gray15")
        delCanvas.pack()

        delLabel = tk.Label(delCanvas, padx=10, pady=10, text="Enter the App to be DELETED:",font=("arial",10), bg="Gray15", fg="White")
        delLabel.pack(padx=10, pady=10)

        delEntry = tk.Entry(delCanvas, bg="Gray23", fg="White",font=("arial",10))
        delEntry.pack(padx=10, pady=10)

        Confirm = tk.Button(delCanvas, text="Confirm",font=("arial",10), command=onClick, padx=5, pady=5, bg="Gray23", fg="White")
        Confirm.pack(padx=10, pady=10)

        delApps.mainloop()

    canvas = tk.Canvas(root, height=600, width=700, bg="Gray15")
    canvas.pack()

    frame = tk.Frame(root, bg='Gray23')
    frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.05)

    openApps = tk.Button(root, text='Open File',font=("arial",10), padx=10, pady=5, command=addApp, bg="Gray23", fg="White")
    openApps.pack(padx=5, pady=5)

    runApps = tk.Button(root, text='Run Apps',font=("arial",10), padx=10, pady=5, command=runApp, bg="Gray23", fg="White")
    runApps.pack(padx=5, pady=5)

    deleteApps = tk.Button(root, text='Delete App',font=("arial",10), padx=10, pady=5, command=deleteApp, bg="Gray23", fg="White")
    deleteApps.pack(padx=5, pady=5)

    for app in apps:
        label = tk.Label(frame, text=os.path.basename(app), bg="Grey23", fg="White")
        label.pack()

    root.mainloop()

    if num==1:
        with open('work.txt', 'w') as f:
            for app in apps:
                f.write(app + ',')

    if num==2:
        with open('game.txt', 'w') as f:
            for app in apps:
                f.write(app + ',')

    if num==3:
        with open('other.txt', 'w') as f:
            for app in apps:
                f.write(app + ',')

welcome=tk.Label(main,text="Welcome to appProfiler",font=("arial",15),bg="Grey23",fg="White",padx=20,pady=20)
welcome.pack(padx=20,pady=20)

choose=tk.Label(main,text="Select from the given types of profiles:",font=("arial",10),bg="Grey15",fg="White")
choose.pack(padx=5,pady=5)

button1=tk.Button(main,text="WORK",command= lambda:appProfiler(1),font=("arial",10),bg="Grey23",fg="White",padx=15,pady=5)
button1.pack(padx=10,pady=10)

button2=tk.Button(main,text="GAME",command=lambda:appProfiler(2),font=("arial",10),bg="Grey23",fg="White",padx=15,pady=5)
button2.pack(padx=10,pady=10)

button3=tk.Button(main,text="OTHER",command=lambda:appProfiler(3),font=("arial",10),bg="Grey23",fg="White",padx=15,pady=5)
button3.pack(padx=10,pady=10)

main.mainloop()