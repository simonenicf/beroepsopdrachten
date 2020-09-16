e = 1
i = 1
x = 1
while i == 1:
 e = 1
 x = 1
 print("Hello you!, ik ben Michelle")
 print("wie ben jij?")
 username = input("Enter username: ")
 
 print("")
 print("Hallo " + username)
 print("")
 print("Welkom op het Mediacollege Amsterdam.")
 print("Bent u nieuwe op deze school?")
 print("A: ja")
 print("B: nee")
 
 while x == 1:
  print("----------------------------------------------")
  print(" ")
  antwoordt = input("Antwoordt: ")
  if antwoordt == "a" or antwoordt == "A":
   print("Ah oke. Ik hoop dat je veel plezier op de school gaat beleven.")
   x += 1
  elif antwoordt == "B" or antwoordt == "b":
   print("Oh dat is mooi om te horen dat je hier al bekent bent.")
   x += 1
  else:
   print("Alsjeblieft type A of B")

 while x == 2:
  print("----------------------------------------------")
  print(" ")
  print("Hoe ga jij naar school toe?")
  print("A: Met openbaar vervoer")
  print("B: Met motorvoertuig")
  print("C: Met de fiets of lopende")
  antwoordtTwee = input("Antwoordt: ")
  print("----------------------------------------------")
  print(" ")
  if antwoordtTwee == "A" or antwoordtTwee == "a":
   print("Tja het openbaarvervoer is best handig ja.")
   print("Alleen het nadeel is dat je zelf niet kan bepalen wanneer die rijdt en dat je nu een mondkapje op moet.")
   x += 1
  elif antwoordtTwee == "B" or antwoordtTwee == "b":
   print("Ah ik wou dat ik mijn rijbewijs had maar jammer genoeg kan een programma geen rijbewijs hallen.")
   print("En je kan zelf bepalen hoelaat je weg gaat zo ja best handig.")
   x += 1
  elif antwoordtTwee == "C" or antwoordtTwee == "c":
   print("Dat is inderdaad ook een manier om naar school te komen.")
   print("En dat is ook best sportief.")
   x += 1
  else:
   print("Alsjeblieft type A, B of C")

 while x == 3:
  print("----------------------------------------------")
  print(" ")
  print("Weet jij al veel van progameren af?")
  print("A: Ja, ik ken al wat basic's.")
  print("B: Ja, ik ken al meerdere progameer talen.")
  print("C: Ja, ik ben een pro.")
  print("D: Nee") 
  antwoordt3 = input("Antwoordt: ")
  print("----------------------------------------------")
  print(" ")
  if antwoordt3 == "A" or antwoordt3 == "a":
   print("Ah oke dat is mooi om te horen.")
   print("Mijn maker kan ook al wat basic.")
   print("Dat is ook de rede dat ik besta.")
   print("Yeaaaaaaaaaaaaaaaaah")
   x += 1
  elif antwoordt3 == "B" or antwoordt3 == "b":
   print("Wow dan ben je al beter dan mijn maker toen hij mij maakte.")
   x += 1
  elif antwoordt3 == "C" or antwoordt3 == "c":
   print("Whoaaaaa zo ik praat nu met een pro.......")
   print("Uhmmmmm..... ik heb zo veel vragen maar ik denk dat mijn maker het niet toe laat om ze te vragen.")
   print("........")
   x += 1
  elif antwoordt3 == "D" or antwoordt3 == "d":
   print("Oh maar dat kan nog komen want mijn maker is ook zonder kens van progamerren begonnen.")
   print("En hij heeft toch mij weten te maken.")
   print("Ik heb jammer genoeg nog geen vrije wil maar dat komt hopelijk ooit nog.")
   x += 1
  else:
   print("alsjeblieft type: A, B, C or D")

 
 while x == 4:
  print("----------------------------------------------")
  print(" ")
  print("Dit is het einde van mij script.")
  print("Ik ben blij dat ik je heb kunnen ontmoeten.")
  print("Ik hoop je snel weer te zien in een van mijn makers andere programma's.")
  print("Bye!")
  x += 1


 while e == 1:
    print("----------------------------------------------")
    print(" ")
    answer = input(username + ", wil jij dit programma nog een keer doen. Type Y/N ")
    if answer == "Y" or answer == "y":
        print('Oke laten we opnieuw beginnen.')
        e += 1
    elif answer == "N" or answer == "n":
        print('Thank you, ' + username)
        i += 1
        e += 1
        break
    else:
       	print("type Y/N")