from Tkinter import *
import tkMessageBox

tick_cfm1, tick_cfm2 = [0], [0]
sub_wkd, daysl = [0], [0]
earn_get_all = [0]

class App(object):
    
    def __init__(self):
        
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.geometry("400x200+550+300")
        self.root.wm_title("My salary")
        Label(self.root, fg = "blue", font = "Helvetica 20 bold",text = 'Please Choose Form').place(relx=0.5, rely=0.2, anchor = CENTER)       

        week = Button(self.root,font = " Serif 12 bold",fg="midnight blue", text = 'Week form', height = 2, width = 25, command = lambda : self.destroyers(7))
        week.place(relx=0.5, rely=0.5,anchor = CENTER)
        month = Button(self.root,font = " Serif 12 bold",fg="midnight blue", text = 'Month form', height = 2, width = 25, command = lambda : self.destroyers(30))
        month.place(relx=0.5, rely=0.8,anchor = CENTER)   

        self.root.mainloop()

    def destroyers(self, days):
        self.root.destroy()
        Check_days(days)


class Check_days(object):
    
    def __init__(self, days):
        self.ask_work = Tk()
        self.ask_work.resizable(0,0)
        self.ask_work.geometry("300x200+600+300")
        self.ask_work.wm_title("My salary")

        if days == 7:
            Label(self.ask_work, font = "System 14 ", text='How many days do you work in 1 week ? ').place(relx=0.05, rely=0.2)
            Button(self.ask_work,font = "System 14 ",fg="midnight blue", text='OK', command= lambda : self.open_calculate(days)).place(relx=0.35, rely=0.7)
            Button(self.ask_work,font = "System 14 ",fg="midnight blue", text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)
        else:
            Label(self.ask_work,font = "System 14 ",  text='How many days do you work in 1 month ? ').place(relx=0.05, rely=0.2)
            Button(self.ask_work,font = "System 14 ",fg="midnight blue", text='OK ', command= lambda : self.open_calculate(days)).place(relx=0.35, rely=0.7)
            Button(self.ask_work,font = "System 14 ",fg="midnight blue", text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)

        self.workday = IntVar()
        self.entry = Entry(self.ask_work, textvariable=self.workday, justify='center', bd = 5)
        self.entry.place(relx=0.3, rely=0.45)
        

    def open_calculate(self, days):
        result = Check_moredays(days, self.workday.get())
        call_result = result.calculate_day()

        if call_result == True:
            self.ask_work.destroy()
            daysl[0] = self.workday.get()
            Pattern(daysl[0])
        else:
            if self.workday.get() == 0:
                tkMessageBox.showwarning("Error", "Error input have more than one day")
            else:
                if days == 7:
                    tkMessageBox.showwarning("Error", "Error day out of range in 1 week \nPlease enter days in range 1-7")
                else:
                    tkMessageBox.showwarning("Error", "Error day out of range in 1 month \nPlease enter days in range 1-30")


    def destroyer(self):
        self.ask_work.destroy()
        App()


class Check_moredays(object):
    def __init__(self, days, workday):
        self.workday_come = workday
        self.days_come = days

    def calculate_day(self):
        return False if self.workday_come > self.days_come or self.workday_come <= 0 else True

##------------------------------------------------------- Pattern --------------------------------------------------------------------
class Pattern(object):
    

    def __init__(self, workday):
        week = Tk()
        week.resizable(0,0)

        textconclude = ''

        if workday <= 7:
            textconclude = "Total income in this week"
        else:
            textconclude = "Total income in this month"

        week.geometry("650x350+450+250")
        week.wm_title("My salary")
        
        Label(week,font = "Verdana 10 bold",fg="DodgerBlue4", text = 'Earnings Per Hours :', ).place(relx=0.25, rely=0.1)

        self.earn = IntVar()
        Entry(week, textvariable=self.earn, justify='center', bd = 5).place(relx=0.50, rely=0.1)

        Label(week,font = "Verdana 10 bold", text = ':', ).place(relx=0.2, rely=0.36)
        Label(week,font = "Verdana 10 bold",fg="dark goldenrod", text = 'What time do you start your work?', ).place(relx=0.03, rely=0.26)

        Label(week,font = "Verdana 10 bold", text = ':', ).place(relx=0.79, rely=0.36)
        Label(week,font = "Verdana 10 bold",fg="dark goldenrod", text = 'What time do you knock off?', ).place(relx=0.62, rely=0.26)
        

        listtime= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hour_in, hour_out = [0, 0], [0, 0]
        minute_in, minute_out = [0, 0], [0, 0]
        
