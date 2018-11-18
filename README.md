# 2048
Simple port of the game 2048 to test bots

Requirements
* Python 3 for the python version

To play
1. choose your language
2. run `<interpretter> main.<extension>`, e.g. `python main.py`
3. choose bot or human
4. if human:
    1. press an arrow key, then "enter" to move
5. if bot:
    1. select number of games to play
    2. select strategy to use to play
    3. highest game, score, and tile will be displayed at end

Bot strategies must always return a string corresponding to a move: `up`, `down`, `left`, or `right`.