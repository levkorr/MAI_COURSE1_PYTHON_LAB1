def calculate(rpn_tokens):
    stack = []

    for token in rpn_tokens:
        if token.lstrip("+-").isdigit() or "." in token: # Если число
            stack.append(float(token))
        else: # Если операция
            # Порядок чисел важен для вычитания
            b = stack.pop() # Последнее число в стэке
            a = stack.pop() # Предпоследнее число в стэке

            # Выполняем операцию, убираем обратно в стэк
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "/":
                stack.append(a/b)
            elif token == "*":
                stack.append(a*b)

    return stack[0]
