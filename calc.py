def calc(_num1, _num2):
    sum = _num1 + _num2
    difference = _num1 - _num2
    multiply =  _num1 * _num2
    divide = float(_num1) / _num2
    return [sum, difference, multiply, divide]

list = calc(10, 20)
print (list)
