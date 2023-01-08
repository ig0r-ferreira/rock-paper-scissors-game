# Rock Paper Scissors Game

A CLI implementation of the rock-paper-scissors game in which you play against the computer.

![Rock, Paper, Scissors game](assets/rpsgame.gif)


## Run only

Use [pipx](https://pypa.github.io/pipx/) to run without permanently installing.

```
pipx run --spec git+https://github.com/ig0r-ferreira/rock-paper-scissors-game.git rpsgame
```
**Note: Characters may not display correctly on Windows, if this happens, try the installation.**

## Install and Run

### [pipx](https://pypa.github.io/pipx/)
  
1. Install in an isolated environment with:
    ```
    pipx install git+https://github.com/ig0r-ferreira/rock-paper-scissors-game.git
    ```

2. Run:
    ```
    rpsgame
    ```

### [poetry](https://python-poetry.org/)

1. Open a terminal on your desktop or wherever you like and run the command below to clone the project:
    ```
    git clone https://github.com/ig0r-ferreira/rock-paper-scissors-game.git
    ```

2. Go to the project folder with:
    ```
    cd rock-paper-scissors-game
    ```

3. Install with:
    ```
    poetry install --without dev
    ```

4. And finally run:
    ```
    poetry run rpsgame
    ```