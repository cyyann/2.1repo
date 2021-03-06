# Versie 2.2
# Door Misha Dokter
# Datum: 01-11-'17

import matplotlib # matplotlib = voor graphs
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy
from drawnow import *
from matplotlib import style

import tkinter as tk # tkinter importen
from tkinter import ttk
import time
import serial
import time 

LARGE_FONT= ("Verdana", 12)

style.use('ggplot')
    
# Default instellingen            
class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Project GUI")
         
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TempPage, RollOut):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# Beginscherm GUI
    
class StartPage(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Maak uw keuze", font=LARGE_FONT)
        label.pack(pady=20,padx=10)

        # Rolluik omhoog laten gaan
        def upwards():
            self.lbl = tk.Label(self, text="Rolluik gaat omhoog...", font=('Helvetica', 10))
            self.lbl.pack(pady=10,padx=10)
            def change_color():
                    
                current_color = box.cget("background")
                for i in range(5):
                    next_color = "orange" if current_color == "green" else "green"
                box.config(background=next_color, height="3", width="6")
                root.after(500, change_color)
                
            box = tk.Text(self)
            box.pack()
            change_color()

            ser = serial.Serial(
                port = 'COM6',
                baudrate = 9600,
             )
            
            ser.write(1)

        # Rolluik omlaag laten gaan
        def downwards():
            label = tk.Label(self, text="Rolluik gaat omlaag...", font=('Helvetica', 10))
            label.pack(pady=10,padx=10)
            def change_color():
                current_color = box.cget("background")
                next_color = "orange" if current_color == "red" else "red"
                box.config(background=next_color, height="3", width="6")
                root.after(500, change_color)
                        
            box = tk.Text(self)
            box.pack()
            change_color()

            ser = serial.Serial(
                port = 'COM6',
                baudrate = 9600,
             )
            
            ser.write(0)
            
        button = tk.Button(self, text="Temperatuur diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(TempPage))
        button.pack()

        button2 = tk.Button(self, text="Uitrol aanpassen", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(RollOut))
        button2.pack(pady=18)

        label = tk.Label(self, text="Rolluik control, omhoog of omlaag. \nKlik op de knop om het rolluik te besturen ", font=('Helvetica', 12))
        label.pack(pady=10,padx=10)
        
        button3 = tk.Button(self, text="⬆", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Helvetica', 20), command=upwards)
        button3.pack(pady=1)

        button4 = tk.Button(self, text="⬇", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Helvetica', 20), command=downwards)
        button4.pack(pady=1)
            
       #Kijken of Arduino in COM-poort is geplugged
        try:
            ser = serial.Serial("COM7", 9600)

            if ser.read():

                '''temperatuur = []

                arduinoString = ser.readline()#lees arduino output waarde

                temp = float (arduinoString) #string naar float
                temperatuur.append(temp)#temperatuur array

                labelt = tk.Label(self, text="Het is momenteel {} °C".format(temp), font=('Helvetica', 10))
                labelt.pack(pady=10,padx=10)'''
                    
                label = tk.Label(self, text="Arduino gevonden", font=('Helvetica', 10))
                label.pack(pady=10,padx=10)
                
            else:
                label3 = tk.Label(self, text="USB losgekoppeld", font=('Helvetica', 10))
                label3.pack(pady=10,padx=10)

        except serial.serialutil.SerialException:
            label = tk.Label(self, text="", font=('Helvetica', 10))
            label.pack(pady=10,padx=10)

# Temperatuursensor GUI
class TempPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Temperatuur pagina", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        # Temperatuur grafiek
        def temperatuur():
            
            arduinoData = serial.Serial(
                    port = 'COM7',
                    baudrate = 9600,
                    ) #connectie met COM3 met

            #plt.ion() #live data
            temperatuur = []

            def figuur(): #functie figuur aanmaken
                    plt.ylim(-35,35)#geen dynamische Y-as maar met vast waardes 18-25
                    plt.title('Temperatuur sensor') #titel boven temperatuur sensor
                    plt.ylabel('Temperatuur in Celsius') #Y-as temperatuur in Celsius
                    plt.xlabel('Aantal metingen')#X-as aantal metingen
                    plt.plot(temperatuur, 'bo-') #blauw + stippen
                    plt.plot(temperatuur, 'bo-', label ="Celsius") #label "Celsius"
                    plt.legend(loc='upper right')#locatie van label(Celisus) rechtsboven 

            while True: 
                    while (arduinoData.inWaiting()==0):     #wachten op temperatuur
                            pass #oneindige loop
                    arduinoString = arduinoData.readline()#lees arduino output waarde
                    temp = float (arduinoString) #string naar float
                    temperatuur.append(temp)#temperatuur array
                    drawnow(figuur)#functie maken
                    plt.pause(3.0) # 3 seconden

        button = tk.Button(self, text="Terug naar het beginscherm", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = tk.Button(self, text="Uitrol aanpassen", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(RollOut))
        button2.pack(pady=18)

        # Kijken of Arduino in COM-poort is geplugged
        try:
            ser = serial.Serial("COM7", 9600, timeout=1000)
            
            button3 = tk.Button(self, text="Open temperatuur grafiek", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
            command=temperatuur)
            button3.pack(pady=18)

        except serial.serialutil.SerialException:
            label = tk.Label(self, text="Geen Arduino gevonden, koppel de Ardunio \n in de USB poort om data uit te lezen.", font=('Helvetica', 10))
            label.pack(pady=10,padx=10) 

# Lichtsensor GUI
class RollOut(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pas de uitrol van het zonnescherm aan", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Terug naar het beginscherm", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = tk.Button(self, text="Temperatuur diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(TempPage))
        button2.pack(pady=18)

        def getDate():
            labelt = tk.Label(self, text="De nieuwe uitroltijd is {} seconden".format(E3.get()), font=('Helvetica', 10))
            labelt.pack(pady=10,padx=10)

        label3 = tk.Label(self, text="Tijd (in seconden)")
        E3 = tk.Entry(self, bd =5)
        submit = tk.Button(self, text ="Submit", command = getDate)
        label3.pack()
        E3.pack()
        submit.pack()

root = MainWindow()
root.mainloop()
