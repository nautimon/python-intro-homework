def celsius_to_fahrenheit(c):
    f_temp = (c* 9/5) + 32
    return f_temp

def fahrenheit_to_celsius(f):
    c_temp = (f - 32) * 5/9
    return c_temp

c = 40
result = (celsius_to_fahrenheit(c))
print(f"{c}°C = {result:.1f}°F")

c = 20
result = (celsius_to_fahrenheit(c))
print(f"{c}°C = {result:.1f}°F")

c = 0
result = (celsius_to_fahrenheit(c))
print(f"{c}°C = {result:.1f}°F")

f = 60
result = (fahrenheit_to_celsius(f))
print(f"{f}°F = {result:.1f}°C")

f = 100
result = (fahrenheit_to_celsius(f))
print(f"{f}°F = {result:.1f}°C")

f = 0
result = (fahrenheit_to_celsius(f))
print(f"{f}°F = {result:.1f}°C")