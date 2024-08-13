
def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"

    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")



============================================================================================================


def are_brackets_balanced(s):
    stack = []
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        else:
            if stack and ((stack[-1] == '(' and ch == ')') or
                          (stack[-1] == '{' and ch == '}') or
                          (stack[-1] == '[' and ch == ']')):
                stack.pop()
            else:
                return False
    return not stack

expr = "{()}[]"

# Function call
if are_brackets_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")

