import sys
from Task.Task1 import solution as task1
from Task.Task2 import solution as task2


if __name__ == "__main__":
    print("Task 1")
    S = input("Input your string: ")
    result = task1.solution(S)
    if result == -1 or len(S) not in range(1,200):
        print("You didn't input your string or your string are incorrect!")
    else:
        print(result)

    # print("Task 2")
    # moves = input("Input your moves: ")
    # count = task2.solution(moves)
    # if count == -1 or len(S) not in range(1,50):
    #     print("You didn't input your moves or your moves are incorrect!")
    # else:
    #     print(count)
    
    # print("Task 3")
    # S = input("Input your string: ")
    # result = task1.solution(S)
    # if result == -1 or len(S) not in range(1,200):
    #     print("You didn't input your string or your string are incorrect!")
    # else:
    #     print(result)
