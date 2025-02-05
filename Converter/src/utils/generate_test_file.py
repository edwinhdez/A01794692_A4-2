import random
import os

def generate_test_file(file_path, num_lines=1000):
    with open(file_path, 'w') as f:
        for _ in range(num_lines):
            f.write(f"{random.randint(1, 1000)}\n")

if __name__ == "__main__":
    # Ruta al archivo de prueba
    test_file_path = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/ComputeStatistics/data/test_file.txt'
    
    # Crear el archivo de prueba con 1000 datos aleatorios
    generate_test_file(test_file_path)
    print(f"Generated {test_file_path} with 1000 random numbers.")