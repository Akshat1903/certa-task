# Certa Task

## Getting Started

Below listed are the detailed steps to use the script

### Prerequisites

You need to have following things installed: 
1. [Python](https://www.python.org/downloads/)
2. [Pip (Package Installer for python)](https://pypi.org/project/pip/)

### Usage

In order to use the program create a folder anywhere you want and create a python virtualenv in it and activate it, the following commands shows how it can be done in linux

```sh
mkdir akshattask
cd akshattask
python -m venv venv
source venv/bin/activate
```

Then you need to clone the repository

```sh
git clone https://github.com/Akshat1903/certa-task
```

In order to install all the dependencies in the program run the following command after moving inside the cloned directory

```sh
pip install -r requirements.txt
```

Next you need to configure the spotify credentials which you can get by following the [documentation](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/), enter the client id and client secret in the json file in songspotter folder using any text editor.

Now you are finally ready to run the program. Move inside the songspotter directory and run the following command
```sh
python main.py
```

## Contact

Akshat Gupta - [@linkedin_handle](https://www.linkedin.com/in/akshat-g-1903/) - [Mail me](mailto:akshatgupta1903@gmail.com)
