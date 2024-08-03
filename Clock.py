import tkinter as ui
import time

# Create the main window
window = ui.Tk()
window.title("Digital Clock")

# Function to update the clock
def update_clock():
    print("Updating clock...")
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_pm
    digital_clock_label.config(text=time_text)
    digital_clock_label.after(1000, update_clock)

# Create and pack the label to display the clock
digital_clock_label = ui.Label(window, text="00:00:00", font="Helvetica 72 bold")
digital_clock_label.pack()

# Initialize the clock update
update_clock()

# Start the Tkinter main loop
window.mainloop()