##------------------------------------------- TIME SUB IN -----------------------------------------------------------------------

    ##------------------------------------ SUB TIME IN HOURS ----------------------------------------------------
        def w_hrl(event):
            hour_in[0] = self.hourleft.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

                 
        def w_hrr(event):
            hour_in[1] = self.hourright.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


    ##----------------------------------- SUB TIME IN MINUTES-------------------------------------------------
        def w_mnl(event):
            minute_in[0] = self.minuteleft.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

        def w_mnr(event):
            minute_in[1] = self.minuteright.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


##----------------------------------------- SUB TIME OUT ----------------------------------------------------------------------------
    
    ##---------------------------------- SUB TIME OUT HOURS---------------------------------------------------

        def w_hrl2(event):
            hour_out[0] = self.hourleft2.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

        def w_hrr2(event):
            hour_out[1] = self.hourright2.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


    ##-------------------------------- SUB TIME OUT MINUTE------------------------------------------
        def w_mnl2(event):
            minute_out[0] = self.minuteleft2.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


        def w_mnr2(event):
            minute_out[1] = self.minuteright2.get()
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            

##------------------------------------------------------------------------------------------------------------------------
                
        

        
##------------------------------------------------------ TIME IN ---------------------------------------------------------------
        def button_set1():
            butt_set1.place_forget()
            butt_con1.place(relx=0.16, rely=0.46)
            op1.config(state = NORMAL)
            op2.config(state = NORMAL)
            op3.config(state = NORMAL)
            op4.config(state = NORMAL)
            tick_cfm1[0] = 0

        def button_confirm1():
            num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))
            num_minute_in, num_minute_out = int(str(minute_in[0])+str(minute_in[1])), int(str(minute_out[0])+str(minute_out[1]))
            if num_hour_in > 23:
                tkMessageBox.showwarning("Error", "Error, Out of range hours in 1 day \n Please select hour in the range 0-23")
            elif (num_hour_in > num_hour_out and num_hour_out != 0) or (num_hour_in == num_hour_out and num_minute_in > num_minute_out):
                tkMessageBox.showwarning("Error", "Error, You must enter time start your work \n more than time knock off")
            else:
                butt_con1.place_forget()
                butt_set1.place(relx=0.16, rely=0.46)
                op1.config(state = DISABLED)
                op2.config(state = DISABLED)
                op3.config(state = DISABLED)
                op4.config(state = DISABLED)
                tick_cfm1[0] = 1
      
        self.hourleft = IntVar(week)
        self.hourleft.set(listtime[0])
        op1 = OptionMenu(week,self.hourleft, *listtime[0:3], command=w_hrl)
        op1.config(state = DISABLED)
        op1.place(relx=0.01, rely=0.35)
        
        self.hourright = IntVar(week)
        self.hourright.set(listtime[0])
        op2 = OptionMenu(week,self.hourright, *listtime, command=w_hrr)
        op2.config(state = DISABLED)
        op2.place(relx=0.1, rely=0.35)
        

        butt_set1 = Button(week,font = "Verdana 8",fg="dark goldenrod", text='SET TIME', command =button_set1)
        butt_con1 = Button(week,font = "Verdana 8",fg="dark goldenrod", text='Confirm', command =button_confirm1)
        butt_set1.place(relx=0.16, rely=0.46)


        self.minuteleft = IntVar(week)
        self.minuteleft.set(listtime[0])
        op3 = OptionMenu(week,self.minuteleft, *listtime[:6], command=w_mnl)
        op3.config(state = DISABLED)
        op3.place(relx=0.23, rely=0.35)

        self.minuteright = IntVar(week)
        self.minuteright.set(listtime[0])
        op4 = OptionMenu(week,self.minuteright, *listtime, command=w_mnr)
        op4.config(state = DISABLED)
        op4.place(relx=0.32, rely=0.35)

        

