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

## Run
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

At the end it will automatically open a browser that allows you to log in in to Google Drive, the permissions are so that only we can actually then modify it. 

### Testing

After this you can run PyTest with

```
pytest

```

GitHub unfortunately has no option for soft failing (failing with a warning instead of a red cross), which means we had to improvise. Now any tests allowed to soft fail are automatically skipped when failing instead of failing the whole test. This is indicated by pytest printing: `..s...` where s is the soft-failed test.

Currently tests are failing due to the model itself not being very good in predicting phishing URLs when it comes to internationalized URLs.
