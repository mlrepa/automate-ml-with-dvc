# Lesson 5 tutorial: Demo project Iris
**ML REPA School course**: Machine Learning experiments reproducibility and engineering with DVC

# Demo Project Structure
------------------------
```
    .
    ├── data
    │   ├── processed               <- processed data
    │   └── raw                     <- original unmodified/raw data
    ├── models                      <- folder for ML models
    ├── notebooks                   <- Jupyter Notebokos (ingored by Git)
    ├── reports                     <- folder for experiment reports
    ├── src                         <- source code for modules & pipelines
    └── README.md
```

## Preparation

### 1. Fork / Clone this repository

```bash
git clone https://gitlab.com/mlrepa/course-dvc-mlops/dvc-5-demo-project-iris.git 
cd dvc-5-demo-project-iris
```

### 2. Create a `master` branch and make it a default branch 
```bash
git checkout -b master
``` 
To make the `master` branch a default branch: 
1. At the GitLab repository page go to Settings -> Repository -> Default Branch
2. Click Expand;
3. Select `master` branch -> `Save changes`

 

### 2. Create and activate virtual environment

Create virtual environment named `dvc-venv` (you may use other name)
```bash
python3 -m venv dvc-venv
echo "export PYTHONPATH=$PWD" >> dvc-venv/bin/activate
source dvc-venv/bin/activate
```
Install python libraries

```bash
pip install -r requirements.txt
```
Add Virtual Environment to Jupyter Notebook

```bash
python -m ipykernel install --user --name=dvc-venv
``` 

Configure ToC for jupyter notebook (optional)

```bash
sudo jupyter contrib nbextension install
jupyter nbextension enable toc2/main
```

## 3. Run Jupyter Notebook

Jupyter Notebooks in `notebooks/` directory are for example only. 
To remove them (recommended) from `git` version control run: 

1 - Add the following string to `.gitignore`
```.gitignore
notebook/*
git add .gitignore
git commit -m "Update .gitignore: add notebooks/* " 
```
2 - Remove notebooks from the Git index and commit changes
```bash
git rm --cached notebooks/*
git commit -m "Unstage notebooks" 
```
Note: this will remove files from the Git index only! Files won’t be deleted from the disk
___
IMPORTANT: 
- If you `Remove notebooks from the Git index and commit changes` (see above), do any changes in notebooks and switch back to `step-1` / `step-7` branches, all changes will be lost
- It's not recommended to version your Jupyter Notebooks at all
- We would recommend to treat Jupyter Notebooks as artifacts for your experiments  
___

3 - Run Jupyter Notebooks
```bash
jupyter notebook
```

## Tutorial 
    
#### Step 1: All in Junyter Notebooks 
- run all in Jupyter Notebooks

#### Step 2: Move code to .py modules
- i.e. main funcitons and classes 

#### Step 3: Add DVC pipelines (stages) on Python modules

Add a pipeline stages code to `src/pipelines`

    prepare_configs.py - load config/pipeline_config.yml and split it into configs specific for next stages
    featurize.py - create new features
    split_train_test.py - split source dataset into train/test
    train.p - train classifier 
    evaluate.py - evaluate model and create metrics file

    
#### Step 4: Automate DVC pipeline (DAG) execution
  
- add pipelines dependencies under DVC control
- add models/data/configs under DVC control

#### Step 5: Create CI pipeline
- create .gitlab-ci.yml
- create ‘build’ job
- create ‘test’ job
- create local gitlab-runner with Docker executor


#### Step 6: Experiments management

- create multiple experiments
- reproduce with different parameter (changes in pipeline_config.yaml)
- compare metrics

#### Step 7: Deploy model with DVC and CML
- add deploy job to .gitlab-ci.yml


## References for code examples used

1. [DVC tutorial](https://dvc.org/doc/tutorial)
2. [Plot a Confusion Matrix](https://www.kaggle.com/grfiv4/plot-a-confusion-matrix) 