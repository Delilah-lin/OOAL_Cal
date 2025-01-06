from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime


def calculate_price(days, num_dogs, daycare_charge):
    if num_dogs == 1:
        if days < 15:
            return (days * 55) + daycare_charge
        elif days < 30:
            return (days * 50) + daycare_charge
        else:
            return (days * 45) + daycare_charge
    elif num_dogs == 2:
        return (days * 85) + daycare_charge
    elif num_dogs == 3:
        return (days * 110) + daycare_charge
    else:
        return 0  # Handle invalid cases


def get_selections():
    arrival_date = cal_arrival.get_date()
    arrival_hour = hour_arrival.get()
    arrival_minute = minute_arrival.get()
    arrival_period = period_arrival.get()
    arrival_time = f"{arrival_hour}:{arrival_minute} {arrival_period}"

    departure_date = cal_departure.get_date()
    departure_hour = hour_departure.get()
    departure_minute = minute_departure.get()
    departure_period = period_departure.get()
    departure_time = f"{departure_hour}:{departure_minute} {departure_period}"

    num_dogs = int(dogs_dropdown.get())

    date_format = "%Y-%m-%d"
    date_arrival = datetime.strptime(arrival_date, date_format)
    date_departure = datetime.strptime(departure_date, date_format)
    days_difference = (date_departure - date_arrival).days

    if days_difference <= 0:
        result_label.config(text="Error: Departure date must be after Arrival date.")
        return

    daycare_charge = 0
    additional_note = ""
    if arrival_period == "AM" and departure_period == "PM":
        if num_dogs == 1:
            daycare_charge = 30
        elif num_dogs == 2:
            daycare_charge = 50
        elif num_dogs == 3:
            daycare_charge = 65
        additional_note = f"Note: An additional daycare charge of ${daycare_charge} has been added.\n"

    total_price = calculate_price(days_difference, num_dogs, daycare_charge)

    result_label.config(
        text=(
            f"Arrival: {arrival_date} {arrival_time}\n"
            f"Departure: {departure_date} {departure_time}\n"
            f"Number of days between: {days_difference} day(s)\n"
            f"Number of dogs staying: {num_dogs}\n"
            f"{additional_note}"
            f"Total price: ${total_price:.2f}"
        )
    )


# Create the main Tkinter window
root = tk.Tk()
root.title("Out On A Leash Boarding Calculator v0.1")
# root.iconbitmap("ooal_icon.ico")

# Configure grid layout
root.grid_columnconfigure(0, weight=1)  # Left column
root.grid_columnconfigure(1, weight=1)  # Right column
root.grid_columnconfigure(2, weight=1)  # Center column

font_label = ("Arial", 14)
font_calendar = ("Arial", 12)
font_dropdown = ("Arial", 12)

# -------------------- Arrival Section --------------------
tk.Label(root, text="Arrival Date and Time", font=font_label).grid(row=0, column=0, pady=10)
cal_arrival = Calendar(
    root, selectmode='day', date_pattern='yyyy-mm-dd', showweeknumbers=False, font=font_calendar
)
cal_arrival.grid(row=1, column=0, padx=10, pady=10)

# Arrival Time
time_frame_arrival = tk.Frame(root)
time_frame_arrival.grid(row=2, column=0, pady=10)
hour_arrival = ttk.Combobox(time_frame_arrival, values=[f"{i:02}" for i in range(1, 13)], width=3)
hour_arrival.set("12")
hour_arrival.pack(side=tk.LEFT, padx=5)
minute_arrival = ttk.Combobox(time_frame_arrival, values=[f"{i:02}" for i in range(60)], width=3)
minute_arrival.set("00")
minute_arrival.pack(side=tk.LEFT, padx=5)
period_arrival = ttk.Combobox(time_frame_arrival, values=["AM", "PM"], width=5)
period_arrival.set("AM")
period_arrival.pack(side=tk.LEFT, padx=5)

# -------------------- Departure Section --------------------
tk.Label(root, text="Departure Date and Time", font=font_label).grid(row=0, column=1, pady=10)
cal_departure = Calendar(
    root, selectmode='day', date_pattern='yyyy-mm-dd', showweeknumbers=False, font=font_calendar
)
cal_departure.grid(row=1, column=1, padx=10, pady=10)

# Departure Time
time_frame_departure = tk.Frame(root)
time_frame_departure.grid(row=2, column=1, pady=10)
hour_departure = ttk.Combobox(time_frame_departure, values=[f"{i:02}" for i in range(1, 13)], width=3)
hour_departure.set("12")
hour_departure.pack(side=tk.LEFT, padx=5)
minute_departure = ttk.Combobox(time_frame_departure, values=[f"{i:02}" for i in range(60)], width=3)
minute_departure.set("00")
minute_departure.pack(side=tk.LEFT, padx=5)
period_departure = ttk.Combobox(time_frame_departure, values=["AM", "PM"], width=5)
period_departure.set("AM")
period_departure.pack(side=tk.LEFT, padx=5)

# -------------------- Dogs Selection and Submit Button --------------------
tk.Label(root, text="Number of Dogs", font=font_label).grid(row=3, column=0, columnspan=2, pady=10)
dogs_dropdown = ttk.Combobox(root, values=[str(i) for i in range(1, 4)], font=font_dropdown, width=3)
dogs_dropdown.set("1")
dogs_dropdown.grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(root, text="Calculate", font=font_label, command=get_selections).grid(row=5, column=0, columnspan=2, pady=20)

# -------------------- Result Display --------------------
result_label = tk.Label(root, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
