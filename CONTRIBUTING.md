# Contributing to afdd-framework

This document is a set of guidelines and resources for contributing to the afdd-framework effort.
Improvements and changes to this document are always welcome
via [Pull Request](https://github.com/BrickSchema/afdd-framework/pulls)

## Asking Questions

If you have a question about afdd-framework or its related tools, it is recommended to make a post in
the [afdd-framework User Forum](https://groups.google.com/forum/#!forum/brickschema) or under
the [afdd-framework GitHub Issue Tracker](https://github.com/BrickSchema/afdd-framework/issues). If you have a question
about the website,
please file the question either in the User Forum or on
the [afdd-framework Website Issue Tracker](https://github.com/BrickSchema/afdd-framework/issues).

Please conduct a brief search to see if someone has asked your question already; if they have, feel free to jump into
the conversation. Otherwise, please file a new issue or make a new post on the forum.

## Reporting Bugs and Issues

Reporting of bugs and issues should be done on
the [afdd-framework GitHub Issue Tracker](https://github.com/BrickSchema/afdd-framework/issues). The purview of "bugs
and issues"
includes (but is not limited to):

- missing, incomplete or incorrect definitions of afdd-framework classes
- errors, mistakes or inconsistencies in the afdd-framework ontology definition

Bug reports are most helpful when they fully explain the problem and include as many details as possible.
Some suggestions:

- **Use a clear and descriptive title** for the issue that identifies the problem
- **Include as many details as possible** about the problem, including any relevant afdd-framework/SPARQL queries, RDF
  triples,
  segments of Turtle files, Python code, etc
- **Describe the observed and expected behavior**: for example, what query did you run, what were the results, and what
  did you expect the results to be? What definition exists and what definition would you expect?
- **Describe the exact steps to reproducing the problem** where it is appropriate: did you execute a query and
- Make sure you are using the most recent version of the afdd-framework repository

## Proposing Changes to afdd-framework

The content, structure and extent of afdd-framework is determined by its community, so suggestions for how to improve
afdd-framework are
always welcome and will be taken under consideration.
Proposed changes to afdd-framework are tracked on
the [afdd-framework GitHub Issue Tracker](https://github.com/BrickSchema/afdd-framework/issues).

Effective proposals should fully explain the motivation and scope of the proposed changes, and should have at least an
initial impression of the nature of the implementation.
The more detail, the better!

## Submitting Changes to afdd-framework

Changes to afdd-framework are performed through [Pull Requests](https://github.com/BrickSchema/afdd-framework/pulls).
It is recommended that you become familiar with how
to [fork a repository](https://help.github.com/en/articles/fork-a-repo)
and [create a pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

### Setting up Development Environment

afdd-framework requires Python >= 3.6. We recommend
using [virtual environments](https://docs.python.org/3/library/venv.html) to
manage dependencies. We use [pre-commit hooks](https://pre-commit.com/) to automatically run code formatters and style
checkers when you commit.

1. Check out the afdd-framework repository (or your own fork of it)

```bash
git clone https://github.com/BrickSchema/afdd-framework
cd afdd-framework
```

2. Install the virtual environment and set up dependencies

```bash
# creates virtual environment
python3 -m venv venv

# activates virtual environment; do this every time you develop on afdd-framework
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# install pre-commit hooks
pre-commit install
```

3. Run tests to make sure the build is not broken

```bash
make test
```

4. Whenever you commit, the `pre-commit` script will run the Black code formatting tool and the flake8 style checker. It
   will automatically format the code where it can, and indicate when there is a style error. **The tools will not
   commit unformatted code**; if you see a "Failed" message, please fix the style and re-commit the code. An example of
   what this looks like is below; the failed flake8 check results in a short error report at the bottom.

```
gabe@arkestra:~/src/Brick$ git commit -m 'adding changes to Alarm hierarchy'
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gabe/.cache/pre-commit/patch1581700010.
Check Yaml...........................................(no files to check)Skipped
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

bricksrc/alarm.py:85:78: E231 missing whitespace after ','

[INFO] Restored changes from /home/gabe/.cache/pre-commit/patch1581700010.
```