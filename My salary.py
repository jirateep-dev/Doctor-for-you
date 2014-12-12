from Tkinter import *
import tkMessageBox
days_w, days_m = 7, 30

listtime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
hour_in, hour_out = [0, 0], [0, 0]
minute_in, minute_out = [0, 0], [0, 0]
tick_cfm1, tick_cfm2 = [0], [0]

class App(object):
    
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("400x200+550+300")
        self.root.wm_title("My salary")
        Label(self.root, text = 'Please Choose form').place(relx=0.5, rely=0.25, anchor = CENTER)       

        week = Button(self.root, text = 'Week form', height = 2, width = 25, command = self.destroyers)
        week.place(relx=0.5, rely=0.5,anchor = CENTER)
        month = Button(self.root, text = 'Month form', height = 2, width = 25, command = self.destroyers2)
        month.place(relx=0.5, rely=0.75,anchor = CENTER)   

        self.root.mainloop()

##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)

    def destroyers(self):
        self.root.destroy()
        Check_days(days_w)

    def destroyers2(self):
        self.root.destroy()
        Check_days(days_m)


class Check_days(object):
    
    def __init__(self, days):
        self.ask_work = Tk()
        self.ask_work.geometry("300x200+600+300")
        self.ask_work.wm_title("My salary")

        if days == 7:
            Label(self.ask_work, text='How many days do you work in 1 week ? ').place(relx=0.15, rely=0.2)
            Button(self.ask_work, text='OK', command= self.open_calculate).place(relx=0.4, rely=0.7)
            Button(self.ask_work, text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)
        else:
            Label(self.ask_work, text='How many days do you work in 1 month ? ').place(relx=0.15, rely=0.2)
            Button(self.ask_work, text='OK', command= self.open_calculate2).place(relx=0.4, rely=0.7)
            Button(self.ask_work, text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)

        self.workday = IntVar()
        Entry(self.ask_work, textvariable=self.workday, justify='center', bd = 5).place(relx=0.3, rely=0.45)
        

    def open_calculate(self):
        days = 7
        result = Check_moredays(days, self.workday.get())
        call_result = result.calculate_day()

        if call_result == True:
            self.ask_work.destroy()
            Pattern(self.workday.get())
        else:
            if self.workday == 0:
                tkMessageBox.showwarning("Error", "Error input have more than one day")
            else:
                tkMessageBox.showwarning("Error", "Error day out of range in 1 week")

    def open_calculate2(self):
        days = 30
        self.result = Check_moredays(days, self.workday.get())
        self.call_calculate = self.result.calculate_day()

        if self.call_calculate == True:
            self.ask_work.destroy()
            Pattern(self.workday.get())
        else:
            if self.workday == 0:
                tkMessageBox.showwarning("Error", "Error input have more than one day")
            else: 
                tkMessageBox.showwarning("Error", "Error day out of range in 1 month")


    def destroyer(self):
        self.ask_work.destroy()
        App()

    def open_from(self):
        self.ask_work.destroy()
        Pattern()



class Check_moredays(object):
    def __init__(self, days, workday):
        self.workday = workday
        self.days = days

    def calculate_day(self):
        return False if self.workday > self.days or self.workday == 0 else True

##------------------------------------------------------- Pattern --------------------------------------------------------------------
class Pattern(object):

    def __init__(self, workday):
        week = Tk()

        self.workday = workday

        week.geometry("650x350+500+250")
        week.wm_title("My salary")
        Label(week, text = 'Earnings Per Hours :', ).place(relx=0.30, rely=0.1)

        self.earn = IntVar()
        Entry(week, textvariable=self.earn, justify='center', bd = 5).place(relx=0.50, rely=0.1)

        Label(week, text = ':', ).place(relx=0.2, rely=0.36)
        Label(week, text = 'What time do you start your work?', ).place(relx=0.05, rely=0.26)

        Label(week, text = ':', ).place(relx=0.79, rely=0.36)
        Label(week, text = 'What time do you knock off?', ).place(relx=0.65, rely=0.26)
        

        self.time_in_out(week)

    
    def time_in_out(self, week):

        
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
        

        butt_set1 = Button(week, text='SET TIME', command =button_set1)
        butt_con1 = Button(week, text='Confirm', command =button_confirm1)
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
        
        
        butt_set2 = Button(week, text='SET TIME', command =button_set2)
        butt_con2 = Button(week, text='Confirm', command =button_confirm2)
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

        label = Label(week, text= 'Do you take a break ?')
        label.place(relx=0.42, rely=0.56)

    ##----------------------------------------destroytext and replace textbox ---------------------------------
        # def button_set1():

        # def button_set2():

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
                textbreak.place(relx=0.455, rely=0.52)    
                breaks.place(relx=0.4, rely=0.61)

        def button_back():

            textbreak.place_forget()
            breaks.place_forget()
            butt_back.place_forget()

            self.breaks.set(0)

            label.place(relx=0.42, rely=0.56)
            butt_yes.place(relx=0.48, rely=0.64)


        def new_windows():
            num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))
            if (tick_cfm1[0] != 1 or tick_cfm2[0] != 1) and (tick_cfm1[0] == 0 or tick_cfm2[0] == 0):
                if num_hour_in > num_hour_out:
                    tkMessageBox.showwarning("Error", "Error, Please enter time knock off.")
                else:
                    tkMessageBox.showwarning("Error", "Error, Please click set time and confirm button")
            else:
                print 'Yes'

            # def back_2_week():
            #     week.deiconify()
            #     new_win.withdraw()
                
            # week.withdraw()

            # new_win = Tk()
            # new_win.geometry("250x200+650+300")
            # new_win.wm_title("My salary")
            
            # Label(new_win, text = 'Please select the number of working days').place(relx=0.038, rely=0.24)

            # listweek = map(int, xrange(31))

            # work_days = IntVar(new_win)
            # work_days.set(1)
            # OptionMenu(new_win, work_days, *listweek[1:self.workday+1]).place(relx=0.4, rely=0.44)

            # Button(new_win,text='OK', command = back_2_week).place(relx=0.4, rely=0.74)
        

        def cancel():
            week.destroy()
            App()
            
        textbreak = Label(week, text = 'Break time', )
        
        self.breaks = IntVar()
        breaks = Entry(week, textvariable=self.breaks, justify='center', bd = 5)

        butt_yes = Button(week, text='Yes', command =button_yes)
        butt_back = Button(week, text='Back', command = button_back)
        butt_submit = Button(week, text = 'Submit', command = new_windows,  height = 1, width = 10)
        butt_cancel = Button(week, text = 'Cancel',command = cancel,  height = 1, width = 10)

        butt_yes.place(relx=0.48, rely=0.64)
        butt_submit.place(relx=0.35, rely=0.77)
        butt_cancel.place(relx=0.53, rely=0.77)
        
        week.mainloop()

# class Conclude(object):
#     def __init__():


        
if __name__ == '__main__':
    App()
