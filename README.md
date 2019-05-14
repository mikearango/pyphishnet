# PyPhishNet
A simple Python Client library to interface with version 3 of the Phish.net API

### Create Conda environment

To replicate the development environment, run the following command in your terminal:
```bash
conda create --name phishnet --file requirements.txt --yes
```

### Create iPython kernel

If you are planning on doing some prototyping in a notebook-based environment, you'll need to add a new iPython kernel to Jupyter based off of your conda environment to match your scripting environment. You can do this as follows:
```bash
conda activate phishnet
conda install nb_conda --yes
python -m ipykernel install --user --name phishnet --display-name "phish.net"
```

### Storing environment variables

To my knowledge, all of the v3 APIs from Phish.net require authentication except 1: blog get requests. The PyPhishNet package currently allows for API authentication in 2 different ways: reading in through stored environment variables or explicitly declaring during instantiation of the `PhishNetAPI` class. We recommend storing API access credentials as environment variables as you do not want to have your API key exposed to the public. This also ensures you can easily access them in your Conda environment. The following steps will set up a process for automatically setting/unsetting environment variables when your environment is activated: 

1. Activate the Conda environment by running `conda activate phishnet`. 
2. Locate the directory for the conda environment by running `echo $CONDA_PREFIX`.
3. Enter that directory and create these subdirectories and files:
```bash
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
```
4. Edit `./etc/conda/activate.d/env_vars.sh` as follows:
```bash
#!/bin/sh
export PHISH_API_KEY='your-secret-key'
```
5. Edit `./etc/conda/deactivate.d/env_vars.sh` as follows:
```bash
#!/bin/sh
unset PHISH_API_KEY
```

Now when you run `conda activate phishnet`, the environment variables you specify in `./etc/conda/activate.d/env_vars.sh` such as `PHISH_API_KEY` are set to the values you wrote into the file. When you run `conda deactivate`, those variables are erased.

For more info, reference the [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables) for saving environment variables. 
