import sys
from Task.Task2 import solution as task2


if __name__ == "__main__":
    print("Task 2")
    moves = input("Input your moves: ")
    count = task2.solution(moves)
    if count == -1 or len(moves) > 50:
        print("You didn't input your moves or your moves are incorrect!")
    else:
        print(count)
    
