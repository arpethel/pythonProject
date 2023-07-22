# main.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from speech_to_text import SpeechToText

class App:
    def __init__(self, root):
        self.speech_to_text = SpeechToText()
        self.is_recording = False

        self.root = root
        self.root.title("Speech-to-Text App")

        # Load the images and resize them
        record_img = Image.open("assets/microphone.png")
        record_img = record_img.resize((15, 15), Image.LANCZOS)
        self.record_img = ImageTk.PhotoImage(record_img)

        eye_img = Image.open("assets/eye.png")
        eye_img = eye_img.resize((15, 15), Image.LANCZOS)
        self.eye_img = ImageTk.PhotoImage(eye_img)

        clear_img = Image.open("assets/clear.png")
        clear_img = clear_img.resize((15, 15), Image.LANCZOS)
        self.clear_img = ImageTk.PhotoImage(clear_img)

        # Create a 'Start Recording' button
        self.recording_button = ttk.Button(root, image=self.record_img, command=self.toggle_recording)
        self.recording_button.grid(column=0, row=0)

        # Create a 'Clear' button
        self.clear_button = ttk.Button(root, image=self.clear_img, command=self.clear_text)
        self.clear_button.grid(column=0, row=1)

        # Create a text area for the transcript
        self.response_text = tk.Text(root)
        self.response_text.grid(column=1, row=0, rowspan=2, sticky='nsew')

        # Configure the grid
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

    def toggle_recording(self):
        if self.is_recording:
            self.speech_to_text.stop_recording_and_transcribe()
            self.display_response()
            self.recording_button['image'] = self.record_img
        else:
            self.speech_to_text.start_recording()
            self.recording_button['image'] = self.eye_img
        self.is_recording = not self.is_recording

    def display_response(self):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, self.speech_to_text.generate_response())

    def clear_text(self):
        self.response_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
app = App(root)

# Run the main loop
root.mainloop()
