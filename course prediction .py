from tkinter import *
from tkinter.ttk import Combobox

master=Tk()
master.title("Course prediction")
def no():
    master.destroy()
def see_pass():
    global a
    pass_screen=Toplevel(master)
    pass_screen.title("Course prediction")

    Label(pass_screen,text="These are the courses",font=("Rosewood Std Regular",14)).grid(row=0,sticky=N,pady=10)
            

    area=Text(pass_screen,height=6,width=50,font=("Rosewood Std Regular",10))
    area.grid(row=2,sticky=N,pady=10,padx=10)
    area.delete("1.0","end")
    with open(a,"r") as J:
        for l in J:
            area.insert("1.0",l+"\n")
            

    Button(pass_screen,text="Exit", font=("Rosewood Std Regular",12),width=20,command=no).grid(row=5,sticky=N,pady=10)
    
def fin_yes():
    global course
    global c
    global a
    c1=course.get()
    if c1=="-Select Course-":
        notif.config(fg="red",text="Please select the course")
        return
    else:
        if(c1==c[0]):
            a="0.txt"
        elif(c1==c[1]):
            a="1.txt"
        elif(c1==c[2]):
            a="2.txt"
        elif(c1==c[3]):
            a="3.txt"
        elif(c1==c[4]):
            a="4.txt"
        elif(c1==c[5]):
            a="5.txt"
        elif(c1==c[6]):
            a="6.txt"
        elif(c1==c[7]):
            a="7.txt"
        else:
            pass
            
    Button(gen_screen,text="See course",font=("Rosewood Std Regular",12),width=20,command=see_pass).grid(row=4,sticky=N,pady=10)
    notif.config(text="")
    return

def yes():
    global temp_length
    global notif
    global gen_screen
    global course
    global c
    temp_length= StringVar()

    gen_screen=Toplevel(master)
    gen_screen.title("Course prediction")

    Label(gen_screen,text="Choose your domain",font=("Rosewood Std Regular",16)).grid(row=0,sticky=N,pady=10)
    notif=Label(gen_screen, font=("Rosewood Std Regular",12))
    notif.grid(row=4,sticky=N,pady=10)
    
    c=["Web development","Cyber security","AIML","Cloud Computing","Web development(paid)","Cyber security(paid)","AIML(paid)","Cloud Computing(paid)"]
    course=Combobox(gen_screen,values=c,font="Calibri",width=35,state="r")
    course.grid(row=2,stick=N,pady=10)
    course.set("-Select Course-")
   

    Button(gen_screen,text="Enter",font=("Rosewood Std Regular",12),width=20,command=fin_yes).grid(row=3,sticky=N,pady=10)
    

Label(master,text="Course Prediction",font=("Rosewood Std Regular",16)).grid(row=0,sticky=N,pady=10)
Label(master,text="Would you like to see prefered courses",font=("Rosewood Std Regular",13)).grid(row=1,sticky=N,pady=10)

Button(master,text="Yes", font=("Rosewood Std Regular",12),width=20,command=yes).grid(row=2,sticky=N,pady=10)
Button(master,text="No", font=("Rosewood Std Regular",12),width=20,command=no).grid(row=3,sticky=N)
master.mainloop()
