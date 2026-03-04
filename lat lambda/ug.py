# def konversi_waktu(jam, menit, format_24):
#     str_jam = str(jam)
#     str_menit = str(menit)
#     if jam > 24 or menit > 59:
#         return("Opo iki")
#     elif format_24:
#         if jam < 10:
#             str_jam = "0" + str_jam
#         if menit < 10:
#             str_menit = "0" + str_menit
#         if menit == 0:
#             str_menit = "00"
#         return(f"Jam : {str_jam}:{str_menit}")
        
#     else:
#         if jam == 24:
#             str_jam = "12"
#             if menit == 0:
#                 str_menit = "00"
#             return(f"Jam : {str_jam}:{str_menit} AM")
            
#         if jam > 12:
#             jam = jam - 12
#             if menit < 10:
#                 str_menit = "0" + str_menit
#             return(f"Jam : {jam}:{str_menit} PM")
            
#         else:
#             if jam < 10:
#                 str_jam = "0" + str_jam
#             if menit < 10:
#                 str_menit ="0" + str_menit
#             return(f"Jam : {str_jam}:{str_menit} AM")
        
        
    

        
# #Jangan dirubah
# if __name__ == "__main__":
#     jam = int(input())
#     menit = int(input())
#     format = input()
#     fformat = True if format == "true" else False
#     print(konversi_waktu(jam,menit,fformat))

def f(x):
    i = 1
    while i <= 3:
        hasil = x^2 + 2*x +3
        x = hasil
        i + 1
    return(hasil)
x = int(input())
f(x)