##------------------------------------------------------ TIME OUT ------------------------------------------------------------------

        def button_set2():
            butt_set2.place_forget()
            butt_con2.place(relx=0.74, rely=0.46)
            op5.config(state = NORMAL)
            op6.config(state = NORMAL)
            op7.config(state = NORMAL)
            op8.config(state = NORMAL)
            tick_cfm2[0] = 0

        def button_confirm2():
            num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))
            num_minute_in, num_minute_out = int(str(minute_in[0])+str(minute_in[1])), int(str(minute_out[0])+str(minute_out[1])) 
            if num_hour_out > 23:
                tkMessageBox.showwarning("Error", "Error, Out of range hours in 1 day \n Please select hour in the range 0-23")
            elif num_hour_in > num_hour_out or (num_hour_in == num_hour_out and num_minute_in > num_minute_out):
                tkMessageBox.showwarning("Error", "Error, You must enter time start your work \n more than time knock off")
            else:
                butt_con2.place_forget()
                butt_set2.place(relx=0.74, rely=0.46)
                op5.config(state = DISABLED)
                op6.config(state = DISABLED)
                op7.config(state = DISABLED)
                op8.config(state = DISABLED)
                tick_cfm2[0] = 1
        
        self.hourleft2 = IntVar(week)
        self.hourleft2.set(listtime[0])
        op5 = OptionMenu(week,self.hourleft2, *listtime[0:3], command=w_hrl2)
        op5.config(state = DISABLED)
        op5.place(relx=0.6, rely=0.35)

        self.hourright2 = IntVar(week)
        self.hourright2.set(listtime[0])
        op6 = OptionMenu(week,self.hourright2, *listtime, command=w_hrr2)
        op6.config(state = DISABLED)
        op6.place(relx=0.69, rely=0.35)
        
        
        butt_set2 = Button(week,font = "Verdana 8",fg="dark goldenrod", text='SET TIME', command =button_set2)
        butt_con2 = Button(week,font = "Verdana 8",fg="dark goldenrod", text='Confirm', command =button_confirm2)
        butt_set2.place(relx=0.74, rely=0.46)

        self.minuteleft2 = IntVar(week)
        self.minuteleft2.set(listtime[0])
        op7 = OptionMenu(week,self.minuteleft2, *listtime[:6], command=w_mnl2)
        op7.config(state = DISABLED)
        op7.place(relx=0.82, rely=0.35)

        self.minuteright2 = IntVar(week)
        self.minuteright2.set(listtime[0])
        op8 = OptionMenu(week,self.minuteright2, *listtime, command=w_mnr2)
        op8.config(state = DISABLED)
        op8.place(relx=0.91, rely=0.35)


