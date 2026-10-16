"""
Developer: Kelson Glaeske
Creation Date: 21/05/2026
version: 0
name: isc_clock_app.py
Purpose: Clock app that tells ISC time.
"""

import tkinter as tk
from isc_time import ISCTime, timestamp_to_isc_date, format_isc_date, get_deekday, get_current_deekday

class ISCClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interspace Standard Calendar Clock")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Create a frame for better organization
        self.frame = tk.Frame(root, bg="#1a1a1a")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create labels for different parts of the display
        self.date_label = tk.Label(
            self.frame,
            font=("Arial", 14),
            pady=5,
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.date_label.pack()

        self.time_label = tk.Label(
            self.frame,
            font=("Arial", 18, "bold"),
            pady=5,
            bg="#1a1a1a",
            fg="#00ff00"
        )
        self.time_label.pack()

        self.info_label = tk.Label(
            self.frame,
            font=("Arial", 10),
            pady=5,
            bg="#1a1a1a",
            fg="#cccccc"
        )
        self.info_label.pack()

        # Add a timestamp label
        self.timestamp_label = tk.Label(
            self.frame,
            font=("Courier", 9),
            pady=5,
            bg="#1a1a1a",
            fg="#888888"
        )
        self.timestamp_label.pack()

        # Start the clock
        self.update_clock()

    def update_clock(self):
        # Get current ISC time
        current_isc_time = ISCTime.now()
        current_isc_date = timestamp_to_isc_date(current_isc_time.seconds_since_epoch)
        current_deekday = get_current_deekday()  # Use the new function!

        # Update the display
        self.date_label.config(
            text=f"{current_deekday}, {current_isc_date['day']} {current_isc_date['month_name']} {current_isc_date['year']}"
        )

        self.time_label.config(
            text=f"{current_isc_date['hour']:02d}:{current_isc_date['minute']:02d}:{current_isc_date['second']:02d}"
        )

        # Color code the work/leisure status
        if current_isc_date['day_of_deek'] >= 6:  # Dekend (weekend)
            status_text = f"Deek {current_isc_date['deek']}, Day {current_isc_date['day_of_deek']+1}/10 | DEKEND"
            status_color = "#00aaff"  # Blue for weekend
        else:  # Deekday (work day)
            status_text = f"Deek {current_isc_date['deek']}, Day {current_isc_date['day_of_deek']+1}/10 | DEEKDAY"
            status_color = "#ffaa00"  # Orange for work day

        self.info_label.config(text=status_text, fg=status_color)

        self.timestamp_label.config(
            text=f"ISC Timestamp: {current_isc_time.seconds_since_epoch}"
        )

        # Schedule the next update in 1000ms (1 second)
        self.root.after(1000, self.update_clock)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ISCClockApp(root)
    root.mainloop()
