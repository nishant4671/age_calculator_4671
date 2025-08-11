import os
import sys

def build():
    # Clean previous builds
    os.system("rmdir /s /q build 2> nul")
    os.system("rmdir /s /q dist 2> nul")
    
    # Build command
    cmd = f'"{sys.executable}" -m PyInstaller --onefile --windowed --name AgeCalculatorPro age_calculator.py'
    os.system(cmd)
    
    print("\n✅ Executable created in 'dist' folder!")
    print("➡️  File: dist\\AgeCalculatorPro.exe")

if __name__ == "__main__":
    build()