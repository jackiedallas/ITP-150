"""
cold_weather.py
@author: Jackie Johnson-Dallas
"""


import textwrap


class WeatherReport:
    """Represents a weather report"""

    def __init__(self, air_temp, wind_speed, region):
        self.region = region
        self.air_temp = air_temp
        self.wind_speed = wind_speed

    def get_wind_chill(self):
        """method to get the wind chill"""
        return 35.74 + (0.6215 * self.air_temp) - \
            (35.75 * (self.wind_speed**0.16)) + \
            ((0.4275 * self.air_temp) * (self.wind_speed**0.16))

    def format_wind_chill(self):
        """method to format wind chill"""
        formatted_wind_chill = float(self.get_wind_chill()).__format__('.1f')
        return f"{formatted_wind_chill}°F"

    def format_air_temp(self):
        """method to format air temperature"""
        formatted_air_temp = float(self.air_temp).__format__('.1f')
        return f"{formatted_air_temp}°F"

    def format_wind_speed(self):
        """method to format wind speed"""
        formatted_wind_speed = float(self.wind_speed).__format__('.1f')
        return f"{formatted_wind_speed} mph"

    def get_advisory(self):
        """Issue an advisory based on wind chill and air temperature."""
        cold_eb = "Cold Weather Advisory Issued East of Blue Ridge"
        xcold_eb = "Extreme Cold Weather Advisory Issued East of Blue Ridge"
        cold_bw = "Cold Weather Advisory Issued Blue Ridge and West"
        xcold_bw = "Extreme Cold Weather Advisory Issued Blue Ridge and West"
        width = 50
        x_width = 42
        if self.region == 'e':
            if (self.air_temp < 0
                    and self.air_temp > -9) or \
                    (float(self.get_wind_chill()) < 0
                        and float(self.get_wind_chill()) > -9):
                section_1 = cold_eb[:29]
                section_2 = cold_eb[29:]
                return f"{section_1}{section_2:>{width}}"
            elif self.air_temp < -10 or float(self.get_wind_chill()) < -10:
                section_1 = xcold_eb[:37]
                section_2 = xcold_eb[37:]
                return f"{section_1}{section_2:>{x_width}}"
            else:
                return "No Cold Weather Advisory or Extreme Weather Warning"
        if self.region == 'w':
            if (self.air_temp < -10
                and self.air_temp > -19) or \
                (float(self.get_wind_chill()) < -10
                    and float(self.get_wind_chill()) > -19):
                section_1 = cold_bw[:29]
                section_2 = cold_bw[29:]
                return f"{section_1}{section_2:>{width}}"
            elif self.air_temp < -20 or float(self.get_wind_chill()) < -20:
                section_1 = xcold_bw[:37]
                section_2 = xcold_bw[37:]
                return f"{section_1}{section_2:>{x_width}}"
            else:
                return "No Cold Weather Advisory or Extreme Weather Warning"


report_prompt = "Please enter a number of reports: "


# validate reports are more than zero
valid_reports = False
while not valid_reports:

    try:
        reports = int(input(report_prompt))
        if reports > 0:
            valid_reports = True
        else:
            print("Number of reports must be greater than zero.")

    except ValueError:
        print("❌ Invalid input! You must enter an integer.")


# if the reports are valid use a for loop to create as many objects as reports
if valid_reports:

    # initialize dictionary for weather report objects
    instances = {}

    # use for loop with a range of the amount of reports they want to generate
    for i in range(reports):
        # prompts to get user inputs
        region_prompt = textwrap.dedent(f"""
        Please enter your region from the menu below for Report {i+1}:
        E for East of the Blue Ridge Mountains:
        W for West of the Blue Ridge Mountains:\n
        """)
        air_temp_prompt = textwrap.dedent(f"""
        Please enter the air temperature for Report {i+1}, 50 or less:
        """)
        wind_speed_prompt = textwrap.dedent(f"""
        Please enter the wind speed for Report {i+1}, should be at least 3:
        """)

        # create while loop to make sure information entered is valid
        valid_info = False
        while not valid_info:
            # Initialize variables
            air_temp = None
            wind_speed = None
            region = None

            # Validate air temperature
            while air_temp is None:
                try:
                    air_temp = int(input(air_temp_prompt))
                    if air_temp > 50:
                        print("Air Temperature must be 50°F or less.")
                        air_temp = None  # Reset to force prompt again
                except ValueError:
                    print("❌ Invalid input! "
                          "Please enter an integer for air temperature.")

            # Validate wind speed
            while wind_speed is None:
                try:
                    wind_speed = int(input(wind_speed_prompt))
                    if wind_speed < 3:
                        print("Wind Speed must be at least 3 mph.")
                        wind_speed = None  # Reset to force prompt again
                except ValueError:
                    print("❌ Invalid input! "
                          "Please enter an integer for wind speed.")

            # Validate region
            while region is None:
                region_input = input(region_prompt).strip().lower()
                if region_input in ('e', 'w'):
                    region = region_input
                else:
                    print("❌ Region must be 'E' or 'W'.")

            # All inputs are now valid
            valid_info = True
            report_key = f"Weather Report {i+1}"
            instances[report_key] = WeatherReport(air_temp, wind_speed, region)

            # store current report information in an instance
            instance = instances[report_key]
            width = 39
            id_width = 40
            report_name = report_key[:14]
            report_id = report_key[15:]
            report = textwrap.dedent(f"""
                {report_name:<{width}}{report_id:>{id_width}}
                {instance.get_advisory()}
                {'Temperature':<{width}} {instance.format_air_temp():>{width}}
                {'Wind Speed':<{width}} {instance.format_wind_speed():>{width}}
                {'Wind Chill':<{width}} {instance.format_wind_chill():>{width}}
            """).strip()

            # get width of report to create border
            report_lines = report.split("\n")
            max_length = max(len(line) for line in report_lines)
            border = "*" * (max_length)

            # print bordered report
            print(border)
            for line in report_lines:
                print(f"{line.ljust(max_length)}")
            print(border)
