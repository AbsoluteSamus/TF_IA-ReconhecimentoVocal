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
    "imbecil" ,
    "fela da puta",
    "desgraça"
]

def censurar_frase(frase):
    
    tokens = word_tokenize(frase)  # Tokenização da frase em palavras
    tokens_censurados = []

    for token in tokens:
        if token.lower() in xingamentos:
            tokens_censurados.append('*' * len(token))  # Substitui a palavra por asteriscos
        else:
            tokens_censurados.append(token)  # Mantém a palavra original

    return ' '.join(tokens_censurados)  # Retorna a frase censurada como uma string