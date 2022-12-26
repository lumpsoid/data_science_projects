# Seting a new environment for notebooks
## Get conda
[Installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
## Check updates
Make sure you have the latest version of conda installed on your system. If you need to update conda, you can run the following command:
```
conda update conda
```
## Create a new environment
Create a new conda environment and activate it. 
This will allow you to install the packages in the environment, rather than globally on your system.
```
conda create -n [environment_name] python=[python_version]
conda activate [environment_name]
```
Navigate to the directory where the requirements.txt file is located.
Run the following command to install all the packages listed in the file:
```
conda install --file requirements.txt
```
This will install all the packages listed in the requirements.txt file into the activated conda environment. 
You can then use these packages in your project by activating the environment before running your code.
```
conda activate [environment_name]
```
