
#fungsi tahun kabisat
def tahun_kabisat(tahun):
    if tahun % 400==0:
        return True
    if tahun % 100==0:
        return False
    if tahun % 4==0:
        return True
    else:
        return False
tahun=int(input("masukkan tahun: "))
print ("")
if tahun_kabisat(tahun):
    print (tahun,"adalah tahun kabisat")
else:
    print (tahun,"adalah bukan tahun kabisat")
    


