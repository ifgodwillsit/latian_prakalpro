n = 5
# Upper left pyramid
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
# Lower left pyramid
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * i)