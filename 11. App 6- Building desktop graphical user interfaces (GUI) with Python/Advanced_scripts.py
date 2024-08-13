from tkinter import Tk, StringVar, Entry, Button, Text, Label, END, messagebox

class KmToMilesConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Km to Miles Converter")
        
        self.e1_values = StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Input Label
        self.label_input = Label(self.master, text="Enter km:")
        self.label_input.grid(row=0, column=0, padx=10, pady=10)
        
        # Entry widget
        self.e1 = Entry(self.master, textvariable=self.e1_values)
        self.e1.grid(row=0, column=1, padx=10, pady=10)
        
        # Button
        self.b1 = Button(self.master, text="Convert", command=self.km_to_miles)
        self.b1.grid(row=0, column=2, padx=10, pady=10)
        
        # Output Label
        self.label_output = Label(self.master, text="Miles:")
        self.label_output.grid(row=1, column=0, padx=10, pady=10)
        
        # Text widget for output
        self.t1 = Text(self.master, height=1, width=20)
        self.t1.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
    def km_to_miles(self):
        try:
            km = float(self.e1_values.get())
            miles = km * 0.621371
            self.clear_output()
            self.t1.insert(END, f"{miles:.2f}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
    
    def clear_output(self):
        self.t1.delete('1.0', END)

if __name__ == "__main__":
    window = Tk()
    converter = KmToMilesConverter(window)
    window.mainloop()
