from tkinter import *
root=Tk()

count = -1


root.title("Image Viewer")
root.iconbitmap("C:/Users/Shiven Prakash/Desktop/PICS/Icon1.ico") #please enter your address in lines 8 to 13
image1=PhotoImage(file="C:/Users/Shiven Prakash/Desktop/PICS/index.png")
image2=PhotoImage(file="C:/Users/Shiven Prakash/Desktop/PICS/index2.png")
image3=PhotoImage(file="C:/Users/Shiven Prakash/Desktop/PICS/index3.png")
image4=PhotoImage(file="C:/Users/Shiven Prakash/Desktop/PICS/index4.png")
image5=PhotoImage(file="C:/Users/Shiven Prakash/Desktop/PICS/index5.png")

label1=Label(image=image1)
label2=Label(image=image2)
label3=Label(image=image3)
label4=Label(image=image4)
label5=Label(image=image5)	

status = Label(root,text="image 1 of 5")
status.grid(row=2,column=1)


def forward():
	global status
	global count
	count = count + 1
	label1.grid_forget()
	label2.grid_forget()
	label3.grid_forget()
	label4.grid_forget()
	label5.grid_forget()
	status.grid_forget()
	if count == 0:
		label1.grid(row=0,column=2) 
		status = Label(root,text="image 1 of 5")
		status.grid(row=2,column=2)

	if count == 1 :
		label2.grid(row=0,column=2)
		status = Label(root,text="image 2 of 5")
		status.grid(row=2,column=2)
	if count == 2:
		label3.grid(row=0,column=2)
		status = Label(root,text="image 3 of 5")
		status.grid(row=2,column=2)
	if count == 3:
		label4.grid(row=0,column=2)
		status = Label(root,text="image 4 of 5")
		status.grid(row=2,column=2)
	if count == 4:
		label5.grid(row=0,column=2)
		status = Label(root,text="image 5 of 5")
		status.grid(row=2,column=2)

def back():
	global status
	global count
	count = count -1
	label1.grid_forget()
	label2.grid_forget()
	label3.grid_forget()
	label4.grid_forget()
	label5.grid_forget()
	status.grid_forget()
	if count == 0:
		label1.grid(row=0,column=2) 
		status = Label(root,text="image 1 of 5")
		status.grid(row=2,column=2)

	if count == 1 :
		label2.grid(row=0,column=2)
		status = Label(root,text="image 2 of 5")
		status.grid(row=2,column=2)
	if count == 2:
		label3.grid(row=0,column=2)
		status = Label(root,text="image 3 of 5")
		status.grid(row=2,column=2)
	if count == 3:
		label4.grid(row=0,column=2)
		status = Label(root,text="image 4 of 5")
		status.grid(row=2,column=2)
	if count == 4:
		label5.grid(row=0,column=2)
		status = Label(root,text="image 5 of 5")
		status.grid(row=2,column=2)

bb=Button(root,text="Prev",padx=20,pady=16,command = back)
bb.grid(row=1,column=1)
be=Button(root,text="Quit",padx=20,pady=16,command=root.quit)
be.grid(row=1,column=2)
bf=Button(root,text="Next",padx=20,pady=16,command=forward)
bf.grid(row=1,column=3)

root.mainloop()