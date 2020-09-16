e = 1
i = 1
while i == 1:
  e = 1
  print("Hello you!, ik ben Michelle")
  print("wie ben jij?")
  username = input("Enter username:")
  print("username is: " + username)
  import datetime
  x = datetime.datetime.now()
  print(x)
  while e == 1:
    answer = input(username + ", wil jij dit programma nog een keer doen. Type Y/N ").lower()
    if answer == "Y" or answer == "y":
        print('Okay lets start over')
        e += 1
    elif answer == "N" or answer == "n":
        print('Thank you, ' + username)
        i += 1
        break
    else:
       	print("type Y/N")