def validate_brackets(txt_input):

    stack = []
    open_bracket = ['{', '[', '(']
    close_bracket = ['}', ']', ')']

    for i in range(len(txt_input)):
        if txt_input[i] in open_bracket:
            stack.append(txt_input[i])

        elif txt_input[i] in close_bracket:
            index = close_bracket.index(txt_input[i])

            if len(stack) > 0 and stack[-1] == open_bracket[index]:
                stack.pop()
            else:
                return False
            break
 
    if len(stack) != 0:
        return False
    else:
        return True


