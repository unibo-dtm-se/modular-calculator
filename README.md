# Calculator

A simple calculator toolkit written in Python, with several UIs.

## Remarks

UI code is clearly separated from the business logic. 
Actually, two sorts of UIs are provided: a command-line interface (CLI) and a graphical user interface (GUI), 
based on [Kivy](https://kivy.org/).

## Requirements

- Python 3.11
- Kivy 2.3

## How to run the calculator

The software can be run as either a __desktop app__ or a __command-line__ tool.

> Recall restoring the dependencies before running the app for the first time.

### Running the calculator as a desktop app

Open a shell in this directory, and run the following command:

```bash
python -m calculator.ui.gui
```

### Running the calculator as a command-line tool

Open a shell in this directory, and run the following command:

```bash
python -m calculator.ui.cli EXPRESSION
```

where `EXPRESSION` is a mathematical expression to be evaluated.


## How to restore dependencies

Open a shell in this directory, and run the following command:

```bash
pip install -r requirements.txt
```
