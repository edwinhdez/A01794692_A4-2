import unittest
import subprocess
import os

class TestMain(unittest.TestCase):
    def setUp(self):
        # Ruta al archivo de prueba
        self.test_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/Converter/data/test_file2.txt'
        
        # Crear el archivo de prueba si no existe
        if not os.path.exists(self.test_file):
            with open(self.test_file, 'w') as f:
                f.write('1\n2\n3\n4\n5\n')

    def tearDown(self):
        # Eliminar el archivo de prueba si es necesario
        # Comentado para evitar la eliminación del archivo de prueba
        # if os.path.exists(self.test_file):
        #     os.remove(self.test_file)
        pass

    def test_main(self):
        # Ejecutar el script convertNumbers.py con el archivo de prueba
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/Converter/src/convert_numbers.py', self.test_file], capture_output=True, text=True)
        output = result.stdout.strip()
        expected_output = (
            "Original Numbers:\n"
            "1\n2\n3\n4\n5\n\n"
            "Binary Numbers:\n"
            "1\n10\n11\n100\n101\n\n"
            "Hexadecimal Numbers:\n"
            "1\n2\n3\n4\n5\n\n"
        )
        self.assertIn(expected_output, output)

    def test_file_not_found(self):
        # Ejecutar el script convertNumbers.py con un archivo inexistente
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/Converter/src/convert_numbers.py', 'non_existent_file.txt'], capture_output=True, text=True)
        output = result.stdout.strip()
        self.assertIn("Error: The file 'non_existent_file.txt' was not found.", output)

if __name__ == '__main__':
    unittest.main()