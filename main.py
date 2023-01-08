# Imports
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import _tkinter
import pytz
import requests
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


class Window:
    def __init__(self, window, master=None):
        # GUI Window configuration
        self.root = window
        self.root.config(bg="white")
        self.button_mode = True
        # Font Configuration
        self.leel_font = "Leelawadee UI Semilight"
        # API Key
        self.key = "d121ea79ad3e657a62c044116209ab75"
        # Dark theme
        self.dark_colour = "#26242f"
        # --------------------------------------------------------------------------------------------------------------
        # Functions
        '''
        1. get_weather()
        2. theme_custom()
        '''

        # Weather API Request (https://openweatherapi.org)
        def get_weather():
            try:
                # Time Zone
                city = text_field.get()

                # Geographic Divider...
                geolocator = Nominatim(user_agent="geoapiExercises")
                location = geolocator.geocode(city)
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

                # Time Zone Finder
                home = pytz.timezone(result)
                local_time = datetime.now(home)
                current_time = local_time.strftime("%I:%m %p")
                self.clock.config(text=current_time)


                # Weather
                api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}"

                # Weather API Request JSON format
                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = int(json_data['main']['temp'] - 273.15)
                wind = json_data['wind']['speed']
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                feels_like = int(json_data['main']['feels_like']-273.15)
                max_temp = int(json_data['main']['temp_max']-273.15)
                min_temp = int(json_data['main']['temp_min']-273.15)


                self.temp_label.config(text=(temp, "°"))
                self.cond_label.config(text=(condition, "|", "FEELS", "LIKE", feels_like, "°"))

                self.max_temp_label.config(text=f"MAX. TEMP: {max_temp}°")
                self.min_temp_label.config(text=f"MIN. TEMP: {min_temp}°")

                self.name.config(text="Weather At")

                # Lower Box Readings
                self.a.config(text=wind)
                self.b.config(text=humidity)
                self.c.config(text=description)
                self.d.config(text=pressure)
            except Exception as e:
                messagebox.showerror("Weather.IO", "Error 404 Not found...")

        # Changing UI Theme
        def theme_custom():
            if self.button_mode:
                self.theme_button.config(image=self.theme_image_dark_to_light, bg=self.dark_colour,
                                         activebackground=self.dark_colour)
                self.root.config(bg=self.dark_colour)
                self.weather_io_label.config(bg=self.dark_colour)

                self.max_temp_label.config(bg=self.dark_colour)
                self.min_temp_label.config(bg=self.dark_colour)

                self.terms_label.config(bg=self.dark_colour, fg="white")

                self.lower_box_label.config(bg=self.dark_colour)
                self.wind_label.config(bg="#049ED9", border=0)
                self.humidity_label.config(bg="#049ED9", border=0)
                self.description_label.config(bg="#049ED9", border=0)
                self.pressure_label.config(bg="#049ED9", border=0)
                self.a.config(bg="#049ED9", border=0)
                self.b.config(bg="#049ED9", border=0)
                self.c.config(bg="#049ED9", border=0)
                self.d.config(bg="#049ED9", border=0)

                self.weather_logo_label.config(bg=self.dark_colour, fg=self.dark_colour)

                self.search_bar_label.config(bg=self.dark_colour, fg="#404040")
                text_field.config(bg="#101010", fg="white")
                self.search_logo_button.config(bg="#101010")


                self.name.config(bg=self.dark_colour)
                self.clock.config(bg=self.dark_colour)

                self.temp_label.config(bg=self.dark_colour)
                self.cond_label.config(bg=self.dark_colour)

                self.watermark.config(bg=self.dark_colour, fg="white")

                self.button_mode = False
            else:
                self.theme_button.config(image=self.theme_image_light_to_dark, bg="white", activebackground="white")

                self.root.config(bg="white")

                self.weather_io_label.config(bg="white", activebackground="white")

                self.terms_label.config(bg="white", fg="black")

                self.max_temp_label.config(bg="white")
                self.min_temp_label.config(bg="white")

                self.lower_box_label.config(bg="white", activebackground="white")
                self.wind_label.config(bg="#1CB6F0", border=0)
                self.humidity_label.config(bg="#1CB6F0", border=0)
                self.description_label.config(bg="#1CB6F0", border=0)
                self.pressure_label.config(bg="#1CB6F0", border=0)
                self.a.config(bg="#1CB6F0", border=0)
                self.b.config(bg="#1CB6F0", border=0)
                self.c.config(bg="#1CB6F0", border=0)
                self.d.config(bg="#1CB6F0", border=0)

                self.weather_logo_label.config(bg="white", fg="white")

                self.search_bar_label.config(bg="white", fg="#101010")
                text_field.config(fg="white", bg="#404040")
                self.search_logo_button.config(bg="#404040", fg="#404040")

                self.name.config(bg="white")
                self.clock.config(bg="white")

                self.temp_label.config(bg="white")
                self.cond_label.config(bg="white")

                self.watermark.config(bg="white", fg=self.dark_colour)

                self.button_mode = True
        # --------------------------------------------------------------------------------------------------------------
        # Images
        '''
        1. Search box Image
        2. Search Button Image
        3. Weather Logo Image
        4. Light to Dark Mode
        5. Dark to Light Mode
        6. Weather info box Image
        '''
        try:
            # Search box Image
            self.search_box_image = Image.open("search.png")
            self.search_box_image = ImageTk.PhotoImage(self.search_box_image)

            # Search Button Image
            self.search_logo_image = Image.open("search_icon.png")
            self.search_logo_image = ImageTk.PhotoImage(self.search_logo_image)

            # Weather logo image
            # Light Mode
            self.weather_logo_image = Image.open("logo.png")
            self.weather_logo_image = ImageTk.PhotoImage(self.weather_logo_image)

            # Dark Mode
            self.weather_logo_image_dark = Image.open("logo dark.png")
            self.weather_logo_image_dark = ImageTk.PhotoImage(self.weather_logo_image_dark)

            # light to dark mode/dark to light mode button images
            "Light to Dark Mode"
            self.theme_image_light_to_dark = Image.open("dark.png")
            self.theme_image_light_to_dark = self.theme_image_light_to_dark.resize((107, 49), Image.Resampling.LANCZOS)
            self.theme_image_light_to_dark = ImageTk.PhotoImage(self.theme_image_light_to_dark)

            "Dark to Light Mode"
            self.theme_image_dark_to_light = Image.open("light.png")
            self.theme_image_dark_to_light = self.theme_image_dark_to_light.resize((107, 49), Image.Resampling.LANCZOS)
            self.theme_image_dark_to_light = ImageTk.PhotoImage(self.theme_image_dark_to_light)

            # Weather info box image
            self.lower_box_image = Image.open("box.png")
            self.lower_box_image = ImageTk.PhotoImage(self.lower_box_image)
        except _tkinter.TclError:
            print("image not found...Either moved or deleted...")

        # --------------------------------------------------------------------------------------------------------------
        # Labels
        '''
        1. Weather Logo Label
        2. Search Bar Label
        3. Weather IO Label
        4. Lower Box Label
        5. Wind Label
        6. Humidity Label
        7. Description Label
        8. Pressure Label
        9. a (Wind Speed Reading)
        10. b (Humidity Reading)
        11. c (Description Reading)
        12. d (Pressure Reading)
        13. name label
        14. clock label
        15. temp label
        16. cond. label
        17. Terms and conditions Label
        18. Watermark Label
        '''

        # 1. Weather Logo Label
        self.weather_logo_label = Label(self.root, image=self.weather_logo_image, bd=0, bg="white")
        self.weather_logo_label.place(x=150, y=200)

        # 2. Search Bar Label
        self.search_bar_label = Label(self.root, image=self.search_box_image, bd=0, bg="white")
        self.search_bar_label.place(x=500, y=20)

        # Weather IO Label
        self.weather_io_label = Label(self.root, text="WEATHER.IO", bd=0, font=(self.leel_font, 47),
                                      fg="orange", bg="white")
        self.weather_io_label.place(x=20, y=15)

        self.max_temp_label = Label(self.root, text="", font=(self.leel_font, 29), bg="white", fg="red")
        self.max_temp_label.place(x=220, y=540)

        self.min_temp_label = Label(self.root, text="", font=(self.leel_font, 29), bg="white", fg="blue")
        self.min_temp_label.place(x=540, y=540)

        # Lower Box Label
        self.lower_box_label = Label(self.root, image=self.lower_box_image, bd=0, bg="white")
        self.lower_box_label.pack(padx=10, pady=10, side=BOTTOM)

        # Wind Speed Label
        self.wind_label = Label(self.root, text="WIND(knots)", font=(self.leel_font, 15), bg="#1ab5ef", bd=0,
                                fg="white")
        self.wind_label.place(x=220, y=620)

        # Humidity Percentage Label
        self.humidity_label = Label(self.root, text="HUMIDITY(%)",
                                    font=(self.leel_font, 15), bg="#1ab5ef", bd=0, fg="white")
        self.humidity_label.place(x=370, y=620)

        # Description Label
        self.description_label = Label(self.root, text="DESCRIPTION",
                                       font=(self.leel_font, 15), bg="#1ab5ef", bd=0, fg="white")
        self.description_label.place(x=540, y=620)

        # Pressure Label
        self.pressure_label = Label(self.root, text="PRESSURE(hPa)", font=(self.leel_font, 15),
                                    bg="#1ab5ef", bd=0, fg="white")
        self.pressure_label.place(x=760, y=620)

        # Wind Speed Reading
        self.a = Label(self.root, text="...", bd=0, fg="white", bg="#1ab5ef", font=(self.leel_font, 20), border=0)
        self.a.place(x=230, y=645)

        # Humidity Reading
        self.b = Label(self.root, text="...", bd=0, fg="white", bg="#1ab5ef", font=(self.leel_font, 20), border=0)
        self.b.place(x=400, y=645)

        # Description Text
        self.c = Label(self.root, text="", bd=0, fg="white", bg="#1ab5ef", font=(self.leel_font, 20), border=0)
        self.c.place(x=530, y=645)

        # Pressure Reading
        self.d = Label(self.root, text="...", bd=0, fg="white", bg="#1ab5ef", font=(self.leel_font, 20), border=0)
        self.d.place(x=790, y=645)

        # Name Label
        self.name = Label(self.root, font=(self.leel_font, 15), bg="white", fg="red")
        self.name.place(x=30, y=100)

        # Clock Label Tells Time
        self.clock = Label(self.root, font=(self.leel_font, 20), bg="white", fg="red")
        self.clock.place(x=30, y=130)

        # Temperature Reading
        self.temp_label = Label(self.root, font=(self.leel_font, 100, "bold"), fg="#ee666d", bg="white")
        self.temp_label.place(x=600, y=250)

        # Condition Reading
        self.cond_label = Label(self.root, font=(self.leel_font, 35), fg="#1d75d6", bg="white")
        self.cond_label.place(x=450, y=400)

        # Terms & Conditions
        self.terms_label = Label(self.root, text="Weather and Time updates 30 minutes to 1 hour before...",
                                 font=(self.leel_font, 12, "italic"), bg="white", fg="black")
        self.terms_label.place(x=540, y=90)

        # Watermark Logo
        self.watermark = Label(self.root, text="@aatti", font=(self.leel_font, 7, "bold"), bg="white", fg="black")
        self.watermark.place(x=1035, y=700)

        # --------------------------------------------------------------------------------------------------------------
        # Text Fields
        # For entering city...

        text_field = Entry(self.root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0,
                           fg="white")
        text_field.place(x=550, y=40)
        text_field.focus()
        # --------------------------------------------------------------------------------------------------------------
        # Buttons
        "Search Button"
        self.search_logo_button = Button(self.root, image=self.search_logo_image, bd=0, cursor="hand2", bg="#404040",
                                         command=get_weather)
        self.search_logo_button.place(x=880, y=30)

        "ThemeChange Button"
        self.theme_button = Button(self.root, image=self.theme_image_light_to_dark, bd=0, bg="white",
                                   activebackground="white", command=theme_custom)
        self.theme_button.place(x=30, y=650)


if __name__ == "__main__":
    window = Tk()
    x = Window(window)
    window.title("Weather.io")
    window.iconbitmap("icon.ico")
    window.geometry("1080x720+300+100")
    window.resizable(False, False)
    window.mainloop()
