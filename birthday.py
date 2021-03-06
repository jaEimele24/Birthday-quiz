"""
birthday.py
Author: jaEimele24
Credit: Tutorials
Assignment: Birthday-quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
Name=input('Hello, what is your name? ')
BirthMonth=input('Hi {0}, what was the name of the month you were born in? '.format(Name))
Birthyear=int(input('And what year were you born in, {0}? '.format(Name)))
BirthDay=int(input('And the day? '))
Bearthseason=1
Birthage=2
k=0
if BirthMonth == "October" and BirthDay == 31:
    print('You were born on Halloween!')
    k=1
month = month_name[todaymonth]
if BirthDay==todaydate and BirthMonth==month:
    print('Happy birthday!')
    k=1
if BirthMonth == "December" or BirthMonth == "January" or BirthMonth == "February":
    Birthseason = "winter"
if BirthMonth == "March" or BirthMonth == "April" or BirthMonth == "May":
    Birthseason="spring"
if BirthMonth == "June" or BirthMonth == "July" or BirthMonth == "August":
    Birthseason = "summer"
if BirthMonth == "September" or BirthMonth == "October" or BirthMonth == "November":
    Birthseason = "fall"
if Birthyear < 1980:
    Birthage="Stone Age"
if Birthyear >= 1980 and Birthyear < 1990:
    Birthage="eighties"
if Birthyear >= 1990 and Birthyear < 2000:
    Birthage="nineties"
if Birthyear >= 2000:
    Birthage="two thousands"
randomplatitudes="you are a"
morepointlesswords="baby of the"
dumbpunctuation=","
name=Name,
if k==0:
    print('{0}, {1} {2} {3} {4}.'.format(Name,randomplatitudes,Birthseason,morepointlesswords,Birthage))



