## Game Theory Puzzle: Dice Rolling Game
From [@joe_shipman](https://twitter.com/joe_shipman/status/1340386895860297730?s=20) on Twitter.
## Problem
You and your friend each roll a pair of dice where only the roller can see them. If you don’t like the total you pick them up and try again. Your friend then also decides if he wants to try again. High total wins.

What’s the result of optimal play?

## Solution
First player stands on 8 and up, Second player stands on 8 and up if first player rerolls, but stands on 9 and up if first player stands.

Second player advantage is 

<img src="https://latex.codecogs.com/gif.latex?(\frac{5}{72})^2&space;=&space;0.482%" title="(\frac{5}{72})^2 = 0.482%" />

[Link to Tweet](https://twitter.com/joe_shipman/status/1341194220263104512?s=20)  

## Running Monte-Carlo Simulation
Update the desired number of iterations in your simulation by modifying `n_iter` in `config.yml` and run the following command in your terminal.

```python
python main.py
```

