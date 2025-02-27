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
        """Calculate wind chill"""
        return 35.74 + (0.6215 * self.air_temp) - (35.75 * (self.wind_speed**0.16)) + \
               ((0.4275 * self.air_temp) * (self.wind_speed**0.16))

    def format_temp(self, value, unit):
        """Format temperature or speed values"""
        return f"{value:.1f}{unit}"

    def get_advisory(self):
        """Issue an advisory based on wind chill and air temperature."""
        advisories = {
            "e": ("Cold Weather Advisory Issued East of Blue Ridge",
                  "Extreme Cold Weather Advisory Issued East of Blue Ridge"),
            "w": ("Cold Weather Advisory Issued Blue Ridge and West",
                  "Extreme Cold Weather Advisory Issued Blue Ridge and West")
        }

        threshold = (-10, -20) if self.region == "w" else (0, -10)
        wind_chill = self.get_wind_chill()

        if threshold[0] > self.air_temp > threshold[1] or threshold[0] > wind_chill > threshold[1]:
            return advisories[self.region][0]
        elif self.air_temp < threshold[1] or wind_chill < threshold[1]:
            return advisories[self.region][1]
        return "No Cold Weather Advisory or Extreme Weather Warning"


def get_valid_input(prompt, condition, error_msg):
    """Generic function to get valid user input"""
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            print(error_msg)
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")


# Validate and get the number of reports
reports = get_valid_input("Please enter a number of reports: ",
                          lambda x: x > 0,
                          "Number of reports must be greater than zero.")

instances = {}

for i in range(reports):
    region = input(f"\nEnter region for Report {i+1} (E/W): ").strip().lower()
    while region not in ('e', 'w'):
        print("❌ Region must be 'E' or 'W'.")
        region = input("Enter region (E/W): ").strip().lower()

    air_temp = get_valid_input(f"Enter air temperature for Report {i+1} (≤50°F): ",
                               lambda x: x <= 50,
                               "Air Temperature must be 50°F or less.")

    wind_speed = get_valid_input(f"Enter wind speed for Report {i+1} (≥3 mph): ",
                                 lambda x: x >= 3,
                                 "Wind Speed must be at least 3 mph.")

    report = WeatherReport(air_temp, wind_speed, region)
    instances[f"Weather Report {i+1}"] = report

    # Generate formatted report
    report_output = textwrap.dedent(f"""
        {'Weather Report':<39}{i+1:>40}
        {report.get_advisory()}
        {'Temperature':<39}{report.format_temp(report.air_temp, '°F'):>39}
        {'Wind Speed':<39}{report.format_temp(report.wind_speed, ' mph'):>39}
        {'Wind Chill':<39}{report.format_temp(report.get_wind_chill(), '°F'):>39}
    """).strip()

    # Print bordered report
    border = "*" * max(len(line) for line in report_output.split("\n"))
    print(border)
    for line in report_output.split("\n"):
        print(line.ljust(len(border)))
    print(border)
