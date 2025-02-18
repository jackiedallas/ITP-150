t = -6
v = 21
wind_chill = 35.74 + (0.6215 * t) - (35.75 * (v**0.16)) + \
    ((0.4275 * t) * (v**0.16))
print(wind_chill)
