seconds_per_hour = 3600
seconds_per_day = seconds_per_hour * 24
result = seconds_per_day // seconds_per_hour
my_favorite_number = 28
my_name = 'Kyrylo'
poem = '''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
print(seconds_per_hour,seconds_per_day,result)
print(5 + 7)
print(20 - 8)
print(4 * 3)
print(24 // 2)
print(f"Today is: {my_favorite_number}")
print(f"{my_name}, {my_name.upper()},{my_name.lower()}")
print(poem[0:15])
print(len(poem))
print(poem.startswith('Yes'))
print(poem.endswith("I shall live!"))
print(poem.isalpha())
print(poem.isalnum())
print(poem.count(","))
print(poem.find(","))
print(poem.rfind(","))
message = 'Hello World!'
print(message)
print(f"Hello, {my_name}, would you like to learn some Python today?")
famous_person = 'Hellen Keller'
famous_quote = "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart."
print(f"{famous_person} once said: {famous_quote}")
user_name = "  Kyrylo  "
print(user_name.lstrip().rstrip().strip())
zip_code = "22049"
city = "Hamburg"
street = "Straßburger str."
house_number = "3"
print(f"User name: {user_name.strip()}\nZIP Code: {zip_code.lstrip()}\nCity: {city.lstrip()}\nStreet: {street.lstrip()}\nHouse number: {house_number}")
distance_in_meters = 1

distance_in_inches = distance_in_meters * 39.3701
distance_in_feet = distance_in_meters * 3.2808
distance_in_miles = distance_in_meters / 1609.344
distance_in_yards = distance_in_meters * 1.0936
print("Distance in meters is equal to: {:.2f}".format(distance_in_meters))
print("Distance in inches {:.2f}".format(distance_in_inches))
print("Distance in feet {:.2f}".format(distance_in_feet))
print("Distance in miles {:.2f}".format(distance_in_miles))
print("Distance in yards: {:.2f}".format(distance_in_yards))

school_vacation_in_days = 90
school_vacation_in_hours = school_vacation_in_days * 24
school_vacation_in_minutes = school_vacation_in_hours * 60
school_vacation_in_seconds = school_vacation_in_minutes * 60

print("{:<10} {:>10}".format("Duration of school vocation in days:",school_vacation_in_days))
print("{:<10} {:>10}".format("Duration of school vocation in hours:", school_vacation_in_hours))
print("{:<10} {:>10}".format("Duration of school vocation in minutes:", school_vacation_in_minutes))
print("{:<10} {:>10}".format("Duration of school vocation in seconds:", school_vacation_in_seconds)) 

celsius = 10
fahrenheit = 32 + 9/5 * celsius
kelvin = celsius + 273.15

print("Celsius is: {:.2f}".format(celsius))
print("Fahrenheit is: {:.2f}".format(fahrenheit))
print("Kelvin is: {:.2f}".format(kelvin))

number = 6259
first_digit_number = number // 1000
second_digit_number = (number // 100) % 10
third_digit_number = (number // 10) % 10
fourth_digit_number = number % 10
sum = first_digit_number + second_digit_number + third_digit_number + fourth_digit_number
print(f"{first_digit_number} + {second_digit_number} + {third_digit_number} + {fourth_digit_number} = {sum}")

import math

x1 = math.radians(39.9075000)
y1 = math.radians(116.3972300)
x2 = math.radians(50.4546600)
y2 = math.radians(30.5238000)

distance = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between Beijin and Kyiv is: {:>10.3f}".format(distance),"km")