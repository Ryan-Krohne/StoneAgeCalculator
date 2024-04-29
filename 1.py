from tkinter import Tk, Button, Label

# Initialize the number and window
number = 0
window = Tk()
window.title("Number Overlay")

# Set window attributes for overlay
# Set window attributes for on-top overlay with no border or title bar
window.overrideredirect(True)
window.attributes('-topmost', True)
window.attributes('-fullscreen', False)  # Remove for non-fullscreen window



# Create the label for displaying the number
number_label = Label(window, text=str(number), font=("Arial", 50))
number_label.pack()

# Function to increment the number
def increment():
  global number
  number += 1
  number_label.config(text=str(number))

# Function to decrement the number
def decrement():
  global number
  if number > 0:
    number -= 1
  number_label.config(text=str(number))

# Create the buttons
plus_button = Button(window, text="+", command=increment)
plus_button.pack(side="right")

minus_button = Button(window, text="-", command=decrement)
minus_button.pack(side="left")

# Run the main event loop
window.mainloop()
