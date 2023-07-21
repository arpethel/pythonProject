# main.py
import tkinter as tk
from tkinter import ttk
from speech_to_text import SpeechToText

class App:
    def __init__(self, root):
        self.speech_to_text = SpeechToText()

        self.root = root
        self.root.title("Speech-to-Text App")

        # Create a 'Start Recording' button
        start_button = ttk.Button(root, text="Start Recording", command=self.speech_to_text.start_recording)
        start_button.pack()

        # Create a 'Stop Recording and Generate Response' button
        stop_and_respond_button = ttk.Button(root, text="Stop Recording and Generate Response", command=self.stop_and_respond)
        stop_and_respond_button.pack()

        # Create a text area for the transcript
        self.response_text = tk.Text(root)
        self.response_text.pack()

    def stop_and_respond(self):
        self.speech_to_text.stop_recording_and_transcribe()
        self.display_response()

    def display_response(self):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, self.speech_to_text.generate_response())

# Create the main window
root = tk.Tk()
app = App(root)

# Run the main loop
root.mainloop()
