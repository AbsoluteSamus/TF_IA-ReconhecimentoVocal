import nltk
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

# Baixar recursos necessários do NLTK
nltk.download('punkt')

# Dataset de exemplo de xingamentos e palavras comuns
xingamentos = [
    "idiota",
    "burro",
    "estúpido",
    "imbecil",
    "desgraça"
]

palavras_comuns = [
    "olá",
    "mundo",
    "bom",
    "dia",
    "como",
    "você",
    "está"
]

# Combinar os datasets e criar os rótulos
palavras = xingamentos + palavras_comuns
labels = [1] * len(xingamentos) + [0] * len(palavras_comuns)

# Treinando o modelo LSTM
tokenizer = Tokenizer()
tokenizer.fit_on_texts(palavras)
sequences = tokenizer.texts_to_sequences(palavras)
padded_sequences = pad_sequences(sequences, maxlen=10)

# Definindo o modelo LSTM
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=10))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# Compilando o modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinando o modelo
labels = np.array(labels)
model.fit(padded_sequences, labels, epochs=10, verbose=1)

# Função para censurar frase usando LSTM
def censurar_frase(frase):
    tokens = word_tokenize(frase)
    tokens_censurados = []

    for token in tokens:
        sequence = tokenizer.texts_to_sequences([token])
        padded_sequence = pad_sequences(sequence, maxlen=10)
        
        if len(sequence[0]) == 0:  # Caso a palavra não esteja no vocabulário do tokenizer
            tokens_censurados.append(token)
        else:
            prediction = model.predict(padded_sequence)[0][0]
            if prediction >= 0.5:
                tokens_censurados.append('*' * len(token))
            else:
                tokens_censurados.append(token)

    return ' '.join(tokens_censurados)

# Exemplo de uso da função
if __name__ == "__main__":
    exemplo_frase = "Você é um idiota burro e imbecil"
    censurado = censurar_frase(exemplo_frase)
    print(f"Frase original: {exemplo_frase}")
    print(f"Frase censurada: {censurado}")
