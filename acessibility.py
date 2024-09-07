from playsound import playsound
import pyttsx3


SEM_DEFICIENCIA = 0
COM_DEFICIENCIA_VISUAL = 1
COM_DEFICIENCIA_AUDITIVA = 2

def sounds(path_sound):
    playsound(path_sound)

def voice(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')


    #language
    engine.setProperty("voice", "brazil")
    #speed
    engine.setProperty("rate", 110)

    engine.say(text)
    engine.runAndWait()