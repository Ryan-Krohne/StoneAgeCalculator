import tkinter as tk

def read_version_info():
    try:
        with open("version.txt", "r") as file:
            version_info = file.read()
            # Extract version number from the file content
            version_number = version_info.strip().split("=")[1]
            return version_number
    except FileNotFoundError:
        return "Version information not available"

def close_window(event=None):
    window.destroy()

def start_drag(event):
    global x, y
    x, y = event.x, event.y

def drag_window(event):
    window.geometry(f"+{event.x_root - x}+{event.y_root - y}")

# Create a Tkinter window
window = tk.Tk()
window.title("App Version")

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size
window_width = 300
window_height = 150

# Calculate window position to center it on the screen
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Read version information
version_info = read_version_info()

# Create a label to display version information
version_label = tk.Label(window, text="Version: " + version_info)
version_label.pack(pady=20)

# Add an 'X' button to close the window
close_button = tk.Label(window, text="X", font=("Arial", 12), bg="red", fg="white")
close_button.place(relx=1, y=0, anchor="ne")
close_button.bind("<Button-1>", close_window)

# Bind mouse events for window dragging
window.bind("<ButtonPress-1>", start_drag)
window.bind("<B1-Motion>", drag_window)

# Make the window borderless
window.overrideredirect(True)

# Run the main event loop
window.mainloop()
