#Функция возвращает токенизированное выражение

def tokenize(expr):
    tokens = []
    state = "START"
    current_token = ""

    for char in expr: # Проходим по числам
        if state=="START": # Если это новый символ
            if char.isdigit(): # Если это число
                state="NUMBER"
                current_token+=char
            elif char in ["-","+","."]: # Если это ведущий +- или опустили целую нулевую часть числа
                current_token=char
                state="NUMBER"
            elif char in ["*","/"]: # Если это лишняя операция, присекается при валидации
                tokens.append(char)
        elif state=="NUMBER": # Если число уже началось
            if char.isdigit() or char==".": # Если это составляющая числа
                current_token+=char
            elif char in ["+","-","*","/"]: # Если это конец числа
                tokens.append(current_token)
                tokens.append(char)
                current_token=""
                state = "START"
    tokens.append(current_token) # Последний токен
    return tokens

# Функция возвращает постфиксную нотацию
def shunting_yard(tokens):
    output = []
    operators = []

    weight = {"+": 1, "-": 1, "*": 2, "/": 2} # Приоритеты операций

    for token in tokens:
        if token.lstrip("+-").isdigit() or "." in token: # Если это число
            output.append(token)
        elif token in ["+","-","*","/"]: # Если это операция
            while len(operators)!=0 and weight[operators[-1]] >= weight[token]:
                output.append(operators.pop())
            operators.append(token)
    while len(operators)!=0: # Добавляем оставшиеся операции
        output.append(operators.pop())
    if output[-1]=="": # Проверка на пустой символ
        output.pop()
    return output