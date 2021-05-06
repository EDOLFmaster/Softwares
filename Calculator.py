from tkinter import *

root=Tk()
Enter=Entry(root,width=26)
Enter.grid(row=5,column=1,columnspan=3)

def bc(num):
	current = Enter.get()
	Enter.delete(0,END)
	Enter.insert(0,current + num)

def Add():
	global FirstNumInt
	global operator
	FirstNum = Enter.get()
	FirstNumInt = int(FirstNum)
	Enter.delete(0,END)
	operator = "plus"

def Subtract():
	global FirstNumInt
	global operator
	FirstNum = Enter.get()
	FirstNumInt = int(FirstNum)
	Enter.delete(0,END)
	operator = "minus"

def Multiply():
	global FirstNumInt
	global operator
	FirstNum = Enter.get()
	FirstNumInt = int(FirstNum)
	Enter.delete(0,END)
	operator = "into"

def Divide():
	global FirstNumInt
	global operator
	FirstNum = Enter.get()
	FirstNumInt = int(FirstNum)
	Enter.delete(0,END)
	operator = "div"

def Square():
	global FirstNumInt
	FirstNum = Enter.get()
	FirstNumInt = int(FirstNum)
	Enter.delete(0,END)
	Enter.insert(0,FirstNumInt ** 2)

def Answer():
	SecondNum = Enter.get()
	Enter.delete(0,END)
	SecondNumInt = int(SecondNum)
	
	if operator == "plus":
		FinalAnswer = FirstNumInt + SecondNumInt
		Enter.insert(0,FinalAnswer)
	
	elif operator == "minus":
		FinalAnswer = FirstNumInt - SecondNumInt
		Enter.insert(0,FinalAnswer)
	
	elif operator == "into":
		FinalAnswer = FirstNumInt * SecondNumInt
		Enter.insert(0,FinalAnswer)
	
	elif operator == "div":
		FinalAnswer = FirstNumInt / SecondNumInt
		Enter.insert(0,FinalAnswer)

Button1=Button(root,text="1",padx=20,pady=20,command=lambda: bc("1"))
Button1.grid(row=1,column=1,)

Button2=Button(root,text="2",padx=20,pady=20,command=lambda: bc("2"))
Button2.grid(row=1,column=2)

Button3=Button(root,text="3",padx=20,pady=20,command=lambda: bc("3"))
Button3.grid(row=1,column=3)

Button4=Button(root,text="4",padx=20,pady=20,command=lambda: bc("4"))
Button4.grid(row=1,column=4)

Button5=Button(root,text="5",padx=20,pady=20,command=lambda: bc("5"))
Button5.grid(row=2,column=1)

Button6=Button(root,text="6",padx=20,pady=20,command=lambda: bc("6"))
Button6.grid(row=2,column=2)

Button7=Button(root,text="7",padx=20,pady=20,command=lambda: bc("7"))
Button7.grid(row=2,column=3)

Button8=Button(root,text="8",padx=20,pady=20,command=lambda: bc("8"))
Button8.grid(row=2,column=4)

Button9=Button(root,text="9",padx=20,pady=20,command=lambda: bc("9"))
Button9.grid(row=3,column=1)

Button0=Button(root,text="0",padx=20,pady=20,command=lambda: bc("0"))
Button0.grid(row=3,column=2)

ButtonA=Button(root,text="+",padx=20,pady=20,command=Add)
ButtonA.grid(row=3,column=3)

ButtonS=Button(root,text="-",padx=20,pady=20,command=Subtract)
ButtonS.grid(row=3,column=4)

ButtonC=Button(root,text="C",padx=20,pady=20,command=lambda:Enter.delete(0,END))
ButtonC.grid(row=4,column=1)

ButtonM=Button(root,text="x",padx=20,pady=20,command=Multiply)
ButtonM.grid(row=4,column=2)

ButtonD=Button(root,text="÷",padx=20,pady=20,command=Divide)
ButtonD.grid(row=4,column=3)

ButtonE=Button(root,text="=",padx=20,pady=20,command=Answer)
ButtonE.grid(row=5,column=4)

ButtonSq = Button(root,text="Sq",padx=16,pady=20,command=Square)
ButtonSq.grid(row=4,column=4)
root.mainloop()