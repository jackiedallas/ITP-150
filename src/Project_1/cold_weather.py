"""
cold_weather.py
@auhthor: Jackie Johnson
"""


import textwrap


class WeatherReport:
    """Represents a weather report"""

    def __init__(self, reports, air_temp, wind_speed, region):
        self.reports = reports
        self.region = region
        self.air_temp = air_temp
        self.wind_speed = wind_speed


# prompts to get user inputs
region_prompt = textwrap.dedent("""
Please enter your region from the menu below:
E for East of the Blue Ridge Mountains:
W for West of the Blue Ridge Mountains:\n
""")
report_prompt = "Please enter a number of reports: "
air_temp_prompt = "Please enter the air temperature, no more than 50° F: "
wind_speed_prompt = "Please enter the wind speed, should be at least 3 mph: "

# call input function with prompts
reports = input(report_prompt)
air_temp = input(air_temp_prompt)
wind_speed = input(wind_speed_prompt)
region = input(region_prompt)

# initialize weather report object
weather_report = WeatherReport(reports, air_temp, wind_speed, region)

print(weather_report.wind_speed)
