well_id = "well_01"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f -32) * 5/9

print('the well identifiyer is', well_id)
print('the pressure in kpa is', round(pressure_kpa,1))
print('the temperature in celsius is', round(temperature_c, 1))
print('the sensor status is', sensor_active)

raw_pressure = "3150"
conversion_factor = 6.89476

# pressure_kpa =raw_pressure * conversion_factor
pressure_kpa = float(raw_pressure) * conversion_factor
print('the converted pressure is', round(pressure_kpa,1))


