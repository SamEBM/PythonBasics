if __name__ == "__main__":
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    expression = "[((1+2) * (3-1)]"
    stack = []

    for c in expression:
        if c in open_list:
            stack.append(c)
        elif c in close_list:
            char_index = close_list.index(c)
            if len(stack) > 0 and open_list[char_index] == stack[-1]:
                stack.pop()
            else:
                res = 'Unbalanced'
    
    if len(stack) == 0:
        res = 'Balanced'
    else: 
        res = 'Unbalanced'
    
    print(stack)
    print(res)