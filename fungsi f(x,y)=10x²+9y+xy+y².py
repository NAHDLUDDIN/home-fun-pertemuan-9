
#fungsi f(x,y)=10x²+9y+xy+y²
def f(x,y):
    return (10*x*x)+(9*y)+(x*y)+(y*y)
x=int(input("masukkan x: "))
y=int(input("masukkan y: "))
print("hasilnya adalah: ",f(x,y))
