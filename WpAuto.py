from tkinter import *
import webbrowser
from plyer import notification
import pyautogui
import time
win=Tk()
win.resizable(False,False)
win.title("Wp Auto")
# Set the size of the window
win.geometry("500x690")

counter =1
# def insert(number):
# 		global counter
# 		if number!="":
# 				listbox.insert(counter,number)
# 				phoneNumber.delete(0,END)
# 				counter+=1
def clear():
	listbox.delete(0,END)


def sendMessage(listName,t):
	numOfMessages=1
	sendMsg=""
	msg= T.get(1.0, "end-1c")
	# for letter in msg:
	# 	if(letter==" "):
	# 		sendMsg+="%20"
	# 	else:
	# 		sendMsg+=letter
	with open(listName+".txt", "r") as file:
		for line in file.readlines():
			time.sleep(2)
			newMessage="https://wa.me/"+line.strip()
			webbrowser.open(newMessage, new=2)
			time.sleep(5)
			pyautogui.typewrite(msg)
			time.sleep(int(t))
			pyautogui.press('enter')
			L2.config(text = "Number Of Messages : "+str(numOfMessages))
			numOfMessages+=1
	# for i in range(0,listbox.size()):
	# 	time.sleep(2)
	# 	newMessage="https://wa.me/"+listbox.get(i)
	# 	webbrowser.open(newMessage, new=2)
	# 	time.sleep(5)
	# 	pyautogui.typewrite(msg)
	# 	time.sleep(5)
	# 	pyautogui.press('enter') 


Label(win,text="WP Auto").grid(row = 0, column = 0,columnspan = 3, padx = 5, pady = 5)
L1 = Label(win, text="Number List (txt file name) :")
E1 = Entry(win, bd =5)

L1.grid(row=1,column=0, sticky = W,padx=10,pady=10)
E1.grid(row=1,column=1, sticky = W,padx =10,pady=10,columnspan = 2)
L3 = Label(win, text="Time in second :")
E3 = Entry(win, bd =5)

L3.grid(row=2,column=0, sticky = W,padx=10,pady=10)
E3.grid(row=2,column=1, sticky = W,padx =10,pady=10,columnspan = 2)
# Label(win,text="Enter phon number here :").grid(row = 1, column = 0)
# phoneNumber =Entry(win,width=25 )
# phoneNumber.insert(0,"+94700000000")
# listbox = Listbox(win)  
T = Text(win, height = 20, width = 40)
T.insert(END,'Enter your message here')
T.grid(row=3,column=0,columnspan = 2,padx=50)
L2 = Label(win, text="Number Of Messages : 0")
L2.grid(row=4,column=0, sticky = W,padx=10,columnspan=3,pady=20)
# listbox.grid(row=3,column=0)
# c2 = Button(win, text ="Add Phon Number",width=23,pady=10, command =lambda: insert(phoneNumber.get()))
# c3 = Button(win, text ="Clear Number List",width=25,pady=10, command =lambda: clear())
send = Button(win, text ="Send This Message",width=65,pady=10, command =lambda: sendMessage(E1.get(),E3.get()))
# phoneNumber.grid(row = 1, column =1, sticky = W,columnspan=3)
L=Label(win,text="    D  e  v  e  l  o  p  e  d  B y       S  a  c  h  i  r  a      M  a  d  h  u  s  h  a  n      ",bg="aqua")
L.grid(row = 6, column = 0, sticky = W,columnspan=3)
# c2.grid(row = 2, column = 0, sticky = W)
# c3.grid(row = 2, column = 1, sticky = W)
send.grid(row = 5, column = 0, sticky = W,columnspan=3)
win.mainloop()