##--------------------------------------------------------Break------------------------------------------------------

        label = Label(week,font = " Sans 12 bold ", fg = "slate blue", text= 'Do you take a break ?')
        label.place(relx=0.39, rely=0.56)

    ##----------------------------------------destroytext and replace textbox ---------------------------------

        def button_yes():
            num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))

            if (tick_cfm1[0] != 1 or tick_cfm2[0] != 1) and (tick_cfm1[0] == 0 or tick_cfm2[0] == 0):
                if num_hour_in > num_hour_out:
                    tkMessageBox.showwarning("Error", "Error, Please enter time knock off.")
                else:
                    tkMessageBox.showwarning("Error", "Error, Please click set time and confirm button")
            else:
                label.place_forget()
                butt_yes.place_forget()

                butt_back.place(relx=0.61, rely=0.61)
                textbreak.place(relx=0.40, rely=0.52)    
                breaks.place(relx=0.4, rely=0.61)

        def button_back():

            textbreak.place_forget()
            breaks.place_forget()
            butt_back.place_forget()

            self.breaks.set(0)

            label.place(relx=0.39, rely=0.56)
            butt_yes.place(relx=0.48, rely=0.64)


        def new_windows():
            num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))
            num_minute_in, num_minute_out = int(str(minute_in[0])+str(minute_in[1])), int(str(minute_out[0])+str(minute_out[1]))

            if (tick_cfm1[0] != 1 or tick_cfm2[0] != 1) and (tick_cfm1[0] == 0 or tick_cfm2[0] == 0):
                if num_hour_in > num_hour_out:
                    tkMessageBox.showwarning("Error", "Error, Please enter time knock off.")
                else:
                    tkMessageBox.showwarning("Error", "Error, Please click set time and confirm button.")
            elif self.breaks.get() >= num_hour_out - num_hour_in:
                tkMessageBox.showwarning("Error", "Error, Please enter break time less than working time.")
            else:
                if num_minute_in > 30:
                    num_hour_in += 1
                if num_minute_out > 30:
                    num_hour_out += 1
                sub_time = num_hour_out - num_hour_in - self.breaks.get()
                earn_get = self.earn.get()*sub_time
                print earn_get
                Conclude(workday, earn_get, week, textconclude)

        def cancel():
            week.destroy()
            App()
            
        
        self.breaks = IntVar()
        breaks = Entry(week, textvariable=self.breaks, justify='center', bd = 5)
        textbreak = Label(week,font = "Verdana 10 bold",fg="medium slate blue", text = 'Break time (HOUR)', ) 
        
        butt_yes = Button(week,font = "Verdana 8",fg="medium slate blue", text='Yes', command =button_yes)
        butt_back = Button(week,font = "Verdana 8",fg="medium slate blue", text='Back', command = button_back)
        butt_submit = Button(week,font = "Verdana 12 bold",fg="red", text = 'Submit', command = new_windows,  height = 1, width = 10)
        butt_cancel = Button(week,font = "Verdana 12 bold",fg="red",  text = 'Cancel',command = cancel)

        butt_yes.place(relx=0.48, rely=0.64)
        butt_submit.place(relx=0.33, rely=0.8)
        butt_cancel.place(relx=0.53, rely=0.8)
        
        week.mainloop()

class Conclude(object):
    

    def __init__(self, wkd, money, wee, textconclude):
          
        #wee.withdraw()
        wee.destroy()
        text =  textconclude

        new_win = Tk()
        new_win.resizable(0,0)
        new_win.geometry("300x250+650+300")
        new_win.wm_title("My salary")
            
        Label(new_win,font = "System 14 ", text = 'Please select the number of working days').place(relx=0.038, rely=0.24)

        listweek = map(int, xrange(31))

        work_days = IntVar(new_win)
        work_days.set(1)
        OptionMenu(new_win, work_days, *listweek[1:daysl[0]+1]).place(relx=0.4, rely=0.44)

        Button(new_win,font = "System 14 ",fg="midnight blue",text='OK', command = lambda : self.sub_con(wkd, work_days.get(), money, new_win, wee, textconclude)).place(relx=0.43, rely=0.74)

    def sub_con(self, wkds, wkdg, money, nww, wees, textconclude):

        sub_wkd[0] = daysl[0]-wkdg
        daysl[0] = sub_wkd[0]
        earn_get_all[0] += money*wkdg

        if daysl[0] > 0:
            #nww.withdraw()
            nww.destroy()
            Pattern(daysl[0])
            #wees.deiconify()
        else:
            #nww.withdraw()
            nww.destroy()
            Answer(earn_get_all[0], textconclude)

          
class Answer(object):

    def __init__(self, moneys, textconclude):
        
        self.ans = Tk()
        self.ans.resizable(0,0)
        self.ans.geometry("350x350+650+300")
        self.ans.wm_title("My slary")

       # photo = PhotoImage(file="goldpack.gif")
       # Label(ans, image = photo).pack_propagate(0)

        Label(self.ans,font = "Helvetica 18 bold ", fg = "yellow green", text = textconclude).place(relx=0.06, rely=0.05)

        Label(self.ans,font = "Verdana 12 ",fg="yellow green", text = 'You get money  =  %d'%moneys).place(relx=0.25, rely=0.75)
       
        Button(self.ans,font = "system 14",fg= "blue", text = 'Back to main menu', height = 2, width = 15, command = self.gomain).place(relx=0.5, rely=0.9,anchor = CENTER)
    
    def gomain(self):
        self.ans.destroy()
        App()
        
if __name__ == '__main__':
    App()
