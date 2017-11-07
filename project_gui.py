# Versie 1.2
# Door Misha Dokter
# Datum: 01-11-'17
# Verschil met V1.1: Classes om 1 dezelfde GUI te houden ipv verschillende GUI's met DEF (functions)

import matplotlib # matplotlib = voor graphs
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk # tkinter importen
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)


        tk.Tk.wm_title(self, "Project GUI")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TempPage, LightPage):

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

        button = tk.Button(self, text="Temperatuur diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(TempPage))
        button.pack()

        button2 = tk.Button(self, text="Lichtsensor diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(LightPage))
        button2.pack(pady=18)

# Temperatuursensor GUI
class TempPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Temperatuurdiagram", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Terug naar het beginscherm", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = tk.Button(self, text="Lichtsensor diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(LightPage))
        button2.pack(pady=18)

        l = ttk.Label(self, text="Temperatuurdiagram komt hier")
        l.pack(pady=100)

# Lichtsensor GUI
class LightPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lichtsensor diagram", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Terug naar het beginscherm", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = tk.Button(self, text="Temperatuur diagram", bg='#01DF01', fg='#FFFFFF', relief='flat', bd=8, width=20, font=('Helvetica', 10),
                            command=lambda: controller.show_frame(TempPage))
        button2.pack(pady=18)

        l = ttk.Label(self, text="Lichtsensor diagram komt hier")
        l.pack()
        f = Figure(figsize=(5,5), dpi=100)
        plt = f.add_subplot(111)
        # Vooralsnog alleen testdata: Moet worden ingelezen vanuit Arduino results (to do)
        plt.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        plt.set_ylabel('Voltage', rotation=90, fontsize=10, labelpad=8)
        plt.set_xlabel('Uur', rotation=0, fontsize=10, labelpad=5)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

root = MainWindow()
root.mainloop()
        
