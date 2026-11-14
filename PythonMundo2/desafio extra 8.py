s = 0
for n in range(1,101):
    s = s + n
print(f'Soma é {s}')
#
somadepares = 0
for c in range(2, 101):
    if c % 2 == 0:
        somadepares += c
        print(c)
print(somadepares)