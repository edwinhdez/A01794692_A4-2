import os
import random
import nltk
from nltk.corpus import cess_esp

# Descargar el corpus de palabras en español si no está disponible
nltk.download('cess_esp')

def generate_random_word():
    """Genera una palabra aleatoria en español."""
    words = cess_esp.words()
    return random.choice(words)

def generate_test_file(file_path, num_words=100):
    """Genera un archivo de prueba con palabras aleatorias en español."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for _ in range(num_words):
            word = generate_random_word()
            f.write(f"{word} ")

if __name__ == "__main__":
    # Ruta al archivo de prueba
    test_file_path = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/CountWords/data/test_file.txt'
    
    # Crear el archivo de prueba con 1000 palabras aleatorias en español
    generate_test_file(test_file_path)
    print(f"Generated {test_file_path} with 1000 random Spanish words.")