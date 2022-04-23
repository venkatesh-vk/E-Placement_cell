from tkinter import *
from tkinter import messagebox as m
import sqlite3 as sq

conn=sq.connect("DB/ld.sqlite")
c=conn.cursor()


root=Tk()
root.geometry("1200x850+242+47")
bgc="#0085fa"
fgc="white"
root.resizable(False,False)
root.title("Signup page")
root.config(bg=bgc)

def getdata(a,b=None):
    if b == None:
        c.execute(f"SELECT * FROM {a} WHERE rollnum = {idev}")
        d=c.fetchall()
        # print(d)
        # print(d[0])
        # print(d[0][0])
        # print(d[0][1])
        if d==[]:
            return 0
    else:
        c.execute(f"SELECT * FROM {a} WHERE id = {idev}")
        d=c.fetchall()
        # print(d)
        # print(a)
        if d==[]:
            c.execute(f"SELECT * FROM {b} WHERE id = {idev}")
            d=c.fetchall()
            # print(d)
            # print(b)
            if d==[]:
                return 0

    if d[0][0]==int(idev) and d[0][1]==psev:
        return d
    else:
        return 0
def login_check():
    global idev
    global psev
    idev=ide.get()
    psev=pse.get()
    if(idev=="" and psev==""):
            m.showerror("Error","Enter both ID and Password")
    else:        
        try:
            t=int(idev)
            # idev=str(idev)
        except:
            m.showerror("Error","Id must be an number")

        if len(idev)>=6:
            if (len(idev)>6):
                t=getdata("LPC","LF")
                if(t):
                    m.showinfo("Login sucessful","Click okay to view your dashboard")
                
                else:
                    m.showinfo("Alert","Your login details are not in the database check your credentials or contact the developer")
                    print("1")

            elif len(idev)==6:
                t=getdata("LST")
                if(t):
                    m.showinfo("Login sucessful","Welcome student click okay to continue")
                else:
                    print("2")
                    m.showinfo("Alert","Your login details are not in the database check your credentials or contact your adminsters")
        else:
            m.showwarning("Warning","Enter proper details")


wl=Label(root,fg=fgc,text="Welcome to E-Placement cell",font=("",35),bg=bgc)
wl.place(x=350,y=20)

idl=Label(root,fg=fgc,bg=bgc,text="ID",font=("Arial",20))
idl.place(x=400,y=250)

ide=Entry(root,width=25,font=("Arial",20))
ide.place(x=405,y=300)

pl=Label(root,fg=fgc,bg=bgc,text="Password",font=("Arial",20))
pl.place(x=400,y=350)

pse=Entry(root,show="*",width=25,font=("Arial",20))
pse.place(x=405,y=400)

fpb=Button(root,text="Forgot password",font=("Arial",15),bd=0,fg=fgc,bg=bgc)
fpb.place(x=402,y=450)

lb=Button(root,text="Login",font=("Arial",15),bd=0,fg=fgc,bg=bgc,command=login_check)
lb.place(x=725,y=450)

root.mainloop()