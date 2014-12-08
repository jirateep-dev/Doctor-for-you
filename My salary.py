from Tkinter import *
import tkMessageBox
class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x200+600+300")
        self.root.wm_title("My salary")
        

       # self.entryuser = StringVar()
       # Entry(self.root, textvariable=self.entryuser).place(relx=0.5, rely=0.2)


       # self.entrypass = StringVar()
       # Entry(self.root, w_hrr1='*', textvariable=self.entrypass).place(relx=0.5, rely=0.4)
        Label(self.root, text = 'Please Choose form').place(relx=0.5, rely=0.25, anchor = CENTER)       

        
        Button(self.root, text = 'Week form', height = 2, width = 25, command = self.open_before_week)\
                          .place(relx=0.5, rely=0.5,anchor = CENTER)
        Button(self.root, text = 'Month form', height = 2, width = 25, command = self.open_month)\
                          .place(relx=0.5, rely=0.75,anchor = CENTER)


       # self.buttontext = StringVar()
       # self.buttontext.set("Login")
       # Button(self.root, textvariable=self.buttontext, command=self.open_new)\
        #                  .place(relx=0.5, rely=0.8, anchor=CENTER)


        self.root.mainloop()
    def open_before_week(self):
        def open_week():
            self.root.destroy()
            ask_work.destroy()
            Pattern_week()
        ask_work = Tk()
        ask_work.geometry("300x200+600+300")
        ask_work.wm_title("My salary")
        Label(ask_work, text='How many days do you work in 1 week ? ').place(relx=0.15, rely=0.2)
        workday = StringVar(ask_work)
        Entry(ask_work, textvariable=workday).place(relx=0.3, rely=0.5)
        Button(ask_work, text='OK', command=open_week).place(relx=0.46, rely=0.7)


    
        

        
        
        
    

    def open_month(self):
        self.root.destroy()
        Pattern_month()


##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)
        
##    def button_click(self):
##        tkMessageBox.w_hrr1warning("Error", "Bad username and password")

class Pattern_week(object):
    def __init__(self):
        week = Tk()
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'earnings', )
        listtime = [0,1,2,3,4,5,6,7,8,9]
        



  
##--------------------------- SUB IN -----------------------------------------------

        def w_hrr1(self, index, mode):
            num = week.globalgetvar(self)
            if num == 1:
                week.hourright = StringVar(week)
                week.hourright.set(listtime[0])
                week.hourright.trace('w', w_mn1)
                OptionMenu(week,week.hourright, *listtime[0:3]).place(relx=0.1, rely=0.35)
            else:
                week.hourright = StringVar(week)
                week.hourright.set(listtime[8])
                week.hourright.trace('w', w_mn1)
                OptionMenu(week,week.hourright, *listtime[8::]).place(relx=0.1, rely=0.35)
                
        def w_mn1(self, index, mode):
            set1 = week.globalgetvar(self)
            if set1 == 2:
                week.minuteleft = StringVar(week)
                week.minuteleft.set(listtime[0])
                OptionMenu(week,week.minuteleft, listtime[0]).place(relx=0.23, rely=0.35)
                
                week.minuteright = StringVar(week)
                week.minuteright.set(listtime[0])
                OptionMenu(week,week.minuteright, listtime[0]).place(relx=0.32, rely=0.35)
            else:
                week.minuteleft = StringVar(week)
                week.minuteleft.set(listtime[0])
                OptionMenu(week,week.minuteleft, *listtime[:6]).place(relx=0.23, rely=0.35)

                week.minuteright = StringVar(week)
                week.minuteright.set(listtime[0])
                OptionMenu(week,week.minuteright, *listtime).place(relx=0.32, rely=0.35)


##--------------------------- SUB OUT -----------------------------------------------
                
        def w_mn2(self, index, mode):
            set2 = week.globalgetvar(self)
            if set2 == 9:
                week.minuteleft2 = StringVar(week)
                week.minuteleft2.set(listtime[0])
                OptionMenu(week,week.minuteleft2, *listtime[:6]).place(relx=0.82, rely=0.35)

                week.minuteright2 = StringVar(week)
                week.minuteright2.set(listtime[0])
                OptionMenu(week,week.minuteright2, *listtime[0:]).place(relx=0.91, rely=0.35)
            else:
                week.minuteleft2 = StringVar(week)
                week.minuteleft2.set(listtime[0])
                OptionMenu(week,week.minuteleft2, *listtime[:6]).place(relx=0.82, rely=0.35)

                week.minuteright2 = StringVar(week)
                week.minuteright2.set(listtime[0])
                OptionMenu(week,week.minuteright2, *listtime).place(relx=0.91, rely=0.35)


