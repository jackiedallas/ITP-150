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
        formatted_wind_chill = float(self.get_wind_chill()).__format__('.2f')
        return f"{formatted_wind_chill}°F"

    def get_advisory(self):
        """Issue an advisory based on wind chill and air temperature."""
        if self.region == 'e':
            if (self.air_temp <= 0
                    and self.air_temp >= -9) or \
                    (float(self.get_wind_chill()) <= 0
                        and float(self.get_wind_chill()) >= -9):
                return "Cold Weather Advisory Issued East of Blue Ridge"
            elif self.air_temp < -10 or float(self.get_wind_chill()) < -10:
                return "Extreme Cold Weather Advisory Issued East of Blue Ridge"
            else:
                return "No Cold Weather Advisory or Extreme Weather Warning"
        if self.region == 'w':
            if (self.air_temp <= -10
                and self.air_temp >= -19) or \
                (float(self.get_wind_chill()) <= -10
                    and float(self.get_wind_chill()) > -19):
                return "Cold Weather Advisory Issued Blue Ridge and West"
            elif self.air_temp < -20 or float(self.get_wind_chill()) < -20:
                return "Extreme Cold Weather Advisory Issued Blue Ridge and West"
            else:
                return "No Cold Weather Advisory or Extreme Weather Warning"


report_prompt = "Please enter a number of reports: "


# validate reports are more than zero
valid_reports = False
while not valid_reports:

    reports = int(input(report_prompt))
    report_check = False

    if reports > 0:
        report_check = True
    else:
        report_check = False

    if report_check:
        valid_reports = True
    else:
        if not report_check:
            print("Number of reports must be greater than 0.")

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
        Please enter the air temperature for Report {i+1}, 50 or less:\n
        """)
        wind_speed_prompt = textwrap.dedent(f"""
        Please enter the wind speed for Report {i+1}, should be at least 3:\n
        """)

        # create while loop to make sure information entered is valid
        valid_info = False
        while not valid_info:

            # call input function with prompts
            air_temp = int(input(air_temp_prompt))
            wind_speed = int(input(wind_speed_prompt))
            region = input(region_prompt).lower()

            # flags for validating information entered
            valid_air_temp = False
            valid_ws = False
            # valid_reports = False
            valid_region = False

            # check for valid air temperature
            if air_temp <= 50:
                valid_air_temp = True
            else:
                valid_air_temp = False

            # check for valid wind speed
            if wind_speed >= 3:
                valid_ws = True
            else:
                valid_ws = False

            # check for valid region
            if region == 'e' or region == 'w':
                valid_region = True
            else:
                valid_region = False

            # check if all info is valid
            if valid_region and valid_air_temp and valid_reports and valid_ws:
                valid_info = True
                instances[f'Weather Report {i+1}'] = WeatherReport(
                    air_temp, wind_speed, region)

            else:
                if not valid_region:
                    print("Region entered wasn't valid, must be 'E' or 'W'")
                if not valid_air_temp:
                    print("Air Temperature wasn't valid must be 50°F or less.")
                if not valid_ws:
                    print("Wind Speed wasn't valid, must be 3 mph or more.")


for key, instance in instances.items():
    report_name = key[:14]
    report_id = key[15:]
    report = textwrap.dedent(f"""
    {report_name:^10}{report_id:^10}
    {instance.get_advisory()}
    Temperature: {instance.air_temp}°F
    Wind Speed: {instance.wind_speed} MPH
    Wind Chill: {instance.format_wind_chill()}
    """)
    print(report)
