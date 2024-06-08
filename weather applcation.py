import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

# Function to get real-time weather data
def get_weather(city):
    try:
        # URL to scrape weather data (example: "https://www.weather-forecast.com/")
        url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting weather information
        weather = soup.find('span', class_='phrase').text
        return weather
    except Exception as e:
        return "Error retrieving weather data"

# Function to display weather
def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        weather_label.config(text=weather)
    else:
        messagebox.showerror("Input Error", "Please enter a city name.")

# Creating the main window
root = Tk()
root.title("Real Time Weather Application")
root.geometry("400x300")
root.config(bg="lightblue")

# Adding widgets
title = Label(root, text="Real Time Weather", font=("Arial", 20, "bold"), bg="lightblue")
title.pack(pady=20)

city_label = Label(root, text="Enter City Name:", font=("Arial", 12), bg="lightblue")
city_label.pack(pady=5)

city_entry = Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

get_weather_btn = Button(root, text="Get Weather", font=("Arial", 12, "bold"), command=show_weather)
get_weather_btn.pack(pady=10)

weather_label = Label(root, text="", font=("Arial", 12), bg="lightblue")
weather_label.pack(pady=20)

# Running the application
root.mainloop()