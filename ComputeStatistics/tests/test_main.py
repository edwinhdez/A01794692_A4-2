import unittest
import subprocess
import os

class TestMain(unittest.TestCase):
    def setUp(self):
        # Crear un archivo de prueba
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('1\n2\n3\n4\n5\n')

    def tearDown(self):
        # Eliminar el archivo de prueba
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_main(self):
        # Ejecutar el script main.py con el archivo de prueba
        result = subprocess.run(['python', 'ComputeStatistics/src/main.py', self.test_file], capture_output=True, text=True)
        output = result.stdout.strip()
        expected_output = "Items from the file:\n1\n2\n3\n4\n5"
        self.assertEqual(output, expected_output)

    def test_file_not_found(self):
        # Ejecutar el script main.py con un archivo inexistente
        result = subprocess.run(['python', 'ComputeStatistics/src/main.py', 'non_existent_file.txt'], capture_output=True, text=True)
        output = result.stdout.strip()
        self.assertIn("Error: The file 'non_existent_file.txt' was not found.", output)

if __name__ == '__main__':
    unittest.main()