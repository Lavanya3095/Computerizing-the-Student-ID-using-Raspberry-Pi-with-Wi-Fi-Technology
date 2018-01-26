#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import math
import httplib2
import urllib
import flask
import json
from tkinter import *
from PIL import Image, ImageTk
LARGE_FONT = ('Verdana', 12)


##def onLeftDrag(event):
##    a = PageNav();
##    controller.show_frame(HomePage);


class PageNav(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # Insert all the frames here as class files

        for F in (
            Display,
            HomePage,
            Student,
            Leave,
            OnDuty,
            OutPass,
            Attendance,
            Calculator,
            ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(Display)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    

class Display(tk.Frame):
   
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        make_frame = LabelFrame(self, text="", width=100, height=100)
        #make_frame.bind("<Button-1>", onLeftDrag)
        make_frame.pack()
        # create the PIL image object:
        PIL_image = Image.open("Images\logoname.png")

        width = 1400
        height = 180

        # You may prefer to use Image.thumbnail instead
        # Set use_resize to False to use Image.thumbnail
        use_resize = True

        if use_resize:
            # Image.resize returns a new PIL.Image of the specified size
            PIL_image_small = PIL_image.resize((width,height), Image.ANTIALIAS)
        else:
            # Image.thumbnail converts the image to a thumbnail, in place
            PIL_image_small = PIL_image
            PIL_image_small.thumbnail((width,height), Image.ANTIALIAS)

        # now create the ImageTk PhotoImage:
        img = ImageTk.PhotoImage(PIL_image_small)
        in_frame = Label(make_frame, image = img)
        #in_frame.bind("<Button-1>", onLeftDrag)
        in_frame.image= img
        in_frame.place(x=0, y=0)
        in_frame.pack(expand=YES, fill=X)
        


        make_frame1 = LabelFrame(self, text="", width=140, height=160)
        #make_frame1.bind("<Button-1>", onLeftDrag)
        make_frame1.pack(side=LEFT)


        # create the PIL image object:
        PIL_image1 = Image.open("Images\depika.jpg")

        width = 400
        height = 600

        # You may prefer to use Image.thumbnail instead
        # Set use_resize to False to use Image.thumbnail
        use_resize = True

        if use_resize:
            # Image.resize returns a new PIL.Image of the specified size
            PIL_image_small1 = PIL_image1.resize((width,height), Image.ANTIALIAS)
        else:
            # Image.thumbnail converts the image to a thumbnail, in place
            PIL_image_small1 = PIL_image1
            PIL_image_small1.thumbnail((width,height), Image.ANTIALIAS)

        # now create the ImageTk PhotoImage:
        img1 = ImageTk.PhotoImage(PIL_image_small1)
        in_frame1 = Label(make_frame1, image = img1)
        #in_frame1.bind("<Button-1>", onLeftDrag)
        in_frame1.image= img1
        in_frame1.place(x=0, y=0)
        in_frame1.pack(side=LEFT, expand=YES, fill=BOTH)

        make_frame2 = LabelFrame(self, text="", width=200, height=160, background= 'light grey')
       
        #make_frame2.bind("<Button-1>", onLeftDrag)
        make_frame2.pack(side=BOTTOM)
        var = StringVar()
        label = Label( self, textvariable=var, width=500, height=300)
        #label.bind("<Button-1>", onLeftDrag)
        label.config(font=("Lucida Bright", 40))
        label.pack(side=LEFT)
        in_frame2 = Label(make_frame2, text = var.set("NAME :  R.M.DEPIKA \nDEPT  :  CSE \nDURATION  :  2013-2017\nROLL NO :  13CS009"), fg = 'light blue')
        in_frame2.configure(bg='light blue')
        buttonHome = tk.Button(make_frame2, text='Menu',
                               command=lambda : \
                               controller.show_frame(HomePage), anchor = "s")
        buttonHome.pack(side = 'bottom', expand = True)
        buttonHome.config(font=("Lucida Bright", 25))
        #in_frame2.bind("<Button-1>", onLeftDrag)
        in_frame2.pack(side=LEFT)
                     
        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        label = tk.Label(self, text='Start Page', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10)
        button_label = [
            'Student Details',
            'Leave Application',
            'On-Duty Application',
            'Out Pass',
            'Attendance',
            'Calculator',
            ]

        button1 = tk.Button(self, text=button_label[0],
                            command=lambda : \
                                controller.show_frame(Student), width=65, height=2, anchor = "center", bg = '#ffcccc')
        button1.config(font=("Lucida Bright", 25))
        button1.pack()

        button2 = tk.Button(self, text=button_label[1],
                            command=lambda : \
                            controller.show_frame(Leave), width=65, height=2, anchor = "center", bg = '#ff8533')
        button2.config(font=("Lucida Bright", 25))
        button2.pack()

        button3 = tk.Button(self, text=button_label[2],
                            command=lambda : \
                            controller.show_frame(OnDuty), width=65, height=2, anchor = "center", bg = '#e6b3ff')
        button3.config(font=("Lucida Bright", 25))
        button3.pack()

        button4 = tk.Button(self, text=button_label[3],
                            command=lambda : \
                            controller.show_frame(OutPass), width=65, height=2, anchor = "center", bg = '#ffd9b3')
        button4.config(font=("Lucida Bright", 25))
        button4.pack()

        button5 = tk.Button(self, text=button_label[4],
                            command=lambda : \
                            controller.show_frame(Attendance), width=65, height=2, anchor = "center", bg = '#88cc00')
        button5.config(font=("Lucida Bright", 25))
        button5.pack()

        button6 = tk.Button(self, text=button_label[5],
                            command=lambda : \
                            controller.show_frame(Calculator), width=65, height=2, anchor = "center", bg = '#e6e600')
        button6.config(font=("Lucida Bright", 25))
        button6.pack()
        buttonHome = tk.Button(self, text='Back to Home',
                           command=lambda : \
                           controller.show_frame(Display))
        buttonHome.pack()
        buttonHome.config(font=("Lucida Bright", 25))


class Student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        label = tk.Label(self, text='Student Details', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10)
        def stud_rec():
            http = httplib2.Http()
            body = {'name': 'Depika Murali', 'regno': '31113104019'}
            content = http.request("http://192.168.3.70/getAllCustomers.php", 
                      method="POST", 
                      headers={'Content-type': 'application/x-www-form-urlencoded'},
                      body=urllib.parse.urlencode(body) )[1]
            str = (content.decode())
            return str
                  
        stri = stud_rec()
        data = json.loads(stri)
        strin = data[0]
        fname = strin['Sfname']
        dob = strin['Sdob']
        bldgp = strin['Sbldgp']
        cont = strin['Scont']
        addr = strin['Saddr']
        auto = fname, dob, bldgp, cont, addr
        fields = 'Father name', 'Date of birth', 'Blood group', 'Contact no', 'Res Addresss'
        for index in range(len(fields)):
                  row = Frame(self)
                  lab = Label(row, width=15, text=fields[index], anchor='w', padx=10, pady=10)
                  lab.config(font=("Lucida Bright", 25), bg = 'light blue')
                  lab.place(x = 20, y = 250)
                  if(index< 5):
                      ent = Entry(row)
                      ent.insert(30, auto[index])
                      ent.configure(state = 'readonly')
                  else:
                      ent = Entry(row)
                  row.pack(side=TOP, fill=X, padx=5, pady=5)
                  lab.pack(side=LEFT)
                  ent.pack(side=RIGHT, expand=YES, fill = X, ipadx=20, ipady=20)
                  ent.config(font=("Lucida Bright", 10))
        buttonHome = tk.Button(self, text='Back to Home',
                               command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side = 'right', expand = True)
        buttonHome.config(font=("Lucida Bright", 25))
                    
               
class Leave(tk.Frame):
            
    def fetch(entries):
        arr = []
        for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              arr.append(text)         
        name = (arr[0])
        regno = (arr[1])
        date = arr[5]
        days = arr[6]
        reason = arr[7]
        http = httplib2.Http()
        body = {'name': name, 'regno': '31113104019', 'date': date, 'days': days, 'reason': reason}

        content = http.request("http://192.168.3.70/leave_apply.php", 
                  method="POST", 
                  headers={'Content-type': 'application/x-www-form-urlencoded'},
                  body=urllib.parse.urlencode(body) )[1]
        print(content.decode())
        #flash(content.decode())
        
          

    #def on_button(temp):
            
                  
    def makeform(self, fields):
        stri = Leave.stud_rec()
        data = json.loads(stri)
        strin = data[0]
        name = strin['Sname']
        regno = strin['Sregno']
        dept = strin['Sdept']
        batch = strin['Sbatch']
        cont = strin['Scont']
        entries = []
        auto = name, regno,dept, batch, cont
        
        for index in range(len(fields)):
                  row = Frame(self)
                  lab = Label(row, width=15, text=fields[index], anchor='w', padx=10, pady=10)
                  lab.config(font=("Lucida Bright", 25), bg = 'light blue')
                  lab.place(x = 20, y = 250)
                  if(index< 5):
                      ent = Entry(row)
                      ent.insert(20, auto[index])
                      entries.append((index, ent))
                      #temp_list.append(ent.get())
                      ent.configure(state = 'readonly')
                      
                  else:
                      ent = Entry(row)
                      entries.append((index, ent))
                      #temp_list.append(ent.get())
                  row.pack(side=TOP, fill=X, padx=5, pady=5)
                  #row.bind('<Return>', (lambda event, e=ents: fetch(e)))
                  lab.pack(side=LEFT)
                  ent.pack(side=RIGHT, expand=YES, fill = X, ipadx=20, ipady=20)
                  ent.config(font=("Lucida Bright", 10))
        return entries
    
    def stud_rec():
            http = httplib2.Http()
            body = {'name': 'Depika Murali', 'regno': '31113104019'}
            content = http.request("http://192.168.3.70/getAllCustomers.php", 
                      method="POST", 
                      headers={'Content-type': 'application/x-www-form-urlencoded'},
                      body=urllib.parse.urlencode(body) )[1]
            str = (content.decode())
            return str
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        temp_list = []
        label = tk.Label(self, text='Leave Application', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10)
        
        
                   
        
        #buttonSubmit = tk.Button(self, text='Submit',
                                 #command = lambda : \
                                 #Leave.on_button(temp_list), anchor = "center")
        fields = 'Name', 'Reg', 'Dept', 'Batch', 'Contact no','Date of leave', 'No of days', 'Reason'
        ents = Leave.makeform(self, fields)
        
        self.bind('<Return>', (lambda event, e=ents: fetch(e)))   
        buttonSubmit = tk.Button(self, text='submit',
                                 command=(lambda e=ents: Leave.fetch(e)))
        buttonSubmit.pack(side = 'left', expand = True)
        buttonSubmit.config(font=("Lucida Bright", 25))
        buttonHome = tk.Button(self, text='Back to Home',
                               command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side = 'right', expand = True)
        buttonHome.config(font=("Lucida Bright", 25))
    
        
class OnDuty(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        label = tk.Label(self, text='On Duty Application', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10)
        def stud_rec():
            http = httplib2.Http()
            body = {'name': 'Depika Murali', 'regno': '31113104019'}
            content = http.request("http://192.168.3.70/getAllCustomers.php", 
                      method="POST", 
                      headers={'Content-type': 'application/x-www-form-urlencoded'},
                      body=urllib.parse.urlencode(body) )[1]
            str = (content.decode())
            return str
                  
        stri = stud_rec()
        data = json.loads(stri)
        strin = data[0]
        name = strin['Sname']
        regno = strin['Sregno']
        dept = strin['Sdept']
        batch = strin['Sbatch']
        cont = strin['Scont']
        auto = name, regno,dept, batch, cont
        fields = 'Name', 'Reg', 'Dept', 'Batch','Contact no','Hours','Name of the event'
        for index in range(len(fields)):
                  row = Frame(self)
                  lab = Label(row, width=15, text=fields[index], anchor='w', padx=10, pady=10)
                  lab.config(font=("Lucida Bright", 25), bg = 'light blue')
                  lab.place(x = 20, y = 250)
                  if(index< 5):
                      ent = Entry(row)
                      ent.insert(20, auto[index])
                      ent.configure(state = 'readonly')
                  else:
                      ent = Entry(row)
                  row.pack(side=TOP, fill=X, padx=5, pady=5)
                  lab.pack(side=LEFT)
                  ent.pack(side=RIGHT, expand=YES, fill=X, ipadx=20, ipady=20)
                  ent.config(font=("Lucida Bright", 10))
        buttonSubmit = tk.Button(self, text='Submit', anchor = "center")
        buttonSubmit.pack(side = 'left', expand = True)
        buttonSubmit.config(font=("Lucida Bright", 25))
        buttonHome = tk.Button(self, text='Back to Home',
                               command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side = 'right', expand = True)
        buttonHome.config(font=("Lucida Bright", 25))


class OutPass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        label = tk.Label(self, text='Out Pass', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10)
        def stud_rec():
            http = httplib2.Http()
            body = {'name': 'Depika Murali', 'regno': '31113104019'}
            content = http.request("http://192.168.3.70/getAllCustomers.php", 
                      method="POST", 
                      headers={'Content-type': 'application/x-www-form-urlencoded'},
                      body=urllib.parse.urlencode(body) )[1]
            str = (content.decode())
            return str
                  
        stri = stud_rec()
        data = json.loads(stri)
        strin = data[0]
        name = strin['Sname']
        regno = strin['Sregno']
        dept = strin['Sdept']
        batch = strin['Sbatch']
        cont = strin['Scont']
        auto = name, regno,dept, batch, cont
        fields = 'Name', 'Reg no', 'Dept', 'Batch','Contact no', 'Reason For Leaving', 'Time Of Leaving', 'Time Of Returning'
        for index in range(len(fields)):
                  row = Frame(self)
                  lab = Label(row, width=15, text=fields[index], anchor='w', padx=10, pady=10)
                  lab.config(font=("Lucida Bright", 25), bg = 'light blue')
                  lab.place(x = 20, y = 250)
                  if(index< 5
                     ):
                      ent = Entry(row)
                      ent.insert(20, auto[index])
                      ent.configure(state = 'readonly')
                  else:
                      ent = Entry(row)
                  row.pack(side=TOP, fill=X, padx=5, pady=5)
                  lab.pack(side=LEFT)
                  ent.pack(side=RIGHT, expand=YES, fill=X, ipadx=20, ipady=20)
                  ent.config(font=("Lucida Bright", 10))
        buttonSubmit = tk.Button(self, text='Submit', anchor = "center")
        buttonSubmit.pack(side = 'left', expand = True)
        buttonSubmit.config(font=("Lucida Bright", 25))
        buttonHome = tk.Button(self, text='Back to Home',
                               command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side = 'right', expand = True)
        buttonHome.config(font=("Lucida Bright", 25))


class Attendance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        label = tk.Label(self, text='Attendance', font=LARGE_FONT, bg = 'light blue')
        label.config(font=("Lucida Bright", 25))
        label.pack(pady=10, padx=10)
        #left frame
        col1 = Frame(self)
        label = tk.Label(col1, text='Enter Code', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10, side=TOP)
        label.config(font = ("Lucida Bright", 35))
        ent = Entry(col1)
        #ent.pack(side=TOP)
        ent.pack(side=TOP, expand=YES, fill=X, ipadx=20, ipady=20)
        ent.config(font=("Lucida Bright", 15))
        submit = tk.Button(col1, text='Submit')
        submit.pack(side=TOP)
        submit.config(font=("Lucida Bright", 35))
        col1.config(bg = 'light blue')
        col1.pack(side=LEFT)
        #right frame
        col2 = Frame(self)
        label = tk.Label(col2, text='Percentage', font=LARGE_FONT, bg = 'light blue')
        label.pack(pady=10, padx=10, side=TOP)
        label.config(font = ("Lucida Bright", 35))
        ent1 = Entry(col2)
        ent1.config(font=("Lucida Bright", 15))
        ent1.pack(side=TOP, expand = YES, fill=X, ipadx=20, ipady=20)
        checkPercent = tk.Button(col2, text='Check')
        checkPercent.pack(side=TOP)
        checkPercent.config(font=("Lucida Bright", 35))
        col2.config(bg = 'light blue')
        col2.pack(side=RIGHT)
        #back to home button
        buttonHome = tk.Button(self, text='Back to Home', command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side=BOTTOM)
        buttonHome.config(font=("Lucida Bright", 35))


class Calculator(tk.Frame):
     def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        label = tk.Label(self, text='Calculator', font=LARGE_FONT, bg = 'light blue')
        label.config(font=("Lucida Bright", 25))
        label.pack(pady=10, padx=10)
        insideFrame = Frame(self)
        insideFrame.pack(side=TOP)
        insideFrame.configure(bg = 'light blue')
        text_box = Entry(insideFrame, justify=RIGHT,width=30,font="Times 16 bold")
        text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
        text_box.insert(0, "0")

        numbers = "789456123"
        i = 0
        bttn = []
        for j in range(1,4):
            for k in range(3):
                bttn.append(Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
                bttn[i]["bg"]= "orange"
                bttn[i].grid(row = j, column = k,padx=1,pady=1)
                bttn[i]["command"] = lambda x = numbers[i]: num_press(self,x)
                i += 1
        bttn_0 = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange")
        bttn_0["command"] = lambda: num_press(self,0)
        bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)
        div = Button(insideFrame ,height =2,width=4,padx=10, pady = 10, text = "/",bg="steel blue")
        div["command"] = lambda: operation(self, "divide")
        div.grid(row = 1, column = 3, padx=1, pady = 1)

        mult = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "*",bg="steel blue")
        mult["command"] = lambda: operation(self, "times")
        mult.grid(row = 2, column = 3,  padx=1, pady = 1)

        minus = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "-",bg="steel blue")
        minus["command"] = lambda: operation(self, "minus")
        minus.grid(row = 3, column = 3, padx=1, pady = 1)

        add = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "+",bg="steel blue")
        add["command"] = lambda: operation(self, "add")
        add.grid(row = 4, column = 3,  padx=1, pady = 1)

        power = Button(insideFrame, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
        power["command"] = lambda: operation(self, "raise")
        power.grid(row=2,column = 4,padx=1,pady=1)

        rootof = Button(insideFrame, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
        rootof["command"] = lambda: operation(self, "rootof")
        rootof.grid(row=2, column=5, padx=1, pady=1)

        fact = Button(insideFrame, height=2, width=4, padx=10, pady=10, text="!",bg="green")
        fact["command"] = lambda: operation(self, "fact")
        fact.grid(row=3,column=4, padx=1, pady=1)

        loge = Button(insideFrame, height=2, width=4, padx=10, pady=10, text="ln",bg="green")
        loge["command"] = lambda: operation(self, "ln")
        loge.grid(row=3, column=5, padx=1, pady=1)

        log10 = Button(insideFrame, height=2, width=4, padx=10, pady=10, text="log",bg="green")
        log10["command"]= lambda: operation(self, "log")
        log10.grid(row=4, column=4, padx=1 , pady=1)

        sine = Button(insideFrame, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green")
        sine["command"]=lambda: operation(self, "sine")
        sine.grid(row=5,column=0,padx=1,pady=1)

        cosine = Button(insideFrame, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green")
        cosine["command"]=lambda: operation(self, "cosine")
        cosine.grid(row=5,column=1,padx=1,pady=1)

        tangent = Button(insideFrame, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green")
        tangent["command"]=lambda: operation(self, "tangent")
        tangent.grid(row=5,column=2,padx=1,pady=1)

        exponent = Button(insideFrame, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
        exponent["command"]=lambda: operation(self, "exp")
        exponent.grid(row=5,column=3,padx=1,pady=1)

        inv = Button(insideFrame, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
        inv["command"] = lambda: operation(self, "inv")
        inv.grid(row=5,column=4,padx=1,pady=1)

        point = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
        point["command"] = lambda: num_press(self, ".")
        point.grid(row = 4, column = 1, padx=1, pady = 1)

        neg= Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
        neg["command"] = lambda: sign(self)
        neg.grid(row = 4, column = 2,  padx=1, pady = 1)


        clear = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
        clear["command"] = lambda: clear(self)
        clear.grid(row = 1, column = 4,  padx=1, pady = 1)

        all_clear = Button(insideFrame,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
        all_clear["command"] = lambda: all_clear(self)
        all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

        equals = Button(insideFrame,height =6,width=4,padx=10, pady = 10, text = "=",bg="green")
        equals["command"] = lambda: calc_total(self)
        equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)


        buttonHome = tk.Button(self, text='Back to Home', command=lambda : \
                               controller.show_frame(HomePage), anchor = "center")
        buttonHome.pack(side=BOTTOM)
        buttonHome.config(font=("Lucida Bright", 35))

        def num_press(self, num):
            self.eq = False
            temp = text_box.get()
            temp2 = str(num)
            if self.new_num:
                self.current = temp2
                self.new_num = False
            else:
                if temp2 == '.':
                    if temp2 in temp:
                        return
                self.current = temp + temp2
            display(self,self.current)

        def display(self, value):
            text_box.delete(0, END)
            text_box.insert(0, value)

        def calc_total(self):
            self.eq = True
            self.current = float(self.current)
            if self.op_pending == True:
                do_sum(self)
            else:
                self.total = float(text_box.get())

        def do_sum(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "minus":
                self.total -= self.current
            if self.op == "times":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "raise":
                self.total = self.total ** self.current
            if self.op == "rootof":
                self.total = self.total ** (1/self.current)
            if self.op == "fact":
                self.total=int(text_box.get())
                self.total=math.factorial(self.total)
            if self.op == "ln":
                self.total = log(self.total)
            if self.op == "log":
                self.total=log(self.total,10)
            if self.op == "sine":
                self.total=math.sin(self.total)
            if self.op == "cosine":
                self.total = math.cos(self.total)
            if self.op == "tangent":
                self.total = math.tan(self.total)
            if self.op == "exp":
                self.total = math.exp(self.total)
            if self.op == "inv":
                self.total = 1/self.total
            self.new_num = True
            self.op_pending = False
            display(self, self.total)

        def operation(self, op):
            self.current = float(self.current)
            if self.op_pending:
                do_sum(self)
            elif not self.eq:
                self.total = self.current
            self.new_num = True
            self.op_pending = True
            self.op = op
            self.eq = False

        def clear(self):
            self.eq = False
            self.current = "0"
            display(self, 0)
            self.new_num = True

        def all_clear(self):
            clear(self)
            self.total = 0

        def sign(self):
            self.eq = False
            self.current = -(float(text_box.get()))
            display(self, self.current)


if __name__ == '__main__':
    app = PageNav()
    app.mainloop()


            
