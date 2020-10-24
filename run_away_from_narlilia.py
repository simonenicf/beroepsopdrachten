import time

start = 1
gender = 0
game = 0
skip1 = 0

while start == 1:
 print("----------------------------------------------------------------")
 print("run away from Narlilia")
 print("----------------------------------------------------------------")
 print(" ")
 print("a: start/vlucht")
 print("b: beëindig programa")
 menu = input("Wat wil je doen: ")
 if menu == "start" or menu == "a" or menu == "vlucht":
     print("----------------------------------------------------------------")
     print(" ")
     start += 1
 elif menu == "b" or menu == "beëindig" or menu == "exit":
     print("Oke dag hoop je snel weer te zien.")
     start = 0
 else:
     print("antwoordt: a of b")

while start == 2:
 print("Ik wil graag jou avontuur personaliseren.")
 naam = input("Zo hoe heet jij: ")
 print("Ah hallo " + naam + ".")
 print("Wil je de intro over Narilia skippen?")
 skip = input("Y/N: ")
 if skip == "y" or skip == "Y":
  print("oke laten we het verhaal starten")
  skip1 = 1
  start += 1
 elif skip == "n" or skip == "N":
  print("Oke hier komt de informatie over Narilia.")
  start += 1
 else:
  print("alsjeblieft antwoordt: Y of N")

while skip1 == 0 and start == 3:
 print("----------------------------------------------------------------")
 print(" ")
 time.sleep(1)
 print("Narlilia is een kleine land in ooste van de wereld ong. 30.000 km^2 groot")
 time.sleep(1)
 print("Het land heeft drie soorten geloven: naturia, magistra en kinlion.")
 time.sleep(1)
 print("----------------------------------------------------------------")
 print(" ")
 print("KINLION:")
 time.sleep(1)
 print("Kinlion is het geloof waar rond de 30% van het land in gelooft")
 time.sleep(1)
 print("Mensen die in kinlion geloven dat er meerdere goden zijn voor verschillende dingen")
 time.sleep(1)
 print("Je kan het lichtelijk vergelijken met griekse, egyptische of romeinse goden")
 time.sleep(1)
 print(" ")
 print("----------------------------------------------------------------")
 input("druk op enter om door te gaan")
 print("----------------------------------------------------------------")
 print(" ")
 print("MAGISTRA:")
 print("20% van de bevolking van Narilia gelooft in magistra.")
 print("Magistra gelooft dat als is geschonken aan het volk door een god genaam vulgaris Magistralis")
 time.sleep(1)
 print("Magistra'en hebben het gevoel dat Naturia's hun god wilt weg zuiveren alsof hij nooit bestaan heeft")
 time.sleep(1)
 print("Magistra'en zijn daarom pissig op Naturia aanhangers en de invloed die dat geloof heeft op de regering")
 time.sleep(1)
 
 start += 1













while skip1 == 1 and start == 3:
 print("----------------------------------------------------------------")
 start += 1
