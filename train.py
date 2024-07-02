import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Baixar recursos necessários do NLTK
nltk.download('punkt')

# Dataset de exemplo de xingamentos
xingamentos = [
    "idiota",
    "burro",
    "estúpido",
    "imbecil",
    "desgraça"
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
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

# Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, labels)

def censurar_frase(frase):
    tokens = word_tokenize(frase)  # Tokenização da frase em palavras
    tokens_censurados = []

    for token in tokens:
        if token.lower() in xingamentos:
            tokens_censurados.append('*' * len(token))  # Substitui a palavra por asteriscos
        else:
            tokens_censurados.append(token)  # Mantém a palavra original

    return ' '.join(tokens_censurados)  # Retorna a frase censurada como uma string

