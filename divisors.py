def divisors(_num):
    div_list = []
    for i in range(1, _num + 1):
        if _num % i == 0:
          div_list.append(i)
    return div_list

print(divisors(76))
