from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import webbrowser


'''Menu Commands'''
def newFile():
    root.title("Untitled - Notepad")
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        textArea.delete(1.0, END)
        with open(file, "r") as f:
            textArea.insert(1.0, f.read())

def saveFile():
    global file
    if file == None:
        # Saveas if not saved before
        saveasFile()
    else:
        # Saving in the previously saved file
        with open(file, "w") as f:
            f.write(textArea.get(1.0, END))
            root.title(os.path.basename(file) + "- Notepad")


def saveasFile():
    global file
    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        # Saving as a new file
        with open(file, "w") as f:
            f.write(textArea.get(1.0, END))
            root.title(os.path.basename(file) + "- Notepad")

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    msg.showinfo(title="About Notepad", message="This is my first GUI application, A simple notepad. Use it and give feedbacks.")

def helpMe():
    openWeb = msg.askokcancel(title="Help", message="Open Help in web?")
    if openWeb:
        webbrowser.open("www.google.com")

def feedback():
    openWeb = msg.askokcancel(title="Feedback", message="Do you want to give feedback?")
    if openWeb:
        webbrowser.open("www.google.com")



'''Our main code'''
if __name__ == "__main__":

    '''Tkinter initialissation'''
    root = Tk()
    root.geometry("600x400")
    root.title("Untitled - Notepad")
    root.configure(bg="#3e3636")
    root.wm_iconbitmap("notepad.ico")


    '''Adding Menu'''
    main_menu = Menu(root)


    # file menu
    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label="New", command=newFile)
    file_menu.add_command(label="Open", command=openFile)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_command(label="Save As", command=saveasFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quitApp)

    main_menu.add_cascade(label="File", menu=file_menu)

    # edit menu
    edit_menu = Menu(main_menu, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)

    main_menu.add_cascade(label="Edit", menu=edit_menu)

    # help menu
    help_menu = Menu(main_menu, tearoff=0)
    help_menu.add_command(label="About My Notepad", command=about)
    help_menu.add_command(label="Help", command=helpMe)
    help_menu.add_command(label="Feedback", command=feedback)

    main_menu.add_cascade(label="Help", menu=help_menu)

    # Add menu in root
    root.config(menu=main_menu)


    '''Adding Scrollbar'''
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)


    '''Adding Text Area'''
    textArea = Text(root, yscrollcommand=scrollbar.set, bg="#1a1a1a", insertbackground="white", fg="white", font="Consolas 15")
    file = None
    textArea.pack(fill=BOTH, expand=True)


    '''Connecting scrollbar to text area'''
    scrollbar.config(command=textArea.yview)


    '''Syntax Highlighting'''
    # May be added later


    '''Infinite Loop'''
    root.mainloop()