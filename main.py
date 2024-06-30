from Twilio_Whats import enviar_mensagem_whatsapp
from Reconhecimento import reconhecer_audio
from train import censurar_frase

def main():
    # Configuração das credenciais do Twilio
    account_sid = 'AC64c7ec8bb74c0d57612b17238b92d846'
    auth_token = '9c77c9cdaf6c65351d9846960a6a0016'
    from_number = 'whatsapp:+14155238886'  # Número do sandbox do Twilio
    to_number = 'whatsapp:+558694859177'  # Número de destino com o código do país

    # Chama a função para capturar áudio e reconhecer o texto
    texto_reconhecido = reconhecer_audio()

    # Censura a frase reconhecida
    if texto_reconhecido:
        texto_censurado = censurar_frase(texto_reconhecido)
        print(f"Texto censurado: {texto_censurado}")

        # Envio da mensagem censurada pelo WhatsApp usando Twilio
        mensagem = texto_censurado
        mensagem_enviada = enviar_mensagem_whatsapp(account_sid, auth_token, from_number, to_number, mensagem)
        print(f"Mensagem enviada com sucesso: {mensagem_enviada}")

if __name__ == "__main__":
    main()
