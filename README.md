1.How many seconds are in an hour? Use the Interactive Interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).

2.Assign the result of the previous task (the number of seconds in an hour) to a variable called seconds_per_hour.

3.How many seconds are there in a day? Use the variable seconds_per_hour.

4.Count the number of seconds in a day again, but this time save the result to the variable seconds_per_day.

5.Divide the value of the seconds_per_day variable by the value of the seconds_per_hour variable. Use the floating point division (/).

6.Divide the value of the seconds_per_day variable by the value of the seconds_per_hour variable. Use the integer division (//). Is the result the same as the answer to the previous exercise, if you ignore the .0 at the end?

7.Write addition, subtraction, multiplication, and division operations that result in the number 12. You should write four lines of code that look something like this: print(5 + 7). The result should be four lines, each with the number 12.

8.Save your favorite number in a variable, and then use the variable to create a message to print this number. Print this message.

9.Save the user's name in a variable and print it in lower case, upper case, and case sensitive.

Write programs in a programming environment to solve the following problems:

10.Store any message in a variable and print that message. Then replace the value of the variable with another message and print the new message. Save the program in a file whose name follows the standard Python rules for using lowercase letters and underscores - for example, simple_messages.py.

11.Save the username in a variable and print a message intended for a specific person. The message should look something like this: "Hello, Sasha, would you like to learn some Python today?".

12.Find a famous quote you like. Save the name of the author of the quote in the famous_person variable. Compose a message and save it in a new variable named message. Print your message. The result should look something like this (including the quotes): Albert Einstein once said, "A person who never made a mistake never tried anything new."

13.Save the username in a variable and add a few spaces at the beginning and end of the username. Make sure that each control sequence (\t and \n) appears at least once. Print the name so that you can see the spaces at the beginning and end of the line. Then print it again using each of the following whitespace removal functions: lstrip(), rstrip(), and strip().

14.Use the print() function to print the complete home address. Print your first and last name in the first line. In each subsequent line print the individual elements of the address (country, zip code, city, street, house number, etc.).

15.Convert the distance units. The distance is given in meters. On each new line, the program displays the distance value in inches, feet, miles, yards, etc. Numerical data on the screen must be formatted: two digits after the decimal point. Use the format() function. Find the necessary values for the units of measurement on the Internet.

16.Calculate the duration of an event. Suppose a school vacation lasted several days. Print the total duration of this event in hours, minutes, and seconds in a formatted format (left alignment, field width: 10 characters).

17.Convert the temperature value to degrees Celsius (C) for other temperature scales: Fahrenheit (F) and Kelvin (K). The program should display the equivalent temperature in degrees Fahrenheit (F = 32 + 9/5 * C). The program should display the equivalent temperature in degrees Kelvin (K = C + 273.15). The results should be displayed in a formatted way: using two digits after the decimal point, minimum field length (15), centered. Note that in real numbers, a period is used to separate the fractional and integer parts.

18.Decompose a four-digit integer and display the sum of the digits in the number. For example, if you choose the number 6259, the program should display a message: 6 + 2 + 5 + 9 = 22. Use the format() function to display the result or f-string.

19.Given the latitude and longitude coordinates of two points on the Earth in degrees, find the distance between them in kilometers. Let (x1, y1) and (x2, y2) be the latitude and longitude coordinates (in degrees) of two points on the Earth's surface. The distance between these points in kilometers is calculated as follows: 6371.032 × arccos(sin(x1) × sin(x2) + cos(x1) × cos(x2) × cos(y1 - y2)). The value 6371.032 is the average radius of the Earth in kilometers. Python trigonometric functions work with radians. As a result, you need to convert coordinate values from degrees to radians before calculating the distance using the formula. The math module contains a function called radians() that converts degrees to radians. You can also convert using a formula, such as x1 = x1 × pi/180, where pi is the number Pi. Find the distance between the two cities Beijing (39.9075000, 116.3972300) and Kyiv (50.4546600, 30.5238000) and print the value on the screen. The distance value should be displayed in a formatted way: with three digits after the decimal point, minimum field length (10), and right alignment. On this site, find the coordinate values in decimal degrees for several more pairs of cities of your choice and determine the distance in kilometers between them. Check that the distances between the cities are correct using one of the services on the above website.




