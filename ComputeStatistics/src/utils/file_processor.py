def process_file(file_path):
    with open(file_path, 'r') as file:
        items = file.readlines()
    return [item.strip() for item in items]