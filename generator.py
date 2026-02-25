# generator adalah fungsi yang bisa pause dan resume execution
#ketika fungsi generator dipanggil bakal return generator object sebagai iterator
# kode didalam fungsi nggk dieksekusi tp baru dicompile. fungsi baru tereksekusi kalo diiterasi di atas generator


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# for num in count_up_to(5):
#     print(num)

# def simple_gen():
#     yield "Emil"
#     yield "Tobias"
#     yield "Linus"

# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))


#generator expression - creates a generator
# n = int(input("Sampai bilangan berapa?"))
# gen_exp = (x * x for x in range(n))
# print(list(gen_exp))

# total = sum(x * x for x in range(n))
# print(total)

#fibonacci sequence generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(15):
    print(next(gen))

