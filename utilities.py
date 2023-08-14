
import numpy as np
import math

def GlobalSearch (GS,n,pl):
    if GS == 0:
        IS = np.random.permutation(n)
    elif GS == 1: # Nearest Neighbour
        s = np.random.randint(n)
        D2=D
        D2=np.array(D2)
        n= len(D2)
        IS=[]
        IS.append(s)
        for i in range(1,n):
            s=IS[-1]
            D2[s,:] = np.inf
            temp = list(D2[:,s])
            IS.append(temp.index(min(temp)))
    else:  # Domino sequence operator 
        D2=np.matrix(np.ones((n+1,n+1)) * np.inf)
        for i in range(n):
            for j in range(n):
                D2[i,j]=D[i,j]
        #pl = m[1]      # set the number of players (pl).
        c = np.random.permutation (n)
        c = c+1
        m=math.ceil(n/pl)
        c=np.array(c)
        c.resize(pl,m)
        I = np.random.randint(1,n+1)
        E=[]
        E.append(I)
        T=[]
        T.append(I)
        c[c==I] = 0
        while sum(sum(c)) > 0:
            for i in range(pl):
                FromTo = c[i,:]
                Dis_E = []
                Dis_T = []
                for j in range (m):
                    Dis_E.append(D2[FromTo[j]-1,E[0]-1]) 
                    Dis_T.append(D2[T[-1]-1,FromTo[j]-1])
                minE = min(Dis_E)
                minT = min(Dis_T)
                Id_minE = np.argmin(Dis_E)
                Id_minT = np.argmin(Dis_T)
                if minE <= minT: 
                    E.insert(0,FromTo[Id_minE])
                    c[c==FromTo[Id_minE]] = 0
                else:
                    T.append(FromTo[Id_minT])
                    c[c==FromTo[Id_minT]] = 0
        E = np.array(E)
        E = E[E!=0]
        T = np.array(T)
        T = T[T!=0]
        E=list(E)
        E.pop(-1)
        T=list(T)
        IS = E+T
        IS = (np.array(IS))-1
    IS = list(IS)
    #IS = np.array(IS)
    return IS

# -----

def LocalSearch (x,LS):   # Random using Reversion, Swap, Insertion
    if LS == 0:
        m = np.random.randint(1, 4) # The Combination of Swap, Reversion, and Insertion
    else:
        m = LS
    x = list (x)
    n = len(x)
    if m == 1: # SWAP
        for i in range(np.random.choice(range(2), 1)[0]):
            i1, i2 = np.random.choice(range(n), 2, False)
            x[i1], x[i2] = x[i2], x[i1]
    elif m == 2: # REVERSION (2-OPT)
        i = np.random.randint(0,n,2)
        i1 = min(i)
        i2 = max(i)
        #z=x
        #tuple(z)
        #y=x[i1:i2]
        #y=y[::-1]
        #x=z
        #x=np.array(x)
        #for i in range(i1,i2):
        #    x[i]=y[i-i1]
        x=list(x)
        x[i1:i2:1]= reversed(x[i1:i2:1])
    elif m == 3: # INSERTION
        temp = x[np.random.choice(range(n), 1)[0]]
        x=list(x)
        x.remove(temp)
        x.insert(np.random.choice(range(n-1), 1)[0], temp)
    #x=np.array(x)
    return x

