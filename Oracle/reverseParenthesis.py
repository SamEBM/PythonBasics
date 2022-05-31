def reverseParentheses(strr):
    st = []
    n = len(strr)

    for i in range(n):

        # Push the index of the current
        # opening bracket
        if (strr[i] == '('):
            st.append(i)

        # Reverse the substring starting
        # after the last encountered opening
        # bracket till the current character
        elif (strr[i] == ')'):
            temp = strr[st[-1]:i + 1]
            strr = strr[:st[-1]] + temp[::-1] + strr[i + 1:]
            del st[-1]
    
    # To store the modified string
    res = ""
    for i in range(n):
        if (strr[i] != ')' and strr[i] != '('):
            res += (strr[i])
    return res

if __name__ == "__main__":
    example1 = '(abc (def) ghi)'
    example2 = '((abc) deg (ghi))'
    example3 = '(abc (d (ex) f) ghi)'
    print(reverseParentheses(example3))