# MMoSE-FinalProject
ID2201

## Contributers
Maximilian Georg Kurzawski & Fabian Zeiher 

## Dependencies
- Python 3.8 or higher
- pytest

If you are on macOs you can install python by running
```
brew install python
```

Install pytest by running
```
pip3 install pytest
```

## Run

To run the program simply run the main file.

```
python3 main.py
```

The program runs in an infinite loop. Close the program by using the commands in your terminal.

```
[control|strg] + c
```

## Test

In order to run the test run pytest from the root project directory.

```
pytest
```

In case you encounter any prompt_toolkit error, that means you've the wrong prompt_toolkit version. You can correct that by doing

```
pip install prompt_toolkit==1.0.14
```