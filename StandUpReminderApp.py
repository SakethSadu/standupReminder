import tkinter as tk
from tkinter import messagebox
import threading
import time

class StandUpReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title ("Stand UP Reminder")

        self.running = False
        self.thread = None

        self.start_button = tk.Button(root, text="Start", command=self.start_reminder)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text = "Stop", command=self.stop_reminder)
        self.stop_button.pack(pady=10)

    def reminder_loop(self):
        while self.running:
            time.sleep(3600)
            if self.running:
                messagebox.showinfo("Reminder",  "Time to Stand up and Stretch")

    
    def start_reminder(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.reminder_loop)
            self.thread.start()
            messagebox.showinfo("Info", "Reminder Started. You will be reminded every one hour")
    
    def stop_reminder(self):
        if self.running:
            self.running = False
            self.thread.join()
            messagebox.showinfo("Info", "Reminder Stopped")

    
if __name__ == "__main__":   

    root = tk.Tk()
    app = StandUpReminderApp(root)
    root.mainloop()

