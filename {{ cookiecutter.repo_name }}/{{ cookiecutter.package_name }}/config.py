import os

ENV = "prod"    # [dev/test/prod]

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
print("PROJECT_DIR:\t", PROJECT_DIR)

DATA_FOLDER = os.path.join(PROJECT_DIR, 'data')
MODELS_FOLDER = os.path.join(PROJECT_DIR, 'models')
LOGS_FOLDER = os.path.join(PROJECT_DIR, 'logs')

if ENV == "dev":
    print("DATA_FOLDER:\t", DATA_FOLDER)
    print("MODELS_FOLDER:\t", MODELS_FOLDER)
    print("LOGS_FOLDER:\t", LOGS_FOLDER)
