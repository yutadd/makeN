import copy
def minus(a,b):
    return a-b
def plus(a,b):
    return a+b
def div(a,b):
    return a//b
def mul(a,b):
    return a*b
def baseN(i,n):
    if i//n<4:
        return str(i//n)+str(i%n)
    else:
        return baseN(i//n,n)+str(i%n)


def permutations(arr:list[int]):
    '''
    この関数は、与えられた整数のリストのすべての順列を生成します。
    順列は、リストの要素を再配置するすべての可能な方法を表します。 
    たとえば、[1, 2, 3]の順列は[1, 2, 3]、[1, 3, 2]、[2, 1, 3]、[2, 3, 1]、[3, 1, 2]、[3, 2, 1]です。
    この関数は再帰的に動作します。リストの各要素について、その要素を取り除いた残りのリストの順列を生成し、
    取り除かれた要素をそれぞれの順列の先頭に追加します。
    
    Parameters:
    list[int]: 順列を生成するための整数のリスト。
    
    Returns:
    list[int]: 入力リストのすべての可能な順列を含むリスト。
    '''
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        m = arr[i]
        rem_list = arr[:i] + arr[i+1:]
        for p in permutations(rem_list):
            result.append([m] + p)
    return result
def make_operater_pattern(variable_count:int)->list[list[str]]:
    '''
    この関数は、指定された変数の数に基づいて演算子のパターンを生成します。
    生成されるパターンは、4つの演算子（加算、減算、乗算、除算）のすべての可能な組み合わせを表します。
    たとえば、変数の数が3の場合、この関数は2つの演算子のすべての可能な組み合わせを生成します。
    
    Parameters:
    variable_count (int): 演算子のパターンを生成するための変数の数。
    
    Returns:
    list[list[str]]: 生成された演算子のパターンのリスト。
    '''
    result=[]
    pattern_length=variable_count-1
    for x in range(4**pattern_length):
        result.append(list(baseN(x,4)))
    return result
def calculate(pattern, numbers, operations):
    '''
    この関数は、指定されたパターン、数字、および演算子を使用して計算を実行します。
    
    Parameters:
    pattern (list[str]): 演算子のパターン。
    numbers (list[int]): 使用する数字。
    operations (dict): 演算子とそれに対応する関数の辞書。
    
    Returns:
    int: 計算の結果。
    '''
    result = numbers[0]
    expression = str(numbers[0])
    for i in range(len(pattern)):
        result = operations[pattern[i]](result, numbers[i+1])
        expression += " " + str(operation_symbols[pattern[i]]) + " " + str(numbers[i+1])
    return result, expression

operations = {'0': plus, '1': minus, '2': mul, '3': div}
operation_symbols = {'0': '+', '1': '-', '2': '*', '3': '/'}
while True:
    target=int(input("作りたい数字を入力してください"))
    elements=[]
    try:
        elements=[int(x) for x in input("材料となる数字を入力してください").split()]
    except Exception as e:
        continue
    operation_patterns = make_operater_pattern(len(elements))
    number_permutations = permutations(elements)
    
    for numbers in number_permutations:
        for pattern in operation_patterns:
            result, expression = calculate(pattern, numbers, operations)
            if result == target:
                print("Found solution: ", expression, "=", target)
                break
    break
