{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Structure
------------

    ├── README.md          <- The top-level README for developers using this project.
	├── data
	│   ├── external       <- Data from third party sources.
	│   ├── interim        <- Intermediate data that has been transformed.
	│   ├── processed      <- The final, canonical data sets for modeling.
	│   └── raw            <- The original, immutable data dump.
	│
	├── logs               <- Log API requests (e.g. input, response, stdout, stderr information)
	│
	├── docs               <- A default Sphinx project; see sphinx-doc.org for details
	│
	├── models             <- Trained and serialized models, model predictions, or model summaries
	│
	├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
	│                         the creator's initials, and a short `-` delimited description, e.g.
	│                         `1.0-sa-initial-data-exploration`.
	│
	├── references         <- Data dictionaries, manuals, and all other explanatory materials.
	│
	├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
	│   └── figures        <- Generated graphics and figures to be used in reporting
	│
	├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
	│                         generated with `pip freeze > requirements.txt`
	│
	├── src                <- Source code for use in this project.
	│   ├── __init__.py    <- Makes src a Python module
	│   │
	│   ├── config.py      <- Configuration file for some global variables
	│   │
	│   ├── data           <- Scripts to download or generate data
	│   │   └── make_dataset.py
	│   │
	│   ├── features       <- Scripts to turn raw data into features for modeling
	│   │   └── build_features.py
	│   │
	│   ├── models         <- Scripts to train models and then use trained models to make
	│   │   │                 predictions
	│   │   ├── predict.py
	│   │   └── train.py
	│   │
	│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
	│       └── visualize.py
	│
	├── tests              <- Test scripts for unit testing (e.g. using pytest), 
	│                         performance and load testing of the API
	│
	├── api.py             <- Flask API script
	│
	└── .gitignore


--------

<p><small>Project based on the <a target="_blank" href="https://github.com/sujitahirrao/flask-api-template">Flask API Template</a>. #flaskappitemplate</small></p>
