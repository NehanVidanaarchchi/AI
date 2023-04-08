from unittest import result
import pyttsx3
import wikipedia


nilame = pyttsx3.init()
voices = nilame.getProperty('voices')
nilame.setProperty('voice',voices[1].id)
nilame.setProperty('rate',175)

x = str(input(":"))

if (x == "NEON", x=="neon"):
    a = (" What do you want to know Sir ")
    print(a)
    nilame.say(a)
    nilame.runAndWait()
    In = input(" :  ")
    result = wikipedia.summary(In, sentences = 2)
    print(result)
    nilame.say(result)
    nilame.runAndWait()

    b = (" Enithing else Sir ")
    print(b)
    nilame.say(b)
    nilame.runAndWait()
    In = input(" :  ")
    

else:
    x = (" Thank you for using me Sir, Have a gread day ")
    print(x)
    nilame.say(x)
    nilame.runAndWait()
    
