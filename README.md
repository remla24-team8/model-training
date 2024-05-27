# urlphishing

This is the repository for the project to detect phising in URLs using a CNN. This corresponds to Assingment 1: ML Configuration Management.

## Installation

We use [`uv`](https://github.com/astral-sh/uv) for dependency management. `uv` can be installed in two ways:

Either use an automatic installation script:
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or use [pipx](https://github.com/pypa/pipx):

```
pipx install uv
```

In both cases, be sure to set up your PATH correctly so that you can run `uv` from the commandline.

### Python version

For now, we use Python 3.12, which is the latest version of Python. Make sure you have that installed on your computer.

### Virtual environment

Setting up your Python virtual environment is as easy as:

```
uv venv
```

It will say something like:
```
> Using Python 3.12.0 interpreter at: <python path>
> Creating virtualenv at: .venv
```

Make sure it actually says "Python 3.12". If you have it installed but it says a different version, you can try running `uv venv -p 3.12`. If that also doesn't work, run `uv venv -p <path to python executable here>` (an example would be something like `/home/tip/.pyenv/versions/3.12.0/bin/python3`, it will end in `.exe` if you are in Windows).

You can activate the virtual environment as follows:

```
# On macOS and Linux when using bash/zsh (or similar).
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
```

### Dependencies

Once your virtual environment is activated, you can now install the project dependencies:

```
uv pip sync requirements.txt
```

## Updating the dependencies

To update the dependencies, first update the `pyproject.toml` file.

Then, run the following command:

```
uv pip compile pyproject.toml -o requirements.txt
```

This updates the requirements.txt with new locked dependencies based on the updated `pyproject.toml`. If you run `uv pip sync requirements.txt` again this will then update your installation.

<!-- ### Download Data
We use the phishing detection dataset from Aravindh Annamalai on Kaggle (https://www.kaggle.com/datasets/aravindhannamalai/dl-dataset).

 You can either download the dataset directly from the website or use `python src/download_data.py`. For the second method you will need your Kaggle API token, follow this tutorial (https://ravi-chan.medium.com/how-to-download-any-data-set-from-kaggle-7e2adc152d7f). 

### Get Data
After having downloaded the data from Kaggle, the following files (`test.txt`, `train.txt` and `val.txt`)  will be stored in the `dl-dataset\DL Dataset\` folder. By running `python src/get_data.py` the data will be stored in `csv_files\test_data.csv`, `csv_files\train_data.csv` and `csv_files\val_data.csv`. 

### Process Data
The text data must also be tokenized and the labels must be encoded, this is done by running inside your environment `python src/process_data.py`. It takes the data stored in the csv files and saves the tokenized versions in `csv_files\x_test.csv`, etc. .

### Train
Run `python src/train.py` to train the model stored in `src\model.py` and save it to `models/phishing_model.h5`. -->

<!-- ### DVC
To create a data pipeline we have used DVC (https://dvc.org/). By running `dvc init` you initialise DVC to setup the pipeline. 

You can either use a local remote DVC by running: `dvc remote add -d mylocalremote ~/ remotedvc`.

Or you can use a cloud remote like google drive following the instructions on this page (https://dvc.org/doc/user-guide/data-management/remote-storage/google-drive#url-format).

By running `dvc repro` a new version of the pipeline is executed. 

Run `dvc push` to push to the remote you created, remember to set your desired remote as default using `dvc remote default mylocalremote`

DVC also has an option to run experiments using `dvc exp run`. The accuracy and loss from each run is saved and can be viewed using `dvc exp show`.  -->
### Run
Create the folders for both the output and the data by running:
```
mkdir data
mkdir output
```

To run the created data pipeline first pull and reproduce:
```
dvc pull

dvc repro
```

After this you can run PyTest with

```
pytest

```