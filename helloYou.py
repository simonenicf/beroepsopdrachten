print("Hello you!, ik ben Michelle")
print("wie ben jij?")
username = input("Enter username:")
print("username is: " + username)
import datetime
x = datetime.datetime.now()
print(x)
answer = input(username + ", wil jij dit programma nog een keer doen. Type Y/N ").lower()
if answer == "Y"or answer == "y":
       	print('Hooray, I can!')
elif answer == "N" or answer == "n" :
      	print('Thank you, ' + username)
else:
       	print('Huh?')