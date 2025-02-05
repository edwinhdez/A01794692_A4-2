"""
Este módulo convierte una lista de números en un archivo a sus 
representaciones binarias y hexadecimales.
"""

import sys
import argparse
import os
import time
from utils.file_processor import process_file


def to_binary(number):
    """Convierte un número a su representación binaria."""
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


def to_hexadecimal(number):
    """Convierte un número a su representación hexadecimal."""
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal


def process_file_and_convert(file_path):
    """Procesa el archivo y convierte los números a binario y hexadecimal."""
    try:
        items = process_file(file_path)
        numbers = []
        for item in items:
            try:
                numbers.append(int(item))
            except ValueError:
                print(f"Warning: '{item}' is not a valid number and will be ignored.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except OSError as e:
        print(f"An OS error occurred: {e}")
        sys.exit(1)
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    #     sys.exit(1)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    binary_numbers = [to_binary(number) for number in numbers]
    hexadecimal_numbers = [to_hexadecimal(number) for number in numbers]

    return numbers, binary_numbers, hexadecimal_numbers


def main():
    """Función principal para analizar argumentos y convertir números."""
    parser = argparse.ArgumentParser(
        description="Convert a list of numbers from a file to binary and hexadecimal.")
    parser.add_argument('file_path', nargs='?', default='Converter/data/test_file.txt',
                        help='Path to the file containing the list of items')
    args = parser.parse_args()

    file_path = args.file_path

    start_time = time.time()

    numbers, binary_numbers, hexadecimal_numbers = process_file_and_convert(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = (
        "Original Numbers:\n" + "\n".join(map(str, numbers)) + "\n\n" +
        "Binary Numbers:\n" + "\n".join(binary_numbers) + "\n\n" +
        "Hexadecimal Numbers:\n" + "\n".join(hexadecimal_numbers) + "\n\n" +
        f"Time Elapsed: {elapsed_time:.2f} seconds\n"
    )

    print("Conversion Results:")
    print(results)

    # Ensure the directory exists
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    os.makedirs(output_dir, exist_ok=True)

    # Save the results to the file in the data directory
    output_file_path = os.path.join(output_dir, 'ConvertionResults.txt')
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(results)


if __name__ == "__main__":
    main()
