# Raw readings in celsius
readings_c = [22.5, 23.1, 20.9, 24.0, 21.5, 19.8, 26.2, 23.5]
# Readings in fahrenheit
readings_f = [temp_c * 1.8 + 32 for temp_c in readings_c]

# Temperature above 23.0
hot_days = [temp_c for temp_c in readings_c if temp_c > 23.0]

print("Readings in Fahrenheit:", readings_f)
print("Hot Days:", hot_days)