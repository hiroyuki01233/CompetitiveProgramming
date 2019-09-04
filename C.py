L,R = input().split()
L = int(L)
R = int(R)

if L == 0:
    if R >= 1868 and R <= 1911:
        K = int(R) - 1867
        print("M" + str(K))
    elif R >= 1912 and R <= 1925:
        K = int(R) - 1911
        print("T" + str(K))
    elif R >= 1926 and R <= 1988:
        K = int(R) - 1925
        print("S" + str(K))
    elif R >= 1989 and R <= 2016:
        K = int(R) - 1988
        print("H" + str(K))
elif L == 1:
    K = int(R) + 1867
    print(K)
elif L == 2:
    K = int(R) + 1911
    print(K)
elif L == 3:
    K = int(R) + 1925
    print(K)
elif L == 4:
    K = int(R) + 1988
    print(K)
