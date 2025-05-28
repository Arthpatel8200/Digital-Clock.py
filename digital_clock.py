import tkinter as tk
from time import strftime

# Function to update time every second
def time():
    current_time = strftime('%H:%M:%S %p')  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every 1000ms = 1s

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Create and style the label
label = tk.Label(root, font=('Arial', 60), background='black', foreground='cyan')
label.pack(anchor='center')

# Call the time function once to initiate
time()

# Run the application
root.mainloop()
