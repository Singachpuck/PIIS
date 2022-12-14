# Chess AI

In this project you can see implementation of 3 different algorithms:
- Negamax
- NegaScout
- Principal Variation Search

You will play for WHITE against AI that plays for BLACK.
Specify the move in the following format: ```a2a4```

### Application accepts 2 command line arguments:
- ```-d, --depth ``` - depth of the search
- ```-a --agent``` - name of the Agent to use

### Example of usage:

- ```python.exe main.py -d 3 -a PVSAgent```
- ```python.exe main.py -d 3 -a NegamaxAgent```
- ```python.exe main.py -d 3 -a NegaScoutAgent```