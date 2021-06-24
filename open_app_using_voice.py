import pyttsx3
import os

engine = pyttsx3.init()
pyttsx3.speak("Enter Number to open application")
while True:
    print("Enter Number to open application")
    print("\n1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER \t 6.NOTEPAD \n\t 7.NOTEPAD++ \n\t 8.ADOBE PHOTOSHOP \t 9.ADOBE ILLUSTRATOR \n\n\t\t 0.FOR EXIT")
    p = input()
    p = p.upper()
    print(p)

    if("DONT" in p) or ("DON'T in p") or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue

    elif("4" in p):
        os.system("start chrome")

    elif("1" in p):
        os.system("start word")

    elif("2" in p):
        os.system("start powerpoint")

    elif("3" in p):
        os.system("start excel")

    elif("5" in p):
        os.system("start vlc")

    elif("6" in p):
        os.system("start notepad")

    elif("7" in p):
        os.system("start notepad++")

    elif("8" in p):
        os.system("start photoshop")

    elif("9" in p):
        os.system("start illustrator")

    elif("0" in p):
        pyttsx3.speak("Exiting")
        break

    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")