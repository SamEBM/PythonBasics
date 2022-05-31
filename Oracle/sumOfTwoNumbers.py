from itertools import permutations

if __name__ == "__main__":
    
    numbers = [1, 2, 3, 4, 5, 4]
    target = 8

    # USING LIST COMPREHENSION
    # solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == target]
    # print('Solutions: ', solutions)

    # USING FOR LOOPS
    # print(number_dict)
    # for i in range(len(numbers)):
    #     for j in range(len(numbers)):
    #         if(numbers[i] != numbers[j] and numbers[i] + numbers[j] == target):
    #             print((numbers[i], numbers[j]))

    numbers = [1,3,4,5,6,2]
    target = 5
    # number_dict = {}
    # pairs = []
    # for num in numbers:
    #     number_dict[num] = number_dict.get(num, 0) + 1 # Lleva el conteo de ocurrencias
    #     complement = target - num
    #     if complement in number_dict.keys():
    #         pairs.append((num, complement))
    #         number_dict.pop(num)
    #         number_dict.pop(complement)
    # print(set(pairs))

    number_dict = {}
    res = []
    for i,num in enumerate(numbers):
        complement = target - num
        if complement in number_dict:
            res = [number_dict[complement], i]
            break
        else:
            number_dict[num] = i
    print(res)
