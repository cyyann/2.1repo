import tkinter as tk

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="Maak uw keuze")
        self.label.pack(side="top", padx=10, pady=10)
        self.button = tk.Button(self, text="Temperatuur diagram", 
                                command=self.create_window)
        self.button.pack(side="top", padx=100, pady=10)
        self.button2 = tk.Button(self, text="lichtsensor diagram", 
                                command=self.create_window2)
        self.button2.pack(side="top", padx=100, pady=10)

    # Temperatuursensor GUI
    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Temperatuur diagram")
        l = tk.Label(t, text="Temperatuurdiagram komt hier")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


    # Lichtsensor GUI
    def create_window2(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Lichtsensor diagram")
        l = tk.Label(t, text="Lichtsensor komt hier")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Project GUI")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
