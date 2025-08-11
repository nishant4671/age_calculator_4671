import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator Pro")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Create modern theme
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"))
        
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Date picker
        ttk.Label(main_frame, text="Select your birth date:").pack(pady=10)
        self.date_frame = ttk.Frame(main_frame)
        self.date_frame.pack(pady=5)
        
        # Day dropdown
        ttk.Label(self.date_frame, text="Day:").grid(row=0, column=0, padx=5)
        self.day_var = tk.StringVar()
        day_combo = ttk.Combobox(self.date_frame, textvariable=self.day_var, width=3)
        day_combo['values'] = [str(i).zfill(2) for i in range(1, 32)]
        day_combo.grid(row=0, column=1, padx=5)
        
        # Month dropdown
        ttk.Label(self.date_frame, text="Month:").grid(row=0, column=2, padx=5)
        self.month_var = tk.StringVar()
        month_combo = ttk.Combobox(self.date_frame, textvariable=self.month_var, width=10)
        month_combo['values'] = ["January", "February", "March", "April", "May", "June", 
                                "July", "August", "September", "October", "November", "December"]
        month_combo.grid(row=0, column=3, padx=5)
        
        # Year dropdown
        ttk.Label(self.date_frame, text="Year:").grid(row=0, column=4, padx=5)
        self.year_var = tk.StringVar()
        year_combo = ttk.Combobox(self.date_frame, textvariable=self.year_var, width=5)
        year_combo['values'] = [str(i) for i in range(1900, datetime.now().year + 1)]
        year_combo.grid(row=0, column=5, padx=5)
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate Age", command=self.calculate).pack(pady=20)
        
        # Results display
        self.result_frame = ttk.LabelFrame(main_frame, text="Results")
        self.result_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(self.result_frame, text="Your current age:").pack(anchor='w', padx=10, pady=5)
        self.age_label = ttk.Label(self.result_frame, text="", font=("Arial", 12, "bold"))
        self.age_label.pack(anchor='w', padx=10, pady=2)
        
        ttk.Label(self.result_frame, text="Days until next birthday:").pack(anchor='w', padx=10, pady=5)
        self.days_label = ttk.Label(self.result_frame, text="", font=("Arial", 12, "bold"))
        self.days_label.pack(anchor='w', padx=10, pady=2)
        
        # Auto-fill current date
        today = datetime.now()
        self.day_var.set(str(today.day).zfill(2))
        self.month_var.set(today.strftime("%B"))
        self.year_var.set(str(today.year))
    
def calculate(self):
    try:
        month_str = self.month_var.get()
        month_num = datetime.strptime(month_str, "%B").month  # Convert month name to number
        birth_date = datetime(
            year=int(self.year_var.get()),
            month=month_num,
            day=int(self.day_var.get())
        ).date()  # Convert to date object
        
        today = datetime.now().date()
        
        # Validate date
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
            
        # Calculate age
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        # Calculate days until next birthday
        next_birthday = datetime(today.year, birth_date.month, birth_date.day).date()
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day).date()
        days_left = (next_birthday - today).days
        
        # Update UI
        self.age_label.config(text=f"{age} years")
        self.days_label.config(text=f"{days_left} days")
        
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid date: {str(e)}")