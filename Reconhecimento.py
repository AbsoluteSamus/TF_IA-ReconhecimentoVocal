import speech_recognition as sr

def reconhecer_audio():
    # Inicializa o reconhecedor
    recognizer = sr.Recognizer()

    # Captura áudio do microfone
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = recognizer.listen(source)

    # Tenta reconhecer o discurso usando o Google Web Speech API
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de fala: {e}")


# Chama a função para capturar áudio e reconhecer o texto
texto_reconhecido = reconhecer_audio()
