# program to convert celsius to Fahrenheit
def celsius_to_fahrenheit(cel):
    ''' convert value given to fahrenheit'''
    fah = cel * 9/5 + 32
    return fah
# program to convert Fahrenheit to celsius
def fahrenheit_to_celsius(fah):
    ''' convert value given to celsius'''
    cel = (fah - 32) * 5/9
    return cel
cel = 25
fah = 88
print(f"{cel} celsius is {celsius_to_fahrenheit(cel)} Fahrenheit\
 and {fah} Fahrenheit is {fahrenheit_to_celsius(fah)} celsius")