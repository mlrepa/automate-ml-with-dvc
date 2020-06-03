# Project Structure
--------------------

```
    .
    ├── config
    │   └── pipeline_config.yml     <- pipeline config
    ├── data
    │   ├── external                <- external data
    │   ├── interim                 <- data in intermediate processing stage
    │   ├── processed               <- data after all preprocessing has been done
    │   └── raw                     <- original unmodified data acting as source of truth and provenance
    ├── docs
    ├── experiments                 <- folder for experiments intermediate files
    ├── models                      <- folder for ML models
    ├── notebooks
    ├── src
        ├── data <- data prepare and/or preprocess
        ├── evaluate <- evaluating model stage code 
        ├── features <- code to compute features
        ├── pipelines <- scripts of pipelines
        ├── report <- visualization (often used in notebooks)
        ├── train <- train model stage code
        └── transforms <- transformations data code (e.g., augmentation) 
    ├── docker-compose.yml
    ├── Dockerfile
    └── README.md

```
# Preparation

### 1. Clone this repository

```bash
git clone https://gitlab.com/7labs.ru/tutorials-dvc/dvc-2-iris-demo-project.git
cd dvc-2-iris-demo-project
```

### 2. Get data

Download iris.csv

```bash
wget -P data/raw/ -nc https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
```         

It may not work for Windows. So, use the [this link](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv) 
to load data into `data/raw/` folder

### 3. Create .env file in `config/` folder 
```bash
GIT_CONFIG_USER_NAME=<git user>
GIT_CONFIG_EMAIL=<git email>
```
   
example

```.env
GIT_CONFIG_USER_NAME=mnrozhkov
GIT_CONFIG_EMAIL=mnrozhkov@gmail.com
```

# Build image

```bash
ln -sf config/.env && docker-compose build
```

# Run     
    
Run docker container via docker-compose  

```bash
docker-compose up
```

# Tutorial 
    
### Step 1: All in Junyter Notebooks 
- run all in Jupyter Notebooks

### Step 2.1: Move code to .py modules
- i.e. main funcitons and classes 

### Step 2.2: Add pipelines (stages) on Python modules

Pipeline (python) scripts location: `src/pipelines`

Main stages:

* __prepare_configs.py__: load config/pipeline_config.yml and split it into configs specific for next stages

* __featurize.py__: create new features

* __split_train_test.py__: split source dataset into train/test

* __train.py__: train classifier 

* __evaluate.py__: evaluate model and create metrics file

    
### Step 3: Automate pipelines (DAG) execution
  
- add pipelines dependencies under DVC control
- add models/data/configs under DVC control


### Step 4: Experiments management

- create multiple experiments;
- reproduce with different parameter (changes in pipeline_config.yaml);
- compare metrics.


# References used for this tutorial

1. [DVC tutorial](https://dvc.org/doc/tutorial) 
2. [100 - Logistic Regression with IRIS and pytorch](https://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/100_Logistic_IRIS.html) 