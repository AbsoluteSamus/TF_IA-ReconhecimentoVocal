import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Baixar recursos necessários do NLTK
nltk.download('punkt')

# Dataset de exemplo de xingamentos
xingamentos = [
    "idiota",
    "burro",
    "estúpido",
    "imbecil"
]

# Dataset de frases para treinamento
frases = [
    "Você é um idiota",
    "Você é muito inteligente",
    "Pare de ser burro",
    "Que pessoa estúpida",
    "Você é incrível",
    "Não seja imbecil"
]

# Labels indicando se a frase contém xingamentos ou não
labels = [1, 0, 1, 1, 0, 1]

# Pré-processamento e vetorização das frases
vectorizer = CountVectorizer(vocabulary=xingamentos)
X = vectorizer.fit_transform(frases)

# Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, labels)

# Função para censurar xingamentos
def censurar_frase(frase):
    tokens = nltk.word_tokenize(frase)
    for i, token in enumerate(tokens):
        if token in xingamentos:
            tokens[i] = '*' * len(token)
    return ' '.join(tokens)

# Teste da função de censura
frase_teste = "Você é um idiota imbecil"
print(censurar_frase(frase_teste))  # Saída: "Você é um ****** ******"

# Função para reconhecer áudio
def reconhecer_audio():
    import speech_recognition as sr
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

# Censura a frase reconhecida
if texto_reconhecido:
    texto_censurado = censurar_frase(texto_reconhecido)
    print(f"Texto censurado: {texto_censurado}")
