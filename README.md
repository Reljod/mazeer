# Mazeer

A simple maze builder game that let's you build a maze using tunnels, ladders, slides, etc.
You can then try and play the maze that you build and challenge your friends!

### Dependencies

- python-3.10
- pygame-2.5

## Get Started

1. Clone the repository.
2. Go to root folder and install the dependencies.

```sh
pip install -r requirements.txt
```

3. Then run the game.

```sh
python main.py
```

## Contribute

1. Clone the repository.
2. Go to root folder and install the dependencies.

```sh
pip install -r requirements.txt
```

3. Install dev dependencies.

```sh
pip install -r requirements_dev.txt
```

4. Test the game.

```sh
python main.py
```

5. Add external packages with following:

```sh
# For prod dependencies
pip install [PACKAGE] && pip freeze | grep [PACKAGE] >> requirements.txt

# For dev dependencies
pip install [PACKAGE] && pip freeze | grep [PACKAGE] >> requirements_dev.txt

# Then update the packages equality from == to ~=, example:
# -> From pygame==2.5.0 to pygame~=2.5.0
# to install latest patches.
```
