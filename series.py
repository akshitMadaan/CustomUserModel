def nTerm(N):
    n = 0
    if(N % 2 == 0):
        n = (N * N) - 1
    else:
        n = (N * N) + 1
    print(n);

N = 9
nTerm(N)

