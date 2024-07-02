import speech_recognition as sr

def reconhecer_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de fala: {e}")

    return None
