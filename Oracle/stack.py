# Stack is LIFO (Last In First Out)
# Push/Pop: O(1)
# Search value: O(n)

# Usages:
# Function Calls, Web Page Return Button, etc

from collections import deque


if __name__ == "__main__":
    pages_stack = []
    pages_stack.append('https://www.page.com/index')
    pages_stack.append('https://www.page.com/about')
    pages_stack.append('https://www.page.com/contact')

    print(pages_stack.pop()) # Get last element pages_stack[-1]

    pages_stack2 = deque()
    pages_stack2.append('https://www.page.com/index')
    pages_stack2.append('https://www.page.com/about')
    pages_stack2.append('https://www.page.com/contact')
    print(pages_stack2.pop())
    print(pages_stack2.count('https://www.page.com/index'))
