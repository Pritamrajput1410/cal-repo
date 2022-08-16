from argparse import SUPPRESS, Action
import tkinter as tk
from tkinter.ttk import Frame, Label,Entry,Button
from tkinter import StringVar
from turtle import onclick




num_label =(('1','2','3'),
            ('4','5','6'),
            ('7','8','9'),
            ('*','0','.'))

sign_label=('/',
            '-',
            '+',
            '=')
#main window
root = tk.Tk()
root.title('Calculater')
root.wm_attributes('-toolwindow',True)

text_var = StringVar()


# making function
express = ''
def putText(ch):
    global express
    express = express + str(ch)
    text_var.set(express)

def equalpress():
    global express
    try:
        result = str(eval(express)) 
        text_var.set(result)
    except:
        pass
    express = ''

def ACpress(): 
    global express
    express = '' 
    text_var.set('')

def CEpress(): 
    global express
    express = express[0:-1]
    text_var.set(express)
# creating main frame


main_frame = Frame(root)
main_frame.pack(fill = tk.BOTH,expand = True)

main_frame.columnconfigure(0,weight = 3)
main_frame.columnconfigure(0,weight=1)

#Entry Top


text_entry = Entry(main_frame,textvariable=text_var,font= 24)
text_entry.grid(row = 0,column = 0,columnspan = 2,sticky=tk.EW)



# creating button


num_frame = Frame(main_frame)
num_frame.grid(row =1,column = 0,)



#creating num button
btn1 = Button(num_frame,text = num_label[0][0],command = lambda: putText(1))
btn1.grid(row=0,column=0,ipadx=5,ipady=5)

btn2 = Button(num_frame,text = num_label[0][1],command = lambda: putText(2))
btn2.grid(row=0,column=1,ipadx=5,ipady=5)

btn3 = Button(num_frame,text = num_label[0][2],command = lambda: putText(3))
btn3.grid(row=0,column=2,ipadx=5,ipady=5)

btn4 = Button(num_frame,text = num_label[1][0],command = lambda: putText(4))
btn4.grid(row=1,column=0,ipadx=5,ipady=5)

btn5 = Button(num_frame,text = num_label[1][1],command = lambda: putText(5))
btn5.grid(row=1,column=1,ipadx=5,ipady=5)

btn6 = Button(num_frame,text = num_label[1][2],command = lambda: putText(6))
btn6.grid(row=1,column=2,ipadx=5,ipady=5)

btn7 = Button(num_frame,text = num_label[2][0],command = lambda: putText(7))
btn7.grid(row=2,column=0,ipadx=5,ipady=5)

btn8 = Button(num_frame,text = num_label[2][1],command = lambda: putText(8))
btn8.grid(row=2,column=1,ipadx=5,ipady=5)

btn9 = Button(num_frame,text = num_label[2][2],command = lambda: putText(9))
btn9.grid(row=2,column=2,ipadx=5,ipady=5)

btnstar = Button(num_frame,text = num_label[3][0],command = lambda: putText('*'))
btnstar.grid(row=3,column=0,ipadx=5,ipady=5)

btn0 = Button(num_frame,text = num_label[3][1],command = lambda: putText(0))
btn0.grid(row=3,column=1,ipadx=5,ipady=5)

btndot = Button(num_frame,text = num_label[3][2],command = lambda: putText('.'))
btndot.grid(row=3,column=2,ipadx=5,ipady=5)



#creating sign frame


sign_frame = Frame(main_frame)
sign_frame.grid(row = 1,column = 1)


#creating sign button
btndiv = Button(sign_frame,text=sign_label[0],command = lambda: putText('/'))
btndiv.grid(row=0,ipadx=5,ipady=5)

btnsub = Button(sign_frame,text=sign_label[1],command = lambda: putText('-'))
btnsub.grid(row=1,ipadx=5,ipady=5)

btnadd = Button(sign_frame,text=sign_label[2],command = lambda: putText('+'))
btnadd.grid(row=2,ipadx=5,ipady=5)

btnequal = Button(sign_frame,text=sign_label[3],command = lambda: equalpress())
btnequal.grid(row=3,ipadx=5,ipady=5)




#AC,CE button


ac_btn =Button(main_frame,text='AC',command = lambda: ACpress())
ac_btn.grid(row = 2 ,column = 0,sticky=tk.NSEW,ipadx=5,ipady=5)

ce_btn = Button(main_frame,text='CE',command = lambda: CEpress())
ce_btn.grid(row = 2 ,column = 1,ipadx=5,ipady=5)

# command= lambda:putText='AC'

root.mainloop()