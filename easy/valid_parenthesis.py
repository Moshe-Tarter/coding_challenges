'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


def check(chars: str) -> bool: 
    stack = []
    for char in chars:
        if char in ['[', '(', '{']:
            stack.append(char)
        elif char == '}':
            temp = stack.pop()
            if temp != '{':
                return False
        elif char == ']':
            temp = stack.pop()
            if temp != '[':
                return False
        else:
            temp = stack.pop()
            if temp != '(':
                return False

    return True


if __name__ == '__main__':
    print(check('()()([[[)]]])[][]'))

