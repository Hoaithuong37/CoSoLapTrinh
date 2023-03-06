M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    print("Phai tra=",S*M1,sep=(""))
elif 101<=S<=150:
    print("Phai tra==",(M1*100)+((S-100)*M2),sep=(""))    
else:
    print("Phai tra=",(M1*100)+(M2*50)+((S-150)*M3),sep=(""))