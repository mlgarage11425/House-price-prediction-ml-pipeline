import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "House_price"


list_of_files = [
    f"src/{project_name}/__init__.py",
    
    # Data preprocessing and feature engineering
    f"src/{project_name}/data_preprocessing/preprocess.py",
    f"src/{project_name}/feature_engineering/features.py",
    
    # Model training and evaluation
    f"src/{project_name}/models/train_model.py",
    f"src/{project_name}/models/evaluate.py",
    
    # Pipeline automation
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    
    # Deployment via Flask
    f"src/{project_name}/deployment/flask_app.py",
    
    # Logging and utilities
    f"src/{project_name}/logger/logger.py",
    f"src/{project_name}/utils/helpers.py",
    
    # Configs
    f"config/config.yaml",
    f"config/schema.yaml",
    
    # Notebook for EDA
    f"notebooks/EDA.ipynb",
    
    # Data folders
    f"data/raw/.gitkeep",
    f"data/processed/.gitkeep",
    
    # Tests
    f"tests/test_preprocessing.py",
    f"tests/test_pipeline.py",
    f"tests/test_model.py",
    
    # Model and output folders
    f"saved_models/.gitkeep",
    f"outputs/logs/.gitkeep",
    f"outputs/reports/.gitkeep",
    
    # Project metadata and environment setup
    ".gitignore",
    "requirements.txt",
    "README.md",
    "main.py"
]





for file_path in list_of_files:
    file_path = os.path.normpath(file_path)
    dir_name = os.path.dirname(file_path)
    
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
        print(f"Created directory: {dir_name}")
    
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")
