import unittest
import subprocess
import os

class TestMain(unittest.TestCase):
    def setUp(self):
        # Ruta al archivo de prueba
        self.test_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/CountWords/data/test_file2.txt'
        
        # Crear el archivo de prueba con las palabras necesarias
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('mexico mexico costa rica estados unidos canada')

    def tearDown(self):
        # Eliminar el archivo de prueba si es necesario
        # Comentado para evitar la eliminación del archivo de prueba
        # if os.path.exists(self.test_file):
        #     os.remove(self.test_file)
        pass

    def test_main(self):
        # Ejecutar el script countWords.py con el archivo de prueba
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/CountWords/src/count_words.py', self.test_file], capture_output=True, text=True)
        output = result.stdout.strip()
        expected_output = (
            "Word Count:\n"
            "mexico: 2\n"
            "costa: 1\n"
            "rica: 1\n"
            "estados: 1\n"
            "unidos: 1\n"
            "canada: 1\n\n"
        )
        self.assertIn(expected_output, output)

    def test_file_not_found(self):
        # Ejecutar el script countWords.py con un archivo inexistente
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/CountWords/src/count_words.py', 'non_existent_file.txt'], capture_output=True, text=True)
        output = result.stdout.strip()
        self.assertIn("Error: The file 'non_existent_file.txt' was not found.", output)

if __name__ == '__main__':
    unittest.main()