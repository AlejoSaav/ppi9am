from  tkinter import *
import time

def reloj():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,bg="black",fg="white",font="Arial 60 bold")
	clock.after(200,reloj)
	
root=Tk()
root.geometry("485x250")
root.title("Reloj")
clock=Label(root,font=("times",50,"bold"))

clock.grid(row=2,column=1,pady=25,padx=100)
reloj()

digi=Label(root,text=" Hora Actual",font="times 35 bold",fg="green")
digi.grid(row=0,column=1)

root.mainloop()