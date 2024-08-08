import pyttsx3

#link para gerar video em libras

#https://video.vlibras.gov.br/#/
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

