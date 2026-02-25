cek_angka = lambda x, y, z: True if (x != y != z and (x + y == z or y + z == x or x + z == y)) else False

a = print("Test Case: ")
print("(1,2,3)=", cek_angka(1,2,3))
print("(1,3,3)=", cek_angka(1,3,3))
print("(3,2,3)=", cek_angka(3,2,3))
print("(3,3,2)=", cek_angka(3,3,2))

print("\nHasil yang benar:")
print("True")
print("False")
print("False")
print("False")