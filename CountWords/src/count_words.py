"""
Este módulo cuenta las palabras en un archivo.
"""

import sys
import argparse
import os
import time
from utils.file_processor import process_file


def count_words(words):
    """Cuenta las palabras en una lista de palabras."""
    word_count = {}
    x_count = 0
    for word in words:
        word = word.lower()
        if 'x' in word:
            x_count += 1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count, x_count


def process_file_and_count(file_path):
    """Procesa el archivo y cuenta las palabras."""
    try:
        items = process_file(file_path)
        words = []
        for item in items:
            words.extend(item.split())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except OSError as e:
        print(f"An OS error occurred: {e}")
        sys.exit(1)
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    #     sys.exit(1)

    if not words:
        print("Error: No valid words found in the file.")
        sys.exit(1)

    return count_words(words)


def main():
    """Función principal para analizar argumentos y contar palabras."""
    parser = argparse.ArgumentParser(
        description="Count the words in a file.")
    parser.add_argument('file_path', nargs='?', default='CountWords/data/test_file.txt',
                        help='Path to the file containing the list of words')
    args = parser.parse_args()

    file_path = args.file_path

    start_time = time.time()

    word_count, x_count = process_file_and_count(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = (
        "Word Count:\n" + 
        "\n".join(f"{word}: {count}" for word, count in word_count.items()) +
        "\n\n" +
        f"Words containing 'x': {x_count}\n\n" +
        f"Time Elapsed: {elapsed_time:.2f} seconds\n"
    )

    print("Word Count Results:")
    print(results)

    # Ensure the directory exists
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    os.makedirs(output_dir, exist_ok=True)

    # Save the results to the file in the data directory
    output_file_path = os.path.join(output_dir, 'WordCountResults.txt')
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(results)


if __name__ == "__main__":
    main()
