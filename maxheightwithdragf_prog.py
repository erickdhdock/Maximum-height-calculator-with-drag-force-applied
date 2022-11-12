from calendar import monthrange
from cgi import test
from logging import root
from re import M
import tkinter as tk
from turtle import left, right, width
import math







def start_position():
    ##def funcs
    def ang_command():
        print('angle selected')
    
        window.destroy()
    
        angl_win = tk.Tk()
        angl_win.title("Angle Calculator")
        angl_win.option_add("*Font","Ariel 15")
        angl_win.geometry("500x500")
        angl_win.resizable(True,True)

        #calculated value
        def calculated_value_printer(x,y):
            calc_val = tk.Label(angl_win, text='calculated values are "{} degrees" and {} radians'.format(x,y) )
            calc_val.place(x=120, y=360)

        #ask g
        asker_g = tk.Label(angl_win, text='input gravitational acceleleration')
        asker_g.place(x=120, y=30)
        
        #make g input
        ent_g = tk.Entry(angl_win)
        ent_g.place(x=120,y=0)
        def get_g_value():
            g = ent_g.get()
            #print(f'[TRACE]: G IS {g}''\n')
            return g


        #ask H
        asker_H = tk.Label(angl_win, text='input maximum height')      
        asker_H.place(x=120, y = 120)
        
        #make h input
        ent_H = tk.Entry(angl_win)
        ent_H.place(x=120, y=90)
        def get_H_value():
            H = ent_H.get()
            #print(f'[TRACE]: H IS {H}''\n')
            return H


        #ask v0
        asker_v0 = tk.Label(angl_win, text='input initial speed')
        asker_v0.place(x=120, y=210)

        #make v0 input
        ent_v0 = tk.Entry(angl_win)
        ent_v0.place(x=120, y=180)
        def get_v0_value():
            v0 = ent_v0.get()
            #print(f'[TRACE]: v0 IS {v0}''\n')
            return v0

        def calculate():
            g = get_g_value()
            
            if g == '':
                #print('[trace]: g is 9.81')
                g = '9.81'
                g = float(g)
            else:
                g = float(get_g_value())

            H = float(get_H_value())
            
            v0 = float(get_v0_value())
            
            print(f'g:{g} H:{H} v0:{v0}')

            angval1 = 4 * g * H
        
            angval2 = v0 ** 2
            
            angval3 = angval1 / angval2
            
            angvalcos = 1 - angval3
            print(f'trace_{angvalcos}')
            angvalacos = math.acos(angvalcos)
            
            angvalrad = angvalacos / 2
            
            angvaldeg = 57.2958 * angvalrad

            #print(f'[TRACE]:calculated values are {angvaldeg}(deg) , and {angvalrad}')

            calculated_value_printer(angvaldeg,angvalrad)

        angl_calc_btn = tk.Button(angl_win)
        angl_calc_btn.config(text = 'Start Calculation')
        angl_calc_btn.config(command=calculate)
        angl_calc_btn.place(x=190, y=290)        


        angl_win.mainloop()
        









    def vel_command():
        print('velocity selected')
        window.destroy()
        vel_win = tk.Tk()
        vel_win.title("Speed Calculator")
        vel_win.geometry("500x500")
        


        #calculated value
        def calculated_value_printer(x):
            calc_val = tk.Label(vel_win, text='calculated initial speed is "{}m/s"'.format(x) )
            calc_val.place(x=120, y=360)

        #ask g
        asker_g = tk.Label(vel_win, text='input gravitational acceleleration')
        asker_g.place(x=120, y=30)
        
        #make g input
        ent_g = tk.Entry(vel_win)
        ent_g.place(x=120,y=0)
        def get_g_value():
            g = ent_g.get()
            #print(f'[TRACE]: G IS {g}''\n')
            return g


        #ask H
        asker_H = tk.Label(vel_win, text='input maximum height')      
        asker_H.place(x=120, y = 120)
        
        #make h input
        ent_H = tk.Entry(vel_win)
        ent_H.place(x=120, y=90)
        def get_H_value():
            H = ent_H.get()
            #print(f'[TRACE]: H IS {H}''\n')
            return H


        #ask angle
        asker_angle = tk.Label(vel_win, text='input launching angle')
        asker_angle.place(x=120, y=210)

        #make angle input
        ent_ang = tk.Entry(vel_win)
        ent_ang.place(x=120, y=180)
        def get_ang_value():
            ang = ent_ang.get()
            return ang

        
        def calculate():
            #recieve values
            g = get_g_value()
            
            if g == '':
                #print('[trace]: g is 9.81')
                g = '9.81'
                g = float(g)
            else:
                g = float(get_g_value())


            H = float(get_H_value())


            angle = float(get_ang_value())      

            #actual calculation starts
            v0val1 = 2 * g * H

            v0valangrad = angle / 57.2958
            v0valangforcos = math.cos(2 * v0valangrad)

            v0valangforsin1 = 1 - v0valangforcos

            v0valangforsin2 = v0valangforsin1 / 2

            v0val2 = v0val1 / v0valangforsin2

            finalval = math.sqrt(v0val2)

            calculated_value_printer(finalval)

        angl_calc_btn = tk.Button(vel_win)
        angl_calc_btn.config(text = 'Start Calculation')
        angl_calc_btn.config(command=calculate)
        angl_calc_btn.place(x=190, y=290)

        calculated_value_printer('none ')
        calculate()





        
        
    def mheight_command():
        print('max height selected')
        window.destroy()
        mheight_win = tk.Tk()
        mheight_win.title("Maximum Height Calculator")
        mheight_win.geometry("500x500")


        #calculated value
        def calculated_value_printer(x):
            calc_val = tk.Label(mheight_win, text='calculated maximum height is "{}m"'.format(x) )
            calc_val.place(x=120, y=360)


        #ask g
        asker_g = tk.Label(mheight_win, text='input gravitational acceleleration')
        asker_g.place(x=120, y=30)
        
        #make g input
        ent_g = tk.Entry(mheight_win)
        ent_g.place(x=120,y=0)
        def get_g_value():
            g = ent_g.get()
            #print(f'[TRACE]: G IS {g}''\n')
            return g


        #ask angle
        asker_angle = tk.Label(mheight_win, text='input launching angle')
        asker_angle.place(x=120, y=120)

        #make angle input
        ent_ang = tk.Entry(mheight_win)
        ent_ang.place(x=120, y=90)
        def get_ang_value():
            ang = ent_ang.get()
            return ang


        #ask v0
        asker_v0 = tk.Label(mheight_win, text='input initial speed')
        asker_v0.place(x=120, y=210)

        #make v0 input
        ent_v0 = tk.Entry(mheight_win)
        ent_v0.place(x=120, y=180)
        def get_v0_value():
            v0 = ent_v0.get()
            #print(f'[TRACE]: v0 IS {v0}''\n')
            return v0

        def calculate():
            #recieve values
            g = get_g_value()
            
            if g == '':
                g = '9.81'
                g = float(g)
            else:
                g = float(get_g_value())

            angle = float(get_ang_value())

            v0 = float(get_v0_value())

            

            Hval1 = v0 ** 2 
            Hval2radiant = angle / 57.2958
            Hval3 = Hval2radiant * 2
            Hval4 = 1 - math.cos(Hval3)
            Hval5sin_2x = Hval4 / 2
            Hval6 = Hval1 * Hval5sin_2x 
            accelgrav = 2 * g
            Hval7 = Hval6 / accelgrav 

            calculated_value_printer(Hval7)
        
        angl_calc_btn = tk.Button(mheight_win)
        angl_calc_btn.config(text = 'Start Calculation')
        angl_calc_btn.config(command=calculate)
        angl_calc_btn.place(x=190, y=290)




    
    
    window = tk.Tk()
    window.title("Select Mode")
    window.geometry("600x240+100+100")
    window.resizable(False,False)




    lable = tk.Label(window, text='select mode', font=('Arial', 15))

    lable.place(x=250, y=0)
    
    
    ang_btn = tk.Button(window, text = 'btn')
    ang_btn.config(width=23, height=2)
    ang_btn.config(text= 'calculate launching angle')
    ang_btn.config(command= ang_command)
    ang_btn.pack(side = 'left')
    
    vel_btn = tk.Button(window,text = 'btn1')
    vel_btn.config(text='calculate speed')
    vel_btn.config(width =23, height = 2)
    vel_btn.config(command=vel_command)
    vel_btn.pack(side='right')
    
    mheight_btn = tk.Button(window, text='btn')
    mheight_btn.config(width=23, height=2)
    mheight_btn.config(text='calculate maximum height')
    mheight_btn.config(command=mheight_command)
    mheight_btn.place(x=215, y=100)
    
    window.mainloop()



    

    
    


start_position()

    

