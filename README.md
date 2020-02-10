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

### Step 2: Move code to .py modules
- i.e. main funcitons and classes 

### Step 3: Add pipelines (stages) on Python modules

Pipeline (python) scripts location: `src/pipelines`

Main stages:

* __prepare_configs.py__: load config/pipeline_config.yml and split it into configs specific for next stages

* __featurize.py__: create new features

* __split_train_test.py__: split source dataset into train/test

* __train.py__: train classifier 

* __evaluate.py__: evaluate model and create metrics file

    
### Step 4: Automate pipelines (DAG) execution
  
- add pipelines dependencies under DVC control
- add models/data/congis under DVC control

1. Prepare configs

Run stage:

```bash
dvc run -f stage_prepare_configs.dvc \
        -d src/pipelines/prepare_configs.py \
        -d config/pipeline_config.yml \
        -o experiments/split_train_test_config.yml \
        -o experiments/featurize_config.yml \
        -o experiments/train_config.yml \
        -o experiments/evaluate_config.yml \
        python src/pipelines/prepare_configs.py \
            --config=config/pipeline_config.yml
```

Reproduce stage: `dvc repro pipeline_prepare_configs.dvc`


2. Features extraction

```bash
dvc run -f stage_featurize.dvc \
    -d src/pipelines/featurize.py \
    -d experiments/featurize_config.yml \
    -d data/raw/iris.csv \
    -o data/interim/featured_iris.csv \
    python src/pipelines/featurize.py \
        --config=experiments/featurize_config.yml
```

Reproduce stage: `dvc repro pipeline_featurize.dvc`

        
3. Split train/test datasets

Run stage:

```bash
dvc run -f stage_split_train_test.dvc \
    -d src/pipelines/split_train_test.py \
    -d experiments/split_train_test_config.yml \
    -d data/interim/featured_iris.csv \
    -o data/processed/train_iris.csv \
    -o data/processed/test_iris.csv \
    python src/pipelines/split_train_test.py \
        --config=experiments/split_train_test_config.yml \
        --base_config=config/pipeline_config.yml
```   

Reproduce stage: `dvc repro pipeline_split_train_test.dvc`


4. Train model 

Run stage:

```bash
dvc run -f stage_train.dvc \
    -d src/pipelines/train.py \
    -d experiments/train_config.yml \
    -d data/processed/train_iris.csv \
    -o models/model.joblib \
    python src/pipelines/train.py \
        --config=experiments/train_config.yml \
        --base_config=config/pipeline_config.yml
```   

Reproduce stage: `dvc repro pipeline_train.dvc`


5. Evaluate model

Run stage:

```bash
dvc run -f stage_evaluate.dvc \
    -d src/pipelines/evaluate.py \
    -d experiments/evaluate_config.yml \
    -d models/model.joblib \
    -m experiments/eval.txt \
    python src/pipelines/evaluate.py \
        --config=experiments/evaluate_config.yml \
        --base_config=config/pipeline_config.yml
```    


Reproduce stage: `dvc repro pipeline_evaluate.dvc`


# References used for this tutorial

1. [DVC tutorial](https://dvc.org/doc/tutorial) 
2. [100 - Logistic Regression with IRIS and pytorch](https://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/100_Logistic_IRIS.html) 