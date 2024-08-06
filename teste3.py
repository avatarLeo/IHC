import pyttsx3

# Inicialize o mecanismo TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')



engine.setProperty("voice", "brazil")
engine.setProperty("rate", 130)

# Defina o texto que você deseja que o Python fale
text = "Conferindo informáções"





# Fale o texto
engine.say(text)

# Aguarde até que a fala seja concluída antes de encerrar o programa
engine.runAndWait()

