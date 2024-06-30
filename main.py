import tkinter as tk
from tkinter import messagebox
from Twilio_Whats import enviar_mensagem_whatsapp
from Reconhecimento import reconhecer_audio
from train import censurar_frase

def processar_frase():
    texto_reconhecido = reconhecer_audio()
    
    if texto_reconhecido:
        texto_censurado = censurar_frase(texto_reconhecido)
        messagebox.showinfo("Texto Reconhecido e Censurado", f"Texto censurado: {texto_censurado}")
        
        # Configuração das credenciais do Twilio
        account_sid = 'AC64c7ec8bb74c0d57612b17238b92d846'
        auth_token = '3ac98e118c95dbc72353d2e581bdb372'
        from_number = 'whatsapp:+14155238886'  # Número do sandbox do Twilio
        to_number = 'whatsapp:+558694859177'  # Número de destino com o código do país
        
        try:
            mensagem_enviada = enviar_mensagem_whatsapp(account_sid, auth_token, from_number, to_number, texto_censurado)
            messagebox.showinfo("Mensagem Enviada", f"Mensagem enviada com sucesso: {mensagem_enviada}")
        except Exception as e:
            messagebox.showerror("Erro ao Enviar Mensagem", f"Erro: {str(e)}")

# Criando a janela principal
root = tk.Tk()
root.title("Reconhecimento de Voz e Envio pelo WhatsApp")

# Criando e posicionando os widgets
label = tk.Label(root, text="Clique no botão para iniciar o reconhecimento de voz e envio pelo WhatsApp:")
label.pack(pady=10)

botao = tk.Button(root, text="Iniciar Reconhecimento e Envio", command=processar_frase)
botao.pack(pady=10)

# Loop principal da interface gráfica
root.mainloop()
