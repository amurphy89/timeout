#timeout

timeout is a simple console app that lets the team know what venues are good and not so good for post work get togethers!

## Getting Started

Open a command prompt in the root of the project and run:

```pip install -e .```

Then from your command line run:

```timeout "[name1]" "[name2]"```

Please wrap names in quotes

i.e ```timeout "Alan Allen" "John Davis"```

## Prerequisites

This project requires Python3 to be installed, you may want to run the application in a virtual Python environment. You can learn to install Python3 and virtualenv here:
https://docs.python-guide.org/dev/virtualenvs/

## Running the tests

To run the tests please install pytest with ```pip install pytest``` and run ```pytest``` in the root folder.

## Authors

* **Ash Murphy**

##Improvements

Given the time limit for this test I'd consider doing the following if I had more time:

- logging (I usually follow the .conf format that can be found here: https://realpython.com/python-logging/)

- Better input parsing and robust error handling
