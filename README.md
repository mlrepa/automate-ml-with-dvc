# From Jupyter Notebooks to Reproducible and Automated experiments with DVC in just 4 steps
**Machine Learning REPA Week 2021 conference**

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
jupyter contrib nbextension install --user
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
    
#### Step 0: All in Junyter Notebooks 
- run all in Jupyter Notebooks

#### Step 1: Create a Single configuration file 

- a separate section for each logical stage 
- one base section with common configs (random_state)
- human readable format (.yaml)
- 
#### Step 2: Move code to .py modules
- i.e. main funcitons and classes 

#### Step 3: Create pipeline

Add a pipeline stages code to `src/pipelines`

    featurize.py - create new features
    split_train_test.py - split source dataset into train/test
    train.p - train classifier 
    evaluate.py - evaluate model and create metrics file

    
#### Step 4: Automate experiment pipeline with DVC
  
- add pipelines dependencies under DVC control
- add models/data/configs under DVC control


## References for code examples used

1. [DVC tutorial](https://dvc.org/doc/tutorial)
2. [Plot a Confusion Matrix](https://www.kaggle.com/grfiv4/plot-a-confusion-matrix) 