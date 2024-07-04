import os
from pathlib import Path

# List of files to be created in the project structure
list_of_files = [    
    ".github/workflows/.gitkeep",               # Placeholder to keep the .github/workflows directory in version control
    "src/__init__.py",                          # Initialization file for the source directory
    "src/components/__init__.py",               # Initialization file for the components package
    "src/components/data_ingestion.py",         # Module for data ingestion processes
    "src/components/data_transformation.py",    # Module for data transformation processes
    "src/components/model_trainer.py",          # Module for model training processes
    "src/components/model_evaluation.py",       # Module for model evaluation processes
    "src/pipeline/__init__.py",                 # Initialization file for the pipeline package
    "src/pipeline/training_pipeline.py",        # Module for training pipeline processes
    "src/pipeline/prediction_pipeline.py",      # Module for prediction pipeline processes
    "src/logger/logging.py",                    # Module for logging configurations
    "src/exception/exception.py",               # Module for custom exception handling
    "src/utils/utils.py",                       # Utility functions module
    "src/utils/__init__.py",                    # Initialization file for the utils package
    "tests/__init__.py",                        # Initialization file for the tests directory
    "tests/unit/__init__.py",                   # Initialization file for unit tests
    "tests/integration/__init__.py",            # Initialization file for integration tests
    "init_setup.sh",                            # Shell script for initial setup
    "requirements.txt",                         # File listing project dependencies
    "requirements_dev.txt",                     # File listing development dependencies
    "setup.py",                                 # Script for setting up the package
    "setup.cfg",                                # Configuration file for setup
    "pyproject.toml",                           # Project configuration file
    "tox.ini",                                  # Configuration file for Tox testing tool
    "experiments/experiments.ipynb",            # Jupyter notebook for experiments
]

# Iterate through the list of files to create the necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    # Create an empty file if it does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
