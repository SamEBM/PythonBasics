if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = set(arr)
    print(scores)
    final = list(scores)
    final.sort(reverse=True)
    print(final[1])