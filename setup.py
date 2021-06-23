import os
import sys
import subprocess

required_env_variables = ['API_KEY', 'API_SECRET']

# Create .env template
print("Generating .env template")

with open('.env', 'w') as file:
    for key in required_env_variables:
        file.write(f'{key}=\n')

# Set up virtual environment
print("Setting up virtual environment")

subprocess.check_call([sys.executable, "-m", "venv", "venv"])

# Install packages from requirements.txt
print("Installing packages from requirements.txt")

project_root_path = os.path.dirname(__file__)
venv_python_path = os.path.join(project_root_path, "venv\Scripts\python.exe")

subprocess.check_call([venv_python_path, "-m", "pip", "install", '-U', 'pip'], stdout=subprocess.DEVNULL)
subprocess.check_call([venv_python_path, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL)

print("Done! Make sure to insert your environment variables into the .env file")