
if __name__ == "__main__":
    # print("Task 1")
    # from Task.Task1 import solution as task1
    # S = input("Input your string: ")
    # result = task1.solution(S)
    # if result == -1 or len(S) not in range(1,200):
    #     print("You didn't input your string or your string are incorrect!")
    # else:
    #     print(result)

    # print("Task 2")
    # from Task.Task2 import solution as task2
    # moves = input("Input your moves: ")
    # count = task2.solution(moves)
    # if count == -1 or len(S) not in range(1,50):
    #     print("You didn't input your moves or your moves are incorrect!")
    # else:
    #     print(count)
    
    # print("Task 3")
    # from Task.Task3 import solution as task3
    # S = input("Input your string: ")
    # count = task3.solution(S)
    # if len(S) not in range(1,20):
    #     print("You didn't input your string or your string are incorrect!")
    # else:
    #     print(count)

    # print("Task 4")
    # from Task.Task4 import solution as task4
    # X = int(input("Input your X: "))
    # N = int(input("Input size of your array A: "))
    # print("Enter you array A:")
    # A = []
    # for i in range(N):
    #     pos = int(input(f"A[{i}] = "))
    #     A.append(pos)
    # count = task4.solution(X, A)
    # if count == -1:
    #     print("The frog is never able to jump to the other side of the river")
    # else:
    #     print(f"The earliest time when the frog can jump to the other side of the river is: {count} seconds")
    
    # print("Task 5")
    # from Task.Task5 import solution as task5
    # result_1 = task5.solution([3, 1, 2])
    # result_2 = task5.solution([1, 2, 3, 4])
    # result_3 = task5.solution([7, 7, 7])
    # result_4 = task5.solution([10000])
    # print(f"The total time that clients need to wait for all ordered items:")
    # print(f"Given T = [3, 1, 2], return: {result_1}")
    # print(f"Given T = [1, 2, 3, 4], return: {result_2}")
    # print(f"Given T = [7, 7, 7], return: {result_3}")
    # print(f"Given T = [10000], return: {result_4}")

    # print("Task 6")
    # from Task.Task6 import solution as task6
    # result_1 = task6.solution([2, 4, 1, 3, 4, 6, 2, 4, 1, 6])
    # result_2 = task6.solution([5, 1, 2, 6, 6, 1, 3, 1, 4, 3, 4, 3, 4, 6, 1, 2, 4, 1, 6, 2])
    # result_3 = task6.solution([1, 5, 3, 3, 1, 3])
    # result_4 = task6.solution([3, 4])
    # print(f"The minimum number of domino tiles that must be removed:")
    # print(f"Given A = [2, 4, 1, 3, 4, 6, 2, 4, 1, 6], return: {result_1}")
    # print(f"Given A = [5, 1, 2, 6, 6, 1, 3, 1, 4, 3, 4, 3, 4, 6, 1, 2, 4, 1, 6, 2], return: {result_2}")
    # print(f"Given A = [1, 5, 3, 3, 1, 3], return: {result_3}")
    # print(f"Given A = [3, 4], return: {result_4}")

    print("Task 7")
    from Task.Task7 import solution as task7
    result_1 = task7.solution(["RR", "GR", "RG", "GR", "GR", "RR"])
    result_2 = task7.solution(["GG", "GG", "RR", "GG", "RR"])
    result_3 = task7.solution(["RG", "GR", "RG", "GR"])
    result_4 = task7.solution(["RG", "RG", "RG"])
    print(f"The minimum number of domino tiles that must be removed:")
    print(f'Given A = ["RR", "GR", "RG", "GR", "GR", "RR"], return: {result_1}')
    print(f'Given A = ["GG", "GG", "RR", "GG", "RR"], return: {result_2}')
    print(f'Given A = ["RG", "GR", "RG", "GR"], return: {result_3}')
    print(f'Given A = ["RG", "RG", "RG"], return: {result_4}')
