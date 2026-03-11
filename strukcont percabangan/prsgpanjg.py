#kosong ato void
def draw_hollow_square(panjang, lebar, karakter):
    # Print top border
    print(karakter * panjang)
    
    # Print middle rows (hollow part)
    for _ in range(lebar - 2):
        print(karakter + ' ' * (panjang - 2) + karakter)
    
    # Print bottom border (only if width > 1)
    if lebar > 1:
        print(karakter * panjang)

# Example usage:
pnjg = int(input("Tentukan panjang: "))
lebr = int(input("Tentukan lebar: "))
karakter = input("Tentukan karakter: ")
draw_hollow_square(pnjg, lebr, karakter)