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

        
        Button(self.root, text = 'Week form', height = 2, width = 25, command = self.open_week)\
                          .place(relx=0.5, rely=0.5,anchor = CENTER)
        Button(self.root, text = 'Month form', height = 2, width = 25, command = self.open_month)\
                          .place(relx=0.5, rely=0.75,anchor = CENTER)


       # self.buttontext = StringVar()
       # self.buttontext.set("Login")
       # Button(self.root, textvariable=self.buttontext, command=self.open_new)\
        #                  .place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.mainloop()
        
    def open_week(self):
        self.root.destroy()
        Pattern()

    def open_month(self):
        self.root.destroy()
        Pattern()


##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)
        
##    def button_click(self):
##        tkMessageBox.w_hrr1warning("Error", "Bad username and password")

class Pattern(object):

    def __init__(self):
        
        week = Tk()
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'earnings', )
        listtime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hour_in, hour_out = [0, 0], [0, 0]
        minute_in, minute_out = [0, 0], [0, 0]
        
##------------------------------------------- TIME SUB IN -----------------------------------------------------------------------

    ##------------------------------------ SUB TIME IN HOURS ----------------------------------------------------

        def w_hrl(self, index, mode):
            hrl = week.globalgetvar(self)
            hour_in[0] = hrl
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            if hrl >= hour_out[0]:
                week.hourleft2 = StringVar(week)
                week.hourleft2.trace('w', w_hrl2)
                week.hourleft2.set(listtime[hrl])
                OptionMenu(week,week.hourleft2, *listtime[hrl:3]).place(relx=0.6, rely=0.35)
                if hrl == 2:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[0])
                    OptionMenu(week,week.hourright, *listtime[hour_in[1]:5]).place(relx=0.1, rely=0.35)

                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[0])
                    OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
            else:
                week.hourleft2 = StringVar(week)
                week.hourleft2.trace('w', w_hrl2)
                week.hourleft2.set(listtime[hour_out[0]])
                OptionMenu(week,week.hourleft2, *listtime[hour_in[0]:3]).place(relx=0.6, rely=0.35)
                if hrl == 2:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[0])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
                else:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
                 
        def w_hrr(self, index, mode):
            hrr = week.globalgetvar(self)
            hour_in[1] = hrr
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if hour_out[0] != 2 and hour_out[0] == hour_in[0]:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)

            elif hour_out[0] == 2 and hour_in[0] == 2:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)

            elif hour_out[0] == 2 and hour_in[0] != 2:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)
            else:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_out[1]])
                OptionMenu(week,week.hourright2, *listtime).place(relx=0.69, rely=0.35)

    ##----------------------------------- SUB TIME IN MINUTES-------------------------------------------------
        def w_mnl(self, index, mode):
            mnl = week.globalgetvar(self)
            minute_in[0] = mnl
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if (hour_in[0] == hour_out[0]) and (hour_in[1] == hour_out[1]):
                if minute_in[0] >= minute_out[0]:
                    week.minuteleft2 = StringVar(week)
                    week.minuteleft2.trace('w', w_mnl2)
                    week.minuteleft2.set(listtime[minute_in[0]])
                    OptionMenu(week,week.minuteleft2, *listtime[minute_in[0]:6]).place(relx=0.82, rely=0.35)
                else:
                    week.minuteleft2 = StringVar(week)
                    week.minuteleft2.trace('w', w_mnl2)
                    week.minuteleft2.set(listtime[minute_out[0]])
                    OptionMenu(week,week.minuteleft2, *listtime[minute_in[0]:6]).place(relx=0.82, rely=0.35)

        def w_mnr(self, index, mode):
            mnr = week.globalgetvar(self)
            minute_in[1] = mnr
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if (hour_in[0] == hour_out[0]) and (hour_in[1] == hour_out[1]):
                if minute_in[1] >= minute_out[1]:
                    week.minuteright2 = StringVar(week)
                    week.minuteright2.trace('w', w_mnr2)
                    week.minuteright2.set(listtime[minute_in[1]])
                    OptionMenu(week,week.minuteright2, *listtime[minute_in[1]::]).place(relx=0.91, rely=0.35)
                else:
                    week.minuteright2 = StringVar(week)
                    week.minuteright2.trace('w', w_mnr2)
                    week.minuteright2.set(listtime[minute_out[1]])
                    OptionMenu(week,week.minuteright2, *listtime[minute_in[1]::]).place(relx=0.91, rely=0.35)


