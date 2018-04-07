# TermPlanner
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/ModoUnreal/TermPlanner.svg?branch=master)](https://travis-ci.org/ModoUnreal/TermPlanner)
[![Latest Version](https://pypip.in/version/termplanner/badge.svg)](https://pypi.python.org/pypi/termplanner/)

Command line application to increase your productivity!

## Usage
### Initialise a database
To begin using `termplanner` you must initialise a database.
```bash
$ planner init
```

You only need to initialise the database once. After that you can just reuse it, as the file will already be made.

### Add an event to the database
You can then add an event to the database like so:
```bash
$ planner add [date][event]
$ planner add "05.06.2018" "Exam day!!!!"
```
The date and event arguments must be added in as strings.

### Manually delete an event from the database
To delete an event from the database input the following:
```bash
$ planner checkout [event]
```
You can also add the following options when using `checkout`.
* `--allow_list` prints out a list of remaining events after an event is deleted.
* `--disallow_list` is the default.

### Display a list of events in the database
To show what events are inside the database do this:
```bash
$ planner list
```

## Installation

### PyPi package
TermPlanner is available on PyPi and can be installed with pip:

```bash
$ pip install termplanner
```

You can also install the latest version of 'planner' from Github:
```bash
$ pip install git+https://github.com/ModoUnreal/planner.git
```

## Developer Installation
If you are interested in contributing to 'TermPlanner', run the following commands:

```bash
$ git clone https://github.com/ModoUnreal/TermPlanner.git

$ pip install -e

$ pip install -r requirements.txt

$ planner <command> [params] [options]

```

## Unit Tests
Run unit tests in your active python environment:

```bash
$ python tests/test_planner.py

```

## Credits
* [click](https://github.com/pallets/click) by [mitsuhiko](https://github.com/mitsuhiko)

## Contact Information
You can contact me to discuss the project using my email below:

modounreal@gmail.com
