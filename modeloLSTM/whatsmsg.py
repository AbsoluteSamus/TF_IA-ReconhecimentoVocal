from twilio.rest import Client

def enviar_mensagem_whatsapp(account_sid, auth_token, from_number, to_number, mensagem):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=mensagem,
        from_=from_number,
        to=to_number
    )
    return message.sid
