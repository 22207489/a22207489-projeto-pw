import zipfile
import os

# Path to the uploaded zip file
zip_file_path = os.path.join(os.path.dirname(__file__),'/home/a22207489/projeto1Pw/meteo/icones/icones.zip')  # Atualize este caminho conforme necessário

# Directory to extract the files to
extract_to_path = os.path.join(os.path.dirname(__file__),'static/meteo/')  # Atualize este caminho conforme necessário

# Ensure the directory exists
os.makedirs(extract_to_path, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print("Files extracted successfully to:", extract_to_path)
