import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator Pro")
        self.root.geometry("400x300")
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Date selection
        ttk.Label(main_frame, text="Select your birth date:").pack()
        
        date_frame = ttk.Frame(main_frame)
        date_frame.pack(pady=10)
        
        # Day
        ttk.Label(date_frame, text="Day:").grid(row=0, column=0, padx=5)
        self.day = ttk.Combobox(date_frame, width=3, values=[str(i).zfill(2) for i in range(1, 32)])
        self.day.grid(row=0, column=1, padx=5)
        self.day.set("01")
        
        # Month
        ttk.Label(date_frame, text="Month:").grid(row=0, column=2, padx=5)
        self.month = ttk.Combobox(date_frame, width=10, values=["January", "February", "March", "April", "May", "June", 
                                                              "July", "August", "September", "October", "November", "December"])
        self.month.grid(row=0, column=3, padx=5)
        self.month.set("January")
        
        # Year
        ttk.Label(date_frame, text="Year:").grid(row=0, column=4, padx=5)
        self.year = ttk.Combobox(date_frame, width=5, values=[str(i) for i in range(1900, datetime.now().year + 1)])
        self.year.grid(row=0, column=5, padx=5)
        self.year.set("2000")
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate Age", command=self.calculate).pack(pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(main_frame, text="Results", padding=10)
        result_frame.pack(fill=tk.X)
        
        ttk.Label(result_frame, text="Your current age:").pack(anchor=tk.W)
        self.age_result = ttk.Label(result_frame, text="", font=("Arial", 10, "bold"))
        self.age_result.pack(anchor=tk.W)
        
        ttk.Label(result_frame, text="Days until next birthday:").pack(anchor=tk.W, pady=(5,0))
        self.days_result = ttk.Label(result_frame, text="", font=("Arial", 10, "bold"))
        self.days_result.pack(anchor=tk.W)
    
    def calculate(self):
        try:
            # Get selected date
            day = int(self.day.get())
            month = datetime.strptime(self.month.get(), "%B").month
            year = int(self.year.get())
            
            birth_date = datetime(year, month, day)
            today = datetime.now()
            
            # Validate date
            if birth_date > today:
                messagebox.showerror("Error", "Birth date cannot be in the future!")
                return
            
            # Calculate age
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            
            # Calculate days until next birthday
            next_bday = datetime(today.year, birth_date.month, birth_date.day)
            if today > next_bday:
                next_bday = datetime(today.year + 1, birth_date.month, birth_date.day)
            days_left = (next_bday - today).days
            
            # Update results
            self.age_result.config(text=f"{age} years")
            self.days_result.config(text=f"{days_left} days")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()