import numpy as np
import pandas as pd
print("----------TIC TAC TOW-----------")
print("_________the Game Begins________")
print("1st Player Has 0\nStart Game")
print("______________________________________________________")
ar=np.full([3,3],'.')
box=pd.DataFrame(ar,index=[1,2,3],columns=[1,2,3])
print(box)
n=0
while n<9:
    a=int(input("Enter Row position: "))
    b=int(input("Enter column position: "))
    if 1<=a<=3 and 1<=b<=3:
        if box[b][a]==0 or box[b][a]=="x":
            print("!!!this position is already taken!!!")
            continue
        else:
            n+=1
            if n%2!=0:
                N=0
            else:
                N='x'
            box[b][a]=N
            print("==================")
            print(box)
            c1=co1=d1=d2=0
            for A in range(1,4):
                c1=co1=0
                for B in range (1,4):
                    if box[A][B]==N:
                        c1+=1
                    if box[B][A]==N:
                        co1+=1
                    if A+B==4 and box[A][B]==N:
                        d2+=1
                    if (A,B)==(B,A) and box[A][B]==N:
                        d1+=1
                if c1==3 or d1==3 or d2==3 or co1==3:
                    print("--------------------------------")
                    n=10
                    print("|",N,"|","\n***Wins The Game***")
                    break
            if n==10:
                break
    else:
        print("!!!Enter valid position!!!")
else:
    print("Opss!!!!!!!: Game Tie :!!!!!!!BLNT")
print("___________G a m e O V E R_________")
