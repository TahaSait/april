# program to convert celsius to Fahrenheit
def celsius_to_fahrenheit(cel):
    fah = cel * 9/5 + 32
    return fah

cel = 25
print(f"25 degress is {celsius_to_fahrenheit(cel)} Fahrenheit")