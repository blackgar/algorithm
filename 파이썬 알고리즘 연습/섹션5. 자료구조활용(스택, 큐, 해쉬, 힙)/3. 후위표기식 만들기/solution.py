import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    expression = input()
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ["*", "/", "+", "-"]
    back_expression = ""
    stack = []
    for i in range(len(expression)):
        print("expression[i]", expression[i])
        if expression[i] in number:
            back_expression += expression[i]
        else:
            if expression[i] =="(":
                stack.append(expression[i])
            elif expression[i] == ")":
                for j in range(1, len(stack)+1):
                    if stack[-j] != "(":
                        back_expression += stack.pop()
                        break
                    if stack[-j] == "(":
                        stack.pop()
            elif expression[i] in operator[:2]:
                for j in range(1, len(stack)+1):
                    if stack[-j] in operator[2:]:
                        back_expression += expression[i]
                        continue
                    elif stack[-j] in operator[:2]:
                        back_expression += stack.pop()
                        stack.append(expression[i])
                        break

            elif expression[i] in operator[2:]:
                stack.append(expression[i])
        print("후기표위식", back_expression)
        print("스택", stack)
    print(back_expression)
