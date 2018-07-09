from tkinter import *
import sqr
import os
os.system("cls")
class Calculator:
    fnt_entry=("Arial",30,"italic")
    fnt_button=("Arial",25,"italic")
    def __init__(self,root):
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)
        self.f=Frame(root,width=500,height=500,bg="#aed6f1")
        self.f.grid(row=0,column=0,sticky=N+S+E+W)
        self.e=Entry(self.f,justify=LEFT,font=Calculator.fnt_entry,bg="#111E6C",fg="white",bd=3,insertbackground="white",relief=FLAT,takefocus=0)
        self.e.grid(row=0,column=0,columnspan=5,sticky=N+S+W+E)
        self.e.bind_all("<KeyPress>",self.keyboard_press)
        
    #    self.e.focus_force()
        self.e.grab_release()
        self.button_gray()
        self.button_orange()
        self.row_column_configure()
    def button_gray(self):
        self.b_0=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="0",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("0"))
        self.b_1=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="1",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("1"))
        self.b_2=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="2",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("2"))
        self.b_3=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="3",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("3"))
        self.b_4=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="4",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("4"))
        self.b_5=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="5",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("5"))
        self.b_6=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="6",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("6"))
        self.b_7=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="7",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("7"))
        self.b_8=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="8",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("8"))
        self.b_9=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text="9",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("9"))
        self.b_dot=Button(self.f,font=Calculator.fnt_button,bg="#bdc3c7",text=".",fg="#343434",bd=1,relief=GROOVE,command=lambda :self.button_click("."))
        self.b_cancel=Button(self.f,font=Calculator.fnt_button,bg="#FF0800",text="C",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("Cancel"))
        self.b_0.grid(row=4,column=0,sticky=N+S+W+E)
        self.b_1.grid(row=3,column=0,sticky=N+S+W+E)
        self.b_2.grid(row=3,column=1,sticky=N+S+W+E)
        self.b_3.grid(row=3,column=2,sticky=N+S+W+E)
        self.b_4.grid(row=2,column=0,sticky=N+S+W+E)
        self.b_5.grid(row=2,column=1,sticky=N+S+W+E)
        self.b_6.grid(row=2,column=2,sticky=N+S+W+E)
        self.b_7.grid(row=1,column=0,sticky=N+S+W+E)
        self.b_8.grid(row=1,column=1,sticky=N+S+W+E)
        self.b_9.grid(row=1,column=2,sticky=N+S+W+E)
        self.b_dot.grid(row=4,column=1,sticky=N+S+W+E)
        self.b_cancel.grid(row=4,column=2,sticky=N+S+W+E)
    def button_orange(self):
        self.b_div=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="/",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("/"))
        self.b_mul=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="x",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("x"))
        self.b_min=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="-",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("-"))
        self.b_add=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="+",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("+"))
        self.b_result=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="=",fg="white",bd=1,relief=GROOVE,command=lambda :self.result())
        self.b_root=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="√",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("√"))
        self.b_pow=Button(self.f,font=Calculator.fnt_button,bg="#FC6600",text="^",fg="white",bd=1,relief=GROOVE,command=lambda :self.button_click("^"))
        self.b_div.grid(row=1,column=3,sticky=N+S+W+E)
        self.b_mul.grid(row=2,column=3,sticky=N+S+W+E)
        self.b_min.grid(row=3,column=3,sticky=N+S+W+E)
        self.b_add.grid(row=4,column=3,sticky=N+S+W+E)
        self.b_result.grid(row=3,column=4,rowspan=2,sticky=N+S+W+E)
        self.b_root.grid(row=1,column=4,sticky=N+S+W+E)
        self.b_pow.grid(row=2,column=4,sticky=N+S+W+E)
    def row_column_configure(self):
        self.f.rowconfigure(0,weight=1)
        self.f.rowconfigure(1,weight=1)
        self.f.rowconfigure(2,weight=1)
        self.f.rowconfigure(3,weight=1)
        self.f.rowconfigure(4,weight=1)
        self.f.columnconfigure(0,weight=1)
        self.f.columnconfigure(1,weight=1)
        self.f.columnconfigure(2,weight=1)
        self.f.columnconfigure(3,weight=1)
        self.f.columnconfigure(4,weight=1)
    def keyboard_press(self,event):        ###this is to handle the keyboard events
        self.check()
        if event.keysym=="0":
            self.e.insert(INSERT,"0")
        elif event.keysym=="1":
            self.e.insert(INSERT,"1")
        elif event.keysym=="2":
            self.e.insert(INSERT,"2")
        elif event.keysym=="3":
            self.e.insert(INSERT,"3")
        elif event.keysym=="4":
            self.e.insert(INSERT,"4")
        elif event.keysym=="5":
            self.e.insert(INSERT,"5")
        elif event.keysym=="6":
            self.e.insert(INSERT,"6")
        elif event.keysym=="7":
            self.e.insert(INSERT,"7")
        elif event.keysym=="8":
            self.e.insert(INSERT,"8")
        elif event.keysym=="9":
            self.e.insert(INSERT,"9")
        elif event.keysym=="period":
            self.e.insert(INSERT,".")
        elif event.keysym=="Return":
            self.result()
        elif event.keysym=="BackSpace":
            self.e.delete((len(self.e.get())-1),END)
        elif event.keysym=="asciicircum":
            self.e.insert(INSERT,"^")
        elif event.keysym=="asterisk":
            self.e.insert(INSERT,"x")
        elif event.keysym=="plus":
            self.e.insert(INSERT,"+")
        elif event.keysym=="minus":
            self.e.insert(INSERT,"-")
        elif event.keysym=="slash":
            self.e.insert(INSERT,"/")

    def button_click(self,num):   ###this is to handle button clicking on the buttons
        self.check()
        if num=="0":
            self.e.insert(INSERT,"0")
        elif num=="1":
            self.e.insert(INSERT,"1")
        elif num=="2":
            self.e.insert(INSERT,"2")
        elif num=="3":
            self.e.insert(INSERT,"3")
        elif num=="4":
            self.e.insert(INSERT,"4")
        elif num=="5":
            self.e.insert(INSERT,"5")
        elif num=="6":
            self.e.insert(INSERT,"6")
        elif num=="7":
            self.e.insert(INSERT,"7")
        elif num=="8":
            self.e.insert(INSERT,"8")
        elif num=="9":
            self.e.insert(INSERT,"9")
        elif num==".":
            self.e.insert(INSERT,".")
        elif num=="Cancel":
            self.e.delete(0,END)
        elif num=="^":
            self.e.insert(INSERT,"^")
        elif num=="√":
            self.e.insert(INSERT,"√")
        elif num=="x":
            self.e.insert(INSERT,"x")
        elif num=="+":
            self.e.insert(INSERT,"+")
        elif num=="-":
            self.e.insert(INSERT,"-")
        elif num=="/":
            self.e.insert(INSERT,"/")
    def result(self):
        if self.check():
            pass
        else:
            stri=self.e.get()
            try:
                stri=sqr.solve(stri)
                stri=stri.replace("x","*")
                stri=stri.replace("^","**")
                self.e.delete(0,END)
                res=str(float(eval(stri)))
                if len(res)>20:
                    res="%.6e"%(float(res))
                self.e.insert(INSERT,res)
            except (SyntaxError,ValueError):
                self.e.delete(0,END)
                self.e.insert(INSERT,str("Syntax Error"))
            except ArithmeticError:
                self.e.delete(0,END)
                self.e.insert(INSERT,str("Math Error"))
    def check(self):
        stri=self.e.get()
        if stri=="Syntax Error" or stri=="Math Error":
            self.e.delete(0,END)
            return 1
        else:
            return 0
root=Tk()
root.resizable(width=True,height=True)
root.title("Calculator")
root.geometry("500x500+100+100")
#root.wm_iconbitmap("logo1.ico")
obj=Calculator(root)
root.mainloop()
