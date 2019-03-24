#t
from tkinter import *
from tkinter import ttk
import tkinter
import pickle
import urllib
from urllib import request
from tkinter import messagebox
global box
global pacmanlist
pacmanlist = []
def create_widgets():
    global search_var
    search_var = StringVar()
    search_var.trace("w", update_list)
    entry = Entry(root, textvariable=search_var, width=13)
    entry.pack(side=BOTTOM)
    
    # Function for updating the list/doing the search.
    # It needs to be called here to populate the listbox.
    update_list()

def update_list(*args):
    search_term = search_var.get()

    # Just a generic list to populate the listbox

    box.delete(0, END)
    try:
        for item in pacmanlist:
                if search_term.lower() in item.lower():
                    box.insert(END, item)
    except:
        oof = 1
def reload():
    global pacmanlist
    try:
        dirfile = open("pacmandir.txt","rb")
        pacmanlist = pickle.load(dirfile)
        dirfile.close()
        box.delete(0,'end')
        for i in range(len(pacmanlist)):
            ladd = i + 1
            box.insert(ladd, pacmanlist[i])
    except:
        oof= 1
        
        

root = Tk()
root.title("WhirlPac")
try:
    dirfile = open("pacmandir.txt","rb")
    pacmanlist = pickle.load(dirfile)
    dirfile.close()
except:
    xboi = 1
top = Frame(root)
top.pack(side=TOP)
boxboi = Frame(root)

box = Listbox(boxboi)

try:
    for i in range(len(pacmanlist)):
        ladd = i + 1
        box.insert(ladd, pacmanlist[i])
except:
    xboi = 1
def install():
    try:
        sel = box.curselection()
        print(sel)
        sel = int(sel[0])
        idx = pacmanlist[sel]
        url = "http://replbox.repl.it/data/web_hosting_1/InventorX/Memebean/" + idx +".py"
        datadown = urllib.request.urlretrieve(url, filename=idx + ".py")
        messagebox.showinfo("Download","Download Complete")
    except:
        messagebox.showerror("Error","Error downloading pack. You are probably not connected to the internet")
def run():
    selruntu = box.curselection()
    selrunnum = int(selruntu[0])
    selrundata = pacmanlist[selrunnum]
    selrun = selrundata + ".py"
    try:
        exec(open(selrun).read())
    except:
        messagebox.showerror(title="Error", message = "File not found. Be sure it is downloaded")
def update():
    try:
        datadown = urllib.request.urlretrieve("http://replbox.repl.it/data/web_hosting_1/InventorX/Memebean/pacmandir.txt", "pacmandir.txt")
        reload()
    except:
        messagebox.showerror("Error","Error updateing WhirlPac. You are probably not connected to the internet")
def getinfo():
    try:
        sel = box.curselection()
        print(sel)
        sel = int(sel[0])
        print (sel)
        idx = pacmanlist[sel]
        print(idx)
        urli = "http://replbox.repl.it/data/web_hosting_1/InventorX/Memebean/" + idx +"info.txt"
        print(urli)
        datadown = urllib.request.urlretrieve(urli,"info.txt")
        file = open("info.txt","rb")
        infodata = pickle.load(file)
        messagebox.showinfo("Information",infodata)
    except:
        messagebox.showerror("Error","Error downloading info. You are probably not connected to the internet")

scrollbar = ttk.Scrollbar(boxboi)
scrollbar.pack(side=RIGHT,fill = Y)
scrollbar.config(command=box.yview)
go = ttk.Button(root, text ="Download", command=install)
go.pack(in_=top,side=LEFT)
upbut = ttk.Button(root, text="Update",command=update)
runbut = ttk.Button(root, text="Run", command=run)
runbut.pack(in_=top,side=LEFT)
upbut.pack(in_=top,side=LEFT)
box.config(yscrollcommand = scrollbar.set)
box.pack(in_=boxboi)
info = ttk.Button(root,text="Info",command=getinfo)
info.pack(in_=top,side=LEFT)
create_widgets()
boxboi.pack(side=BOTTOM)

root.mainloop()
