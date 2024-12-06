
numbers = [int(el) for el in input().split()]
# numbers = [int(el) for el in '1 2 3 4 5 4 5 6 7 7 7 7 4 4'.split()]
print(*sorted(filter(lambda x: numbers.count(x) > 1, set(numbers))))


# res_set = set()
# for el in numbers:
#     if numbers.count(el) > 1:
#         res_set.add(el)
# print(*sorted(res_set))
