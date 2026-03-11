def square_shape(length): # no need to use 3 variables
        print (". " * length)
        for _ in range(length - 2):
            print (". " + "  " * (length - 2) + ".")
        print (". " * length)

n = int(input("Masukkan panjang: "))
square_shape(n)