##-------------------------------------------------------------------------------------
                
        
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'Earnings Per Hours :', ).place(relx=0.25, rely=0.1)

        self.earn= StringVar(week)
        Entry(week, textvariable=self.earn).place(relx=0.45, rely=0.1)
        

##------------------------------ IN ---------------------------------------------------

      
        self.hourleft = StringVar(week)
        self.hourleft.trace('w', w_hrr1)
        self.hourleft.set(listtime[0])
        OptionMenu(week,self.hourleft, *listtime[0:2]).place(relx=0.01, rely=0.35)

        self.hourright = StringVar(week)
        self.hourright.set(listtime[8])
        OptionMenu(week,self.hourright, *listtime[8::]).place(relx=0.1, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.2, rely=0.36)

        Label(week, text = 'What time do you start your work?', ).place(relx=0.05, rely=0.26)

        self.minuteleft = StringVar(week)
        self.minuteleft.set(listtime[0])
        OptionMenu(week,self.minuteleft, *listtime[:6]).place(relx=0.23, rely=0.35)

        self.minuteright = StringVar(week)
        self.minuteright.set(listtime[0])
        OptionMenu(week,self.minuteright, *listtime).place(relx=0.32, rely=0.35)



##------------------------------ OUT ---------------------------------------------------
        
        self.hourleft2 = StringVar(week)
        self.hourleft2.set(listtime[1])
        OptionMenu(week,self.hourleft2, *listtime[1:2]).place(relx=0.6, rely=0.35)

        self.hourright2 = StringVar(week)
        self.hourright2.trace('w', w_mn2)
        self.hourright2.set(listtime[3])
        OptionMenu(week,self.hourright2, *listtime[3::]).place(relx=0.69, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.79, rely=0.36)
        Label(week, text = 'What time do you knock off?', ).place(relx=0.65, rely=0.26)

        self.minuteleft2 = StringVar(week)
        self.minuteleft2.set(listtime[0])
        OptionMenu(week,self.minuteleft2, *listtime[:6]).place(relx=0.82, rely=0.35)

        self.minuteright2 = StringVar(week)
        self.minuteright2.set(listtime[0])
        OptionMenu(week,self.minuteright2, *listtime).place(relx=0.91, rely=0.35)
##----------------------------Break------------------------------------------------------
        label = Label(week, text= 'Do you take a break ?')
        label.place(relx=0.39, rely=0.5)
    ##------------------destroytext and replace textbox ---------------------------------
        def button_yes():
            label.destroy()
            butt_yes.destroy()
            butt_no.destroy()
                
            Label(week, text = '-', ).place(relx=0.49, rely=0.556)
            Label(week, text = 'Break time', ).place(relx=0.455, rely=0.46)
            
            self.breaks = StringVar(week)
            Entry(week, textvariable=self.breaks).place(relx=0.26, rely=0.55)

            self.start= StringVar(week)
            Entry(week, textvariable=self.start).place(relx=0.54, rely=0.55)

            
            butt_submit.place(relx=0.34, rely=0.69)
            butt_cancel.place(relx=0.54, rely=0.69)
        def button_no():
            label.destroy()
            butt_yes.destroy()
            butt_no.destroy()

            
            butt_submit.place(relx=0.36, rely=0.6)
            butt_cancel.place(relx=0.56, rely=0.6)
        def new_windows():
            def back_2_week():
                butt_submit.destroy()
                butt_cancel.destroy()
                new_win.destroy()
            new_win = Tk()
            new_win.geometry("250x200+500+250")
            new_win.wm_title("My salary")
            
            Label(new_win, text = 'Please select the number of working days').place(relx=0.038, rely=0.2)


            work_day = StringVar(new_win)
            work_day.set(0)
            listweek = [1,2,3,4,5,6,7]
            OptionMenu(new_win, work_day, *listweek).place(relx=0.4, rely=0.4)
            Button(new_win,text='OK', command = back_2_week).place(relx=0.4, rely=0.7)

        
               

        def back():
            week.destroy()
            App()
            
            
               
        
        butt_yes = Button(week, text='Yes', command =button_yes)
        butt_yes.place(relx=0.6, rely=0.5)
        butt_no = Button(week, text='No', command = button_no)
        butt_no.place(relx=0.65, rely=0.5)
        butt_submit = Button(week, text = 'Submit', command = new_windows,  height = 1, width = 10)
        butt_cancel = Button(week, text = 'Cancel',command = back,  height = 1, width = 10)

        
         
       

    
        
        week.mainloop()

class Pattern_month(object):
    def __init__(self):
        self.month = Tk()
        self.month.geometry("600x300+500+250")
        self.month.wm_title("My salary")   

        
if __name__ == '__main__':
    App()
