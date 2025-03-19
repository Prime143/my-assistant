import tkinter as tk
from tkinter import messagebox

# Function to handle input from the user (your assistant logic)
def ask_assistant():
    user_input = entry.get()  # Get user input from the entry field
    # Example response, replace with your assistant's logic
    response = f"You asked: {user_input}. Here is the answer!"
    messagebox.showinfo("Assistant Response", response)

# Setting up the main window
root = tk.Tk()
root.title("Digital Assistant")

# Create a label to prompt user
label = tk.Label(root, text="Ask your assistant:")
label.pack()

# Create an entry widget for user input
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to submit the query
ask_button = tk.Button(root, text="Ask", command=ask_assistant)
ask_button.pack()

# Start the app
root.mainloop()
