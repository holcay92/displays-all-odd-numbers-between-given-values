# python h.halil olcay
try: min_value, max_value = map(int, input().split())

except :     print('inputs must be integers');exit()

for item in range(min_value, max_value+1):
    if item % 2 != 0: print(item)