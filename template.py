import os
from pathlib import Path
import logging

# logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', 
    level=logging.INFO,
)

project_name = "MlopsProject"

list_of_files = [
    ".github/workflows/ci-cd.yml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/comman.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "params.yml",
    "schema.yml",
    "main.py"
    "Dockerfile"
    "setup.py",
    # "requirements.txt",
    "research/research.py",
    "templates/index.html",
    "app.py"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"created file {filename} at {filepath}")
    else:
        logging.info(f"file {filename} already exists at {filepath}")

    
    
