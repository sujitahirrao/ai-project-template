# Flask API Template

#### TL;DR: To create a new Flask API project from this template using [cookiecutter](https://cookiecutter.readthedocs.io/), run:
    cookiecutter https://github.com/sujitahirrao/flask-api-template

------------

(Information below is liberally copied from https://drivendata.github.io/cookiecutter-data-science/, with required modifications.)

_**A logical, reasonably standardized, but flexible project template for creating new Flask APIs using cookiecutter.**_

## Why use this project structure?
> We're not talking about bikeshedding the indentation aesthetics or pedantic formatting standards — ultimately, the code quality is about correctness and reproducibility.

**Code quality is important!** Once started, it is not a process that lends itself to thinking carefully about the structure of your code or project layout, so it's best to start with a clean, logical structure and stick to it throughout. We think it's a pretty big win all around to use a fairly standardized setup like this one. Here's why:

### Other people will thank you
A well-defined, standard project structure means that a newcomer can begin to understand an analysis without digging in to extensive documentation. It also means that they don't necessarily have to read 100% of the code before knowing where to look for very specific things.

Well organized code tends to be self-documenting in that the organization itself provides context for your code without much overhead. People will thank you for this because they can:

* Collaborate more easily with you on this analysis
* Learn from your analysis about the process and the domain
* Feel confident in the conclusions at which the analysis arrives
 
 ### You will thank you
Ever tried to reproduce an analysis that you did a few months ago or even a few years ago? You may have written the code, but it's now impossible to decipher whether you should use *make_figures.py.old*, *make_figures_working.py* or *new_make_figures01.py* to get things done. Here are some questions we've learned to ask with a sense of existential dread:

* Are we supposed to go in and join the column X to the data before we get started or did that come from one of the notebooks?
* Come to think of it, which notebook do we have to run first before running the plotting code: was it "process data" or "clean data"?
* Where did the shapefiles get downloaded from for the geographic plots?
* _Et cetera, times infinity._  
  
These types of questions are painful and are symptoms of a disorganized project. A good project structure encourages practices that make it easier to come back to old work, for example separation of concerns, abstracting analysis as a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), and engineering best practices like version control.

### Nothing here is binding
> "A foolish consistency is the hobgoblin of little minds" — Ralph Waldo Emerson (and [PEP 8!](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds))

Disagree with a couple of the default folder names? Working on a project that's a little nonstandard and doesn't exactly fit with the current structure? Prefer to use a different package than one of the (few) defaults?

**Go for it!** This is a lightweight structure, and is intended to be a good starting point for many projects. Or, as PEP 8 put it:

> Consistency within a project is more important. Consistency within one module or function is the most important. ... However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/sujitahirrao/flask-api-template
    
### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── README.md               <- The top-level README for developers using this project.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
│
├── logs                    <- Log API requests (e.g. input, response, stdout, stderr information)
│
├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                  <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                              the creator's initials, and a short `-` delimited description, e.g.
│                              `1.0-sa-initial-data-exploration`.
│
├── references              <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated graphics and figures to be used in reporting
│
├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                     <- Source code for use in this project.
│   └── {{ cookiecutter.package_name }}
│       ├── __init__.py     <- Makes src a Python module
│       │
│       ├── config.py       <- Configuration file for some global variables
│       │
│       ├── data            <- Scripts to download or generate data
│       │   └── make_dataset.py
│       │
│       ├── features        <- Scripts to turn raw data into features for modeling
│       │   └── build_features.py
│       │
│       ├── models          <- Scripts to train models and then use trained models to make
│       │   │                 predictions
│       │   ├── predict.py
│       │   └── train.py
│       │
│       └── visualization   <- Scripts to create exploratory and results oriented visualizations
│           └── visualize.py
│
├── tests                   <- Test scripts for unit testing (e.g. using pytest), 
│                              performance and load testing of the API
│
├── api.py                  <- Flask API script
│
└── .gitignore
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    pytest tests

### Build documentation using Sphinx
------------

    cd docs/
    make html

