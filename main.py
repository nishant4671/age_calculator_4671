from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def days_until_birthday(birth_date):
    today = datetime.today()
    next_birthday = datetime(today.year, birth_date.month, birth_date.day)
    
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
    
    return (next_birthday - today).days

def main():
    print("=== Age Calculator ===")
    while True:
        try:
            year = int(input("Enter your birth year (YYYY): "))
            month = int(input("Enter your birth month (MM): "))
            day = int(input("Enter your birth day (DD): "))
            
            birth_date = datetime(year, month, day)
            today = datetime.today()
            
            if birth_date > today:
                print("Error: Birth date cannot be in the future.\n")
                continue  # Restart the loop
            
            age = calculate_age(birth_date)
            days_left = days_until_birthday(birth_date)
            
            print(f"\nYou are {age} years old.")
            print(f"Days until your next birthday: {days_left}\n")
            break  # Exit loop on success
            
        except ValueError:
            print("Error: Invalid date (e.g., February 30th or non-numbers).\n")
            