import tkinter as tk  # GUI module
from FileOrg import organize_files  # Importing the file organization function

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x250")  # Set the window size

# Define color scheme
bg_color = "#2c3e50"  # Background color
text_color = "#ecf0f1"  # Text color
button_color = "#1abc9c"  # Button color
button_hover_color = "#16a085"  # Button hover color
entry_bg_color = "#34495e"  # Entry background color
entry_fg_color = "#ecf0f1"  # Entry text color

# Function to be called when the button is clicked
def buttonCall():
    address = entry.get()  # Get text from the entry box
    if address:
        organize_files(address)  # Call the file organization function
    else:
        print("No directory path entered!")

# Configure the window with a background color
root.config(bg=bg_color)

# Label for user input
label = tk.Label(root, text="Please Enter Directory Address:", font=("Helvetica", 15), padx=10, pady=5, bg=bg_color, fg=text_color)
label.pack(pady=10)  # Add padding around the label

# Entry (input field) where user can type the directory path
entry = tk.Entry(root, width=40, font=("Helvetica", 12), borderwidth=2, relief="groove", bg=entry_bg_color, fg=entry_fg_color)
entry.pack(pady=5)  # Add padding around the entry field

# Button to trigger the function
button = tk.Button(root, text="Submit", command=buttonCall, font=("Helvetica", 12), padx=10, pady=5, bg=button_color, fg=text_color, activebackground=button_hover_color)
button.pack(pady=10)  # Add padding around the button

# Start the GUI event loop
root.mainloop()