##----------------------------------------- SUB TIME OUT ----------------------------------------------------------------------------
    
    ##---------------------------------- SUB TIME OUT HOURS---------------------------------------------------

        def w_hrl2(self, index, mode):
            hrl2 = week.globalgetvar(self)
            hour_out[0] = hrl2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            if hrl2 == 2:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[0])
                OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
            elif hrl2 == hour_in[0]:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_in[1]])
                OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)
            else:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_out[1]])
                OptionMenu(week,week.hourright2, *listtime).place(relx=0.69, rely=0.35)
            

        def w_hrr2(self, index, mode):
            hrr2 = week.globalgetvar(self)
            hour_out[1] = hrr2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


    ##-------------------------------- SUB TIME OUT MINUTE------------------------------------------
        def w_mnl2(self, index, mode):
            mnl2 = week.globalgetvar(self)
            minute_out[0] = mnl2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


        def w_mnr2(self, index, mode):
            mnr2 = week.globalgetvar(self)
            minute_out[1] = mnr2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            

##------------------------------------------------------------------------------------------------------------------------
                
        
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'Earnings Per Hours :', ).place(relx=0.25, rely=0.1)

        self.earn= StringVar(week)
        Entry(week, textvariable=self.earn).place(relx=0.45, rely=0.1)
        

##------------------------------------------------------ TIME IN ---------------------------------------------------------------

      
        self.hourleft = StringVar(week)
        self.hourleft.trace('w', w_hrl)
        self.hourleft.set(listtime[0])
        OptionMenu(week,self.hourleft, *listtime[0:3]).place(relx=0.01, rely=0.35)
        
        self.hourright = StringVar(week)
        self.hourright.trace('w', w_hrr)
        self.hourright.set(listtime[0])
        OptionMenu(week,self.hourright, *listtime).place(relx=0.1, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.2, rely=0.36)
        Label(week, text = 'What time do you start your work?', ).place(relx=0.05, rely=0.26)
        

        self.minuteleft = StringVar(week)
        self.minuteleft.trace('w', w_mnl)
        self.minuteleft.set(listtime[0])
        OptionMenu(week,self.minuteleft, *listtime[:6]).place(relx=0.23, rely=0.35)

        self.minuteright = StringVar(week)
        self.minuteright.trace('w', w_mnr)
        self.minuteright.set(listtime[0])
        OptionMenu(week,self.minuteright, *listtime).place(relx=0.32, rely=0.35)



##------------------------------------------------------ TIME OUT ------------------------------------------------------------------
        
        self.hourleft2 = StringVar(week)
        self.hourleft2.trace('w', w_hrl2)
        self.hourleft2.set(listtime[0])
        OptionMenu(week,self.hourleft2, *listtime[0:3]).place(relx=0.6, rely=0.35)

        self.hourright2 = StringVar(week)
        self.hourright2.trace('w', w_hrr2)
        self.hourright2.set(listtime[0])
        OptionMenu(week,self.hourright2, *listtime).place(relx=0.69, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.79, rely=0.36)
        Label(week, text = 'What time do you knock off?', ).place(relx=0.65, rely=0.26)

        self.minuteleft2 = StringVar(week)
        self.minuteleft2.trace('w', w_mnl2)
        self.minuteleft2.set(listtime[0])
        OptionMenu(week,self.minuteleft2, *listtime[:6]).place(relx=0.82, rely=0.35)

        self.minuteright2 = StringVar(week)
        self.minuteright2.trace('w', w_mnr2)
        self.minuteright2.set(listtime[0])
        OptionMenu(week,self.minuteright2, *listtime).place(relx=0.91, rely=0.35)


        
        week.mainloop()



        
if __name__ == '__main__':
    App()
