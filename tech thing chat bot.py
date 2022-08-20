import time
import random


ischad = 0
colours = ["red","yellow","green","blue","tangerine"]
names = ["bert","gertrude","timothy","steven"]

botname = random.choice(names)
botcolour = random.choice(colours)
rand = random.randint(1, 5)


print()
showvar = input("Press Enter to continue... ")
if "var" in showvar.lower():
    print("colour - " + botcolour)
    print("name - " + botname)
    makechad = input("make bot chad? [y/n] ")
    if "y" in makechad.lower():
        rand = 5
    elif "n" in makechad.lower():
        rand = 1


if rand == 5:
    ischad = 1
    cname = input("yo wassup broski my name is chad, whats your name? ")
    time.sleep(2)
    print("sup " + cname)
else:
    
    name = input("Hi. I am a chat bot, my name is " + botname + " what is your name? ")
    time.sleep(2)
    print ("Hello " + name)
feeling = input("how are you today? ")
time.sleep(2)

if "swag" in feeling.lower() and rand == 5:
    print("thats totes tubeular broski B]")
if "swag" in feeling.lower() and ischad == 0:
    print("sorry i wasnt programmed to know the meaning of SWAG")
if "good" in feeling.lower():
    print("im feeling good too!")
if "sad" in feeling.lower():
    print("im sorry to hear that :[")
if "happy" in feeling.lower():
    print("thats good! :]")
    
time.sleep(2)
favcolour = input("what is your favorite colour? ")


if favcolour.lower() in botcolour:
    print(botcolour + " is my favorite colour too!")
else:
    print(favcolour + " is a nice favorite colour but i prefer " + botcolour)

if rand == 5:
    print("peace out homedawg, see ya later alligator ")
    bye = input()
    if "in a while crocodile" in bye.lower():
        print(":]")
else:
    print("it has been nice talking to you, goodbye :]")