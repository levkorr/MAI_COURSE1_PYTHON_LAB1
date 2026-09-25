from .constants import OPERATIONS

def calculate(rpn_tokens):
    '''Вычисляет результат выражения записанного с помощью обратной польской записи

    Args:
        rpn_tokens: Список содержащий токенизированное выражение в обратной польской записи

    Returns:
        stack[0]: Число - результат выражения
    '''
    stack = []

    for token_id, token in enumerate(rpn_tokens):
        if "." in token:
            rpn_tokens[token_id] = float(token)
        elif token.lstrip("+-").isdigit():
            rpn_tokens[token_id] = int(token)

    for token in rpn_tokens:
        if isinstance(token, (int, float)):  # Если число
            stack.append(token)
        else:  # Если операция
            # Порядок чисел важен для вычитания
            b = stack.pop()  # Последнее число в стэке
            a = stack.pop()  # Предпоследнее число в стэке

            # Выполняем операцию, убираем итог обратно в стэк
            if token in ["//", "%"]:
                if type(a) == int and type(b) == int:
                    stack.append(OPERATIONS[token](a,b))
                else:
                    raise ValueError(f"The operation {token} only works with int: {a}{token}{b}")
            else:
                stack.append(OPERATIONS[token](a,b))
    return stack[0]
