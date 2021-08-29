# Games
Programming different games using python and accepting user input in some cases.

## TicTacToe 
### Example game scenario after running tictac.py
```
> python tictac.py 
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', '[7]', '[8]']
Enter your value: x
Enter your position: 2
['[0]', '[1]', 'x']
['[3]', '[4]', '[5]']
['[6]', '[7]', '[8]']
Enter your value: o
Enter your position: 5
['[0]', '[1]', 'x']
['[3]', '[4]', 'o']
['[6]', '[7]', '[8]']
Enter your value: x
Enter your position: 8
['[0]', '[1]', 'x']
['[3]', '[4]', 'o']
['[6]', '[7]', 'x']
Enter your value: x
Enter your position: 1
Please let o play instead!
Enter your value: o
Enter your position: 1
['[0]', 'o', 'x']
['[3]', '[4]', 'o']
['[6]', '[7]', 'x']
Enter your value: x
Enter your position: 4
['[0]', 'o', 'x']
['[3]', 'x', 'o']
['[6]', '[7]', 'x']
Enter your value: o
Enter your position: 6
['[0]', 'o', 'x']
['[3]', 'x', 'o']
['o', '[7]', 'x']
Enter your value: x
Enter your position: 7
['[0]', 'o', 'x']
['[3]', 'x', 'o']
['o', 'x', 'x']
Enter your value: o
Enter your position: 0
['o', 'o', 'x']
['[3]', 'x', 'o']
['o', 'x', 'x']
Enter your value: x
Enter your position: 3
['o', 'o', 'x']
['x', 'x', 'o']
['o', 'x', 'x']
no more plays available
```


### Another scenario of the game
```
> python tictac.py
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', '[7]', '[8]']
Enter your value: x
Enter your position: 7
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', 'x', '[8]']
Enter your value: o
Enter your position: 8
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', 'x', 'o']
Enter your value: x
Enter your position: 1
['[0]', 'x', '[2]']
['[3]', '[4]', '[5]']
['[6]', 'x', 'o']
Enter your value: o
Enter your position: 2
['[0]', 'x', 'o']
['[3]', '[4]', '[5]']
['[6]', 'x', 'o']
Enter your value: x
Enter your position: 3
['[0]', 'x', 'o']
['x', '[4]', '[5]']
['[6]', 'x', 'o']
Enter your value: o
Enter your position: 4
['[0]', 'x', 'o']
['x', 'o', '[5]']
['[6]', 'x', 'o']
Enter your value: x
Enter your position: 5
['[0]', 'x', 'o']
['x', 'o', 'x']
['[6]', 'x', 'o']
Enter your value: o
Enter your position: 5
That spot has been taken, please choose another one
Enter your value: o
Enter your position: 1
That spot has been taken, please choose another one
Enter your value: o
Enter your position: 0
['o', 'x', 'o']
['x', 'o', 'x']
['[6]', 'x', 'o']
o is the winner!
```

### Additional scenario of the game
```
> python tictac.py
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', '[7]', '[8]']
Enter your value: x
Enter your position: 8
['[0]', '[1]', '[2]']
['[3]', '[4]', '[5]']
['[6]', '[7]', 'x']
Enter your value: o
Enter your position: 3
['[0]', '[1]', '[2]']
['o', '[4]', '[5]']
['[6]', '[7]', 'x']
Enter your value: x
Enter your position: 6e
please use valid integer for positions
```
