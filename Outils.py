def sec_to_time(s):
        if s < 60: return '{:>2} s'.format(s)
        elif s < 3600: return '{:>2} min {:>2} s'.format(s//60,s%60)
        elif s < 86400: return '{:>2} h {:>2} min {:>2} s'.format(s//3600,s%3600//60,s%60)
        elif s < 31536000: return '{:>3} j {:>2} h {:>2} min {:>2} s'.format(s//86400,s%86400//3600,s%3600//60,s%60)
        else: return '{:>4} ans {:>3} j {:>2} h {:>2} min {:>2} s'.format(s//31536000,s%31536000//86400,s%86400//3600,s%3600//60,s%60)
        

def Mots_c_b(c, b, f_nec = lambda l: True, f_suf = lambda l: True):
        L1 = []

        for j in range(b) :
                L1 += [(j,)]

        #print('First step done')
        
        for n in range(c - 1):
                L = [i for i in L1]
                L1 = []
                for l in L:
                        for j in range(b):
                                e = (l) + (j,)
                                if f_suf(e):
                                        L1 += [e]
                #print(i/(c - 1)*100, '%', sep = ' ')
        L = [e for e in L1 if f_nec(e)]
        return L

def nbr_chiffre(n):
    k = 0
    while 10 ** k <= n:
        k += 1
    return k

def fact(N):
	F = 1
	for i in range(2, N + 1):
		F = F * i
	return F

def Cnk(k,n): return fact(n) // (fact(k) * fact(n-k))

def SommeListe(L, a, b):
	if a > b or b > len(L): return -1
	S = 0
	for i in range(a, b):
		S += L[i]
	return S

def AllDiff(L):
        for i in range(len(L)):
                if L[i] in L[0:i] or L[i] in L[i+1:len(L)]: return False
        return True

def Sqrt(n,a):
    if a == 0 or a == 1: return a
    def f(x):
        return x**n - a
    h = 10**(-13)
    d = 100
    while abs(f(d)) > h :
        d = d - f(d) / (f(d + h) - f(d)) * h
        #print(d,',',end = '')
    if int(d) ** 2 == a : d = int(d)
    if (int(d) + 1) ** 2 == a : d = int(d) + 1
    return abs(d)

def racineEntiere(N):
        A = Sqrt(2,N)
        if type(A) == type(5): return A
        else: return False

def fusion(L1, L2):
	L = []
	for i in range (len(L1) + len(L2)):
		if L1 == []:
			return L + L2
		elif L2 == []:
			return L + L1
		elif L1[0] <= L2[0]:
			L += [L1[0]]
			L1.pop(0)
		else: 
			L += [L2[0]]
			L2.pop(0)
	return L

def tri(L):
	if len(L) <= 1:
		return L
	return fusion(tri(L[:len(L)//2]), tri(L[len(L)//2:]))

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    f = 5
    while f*f <= n:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def expmodk(x, y, k):
    if y == 0 :
        return 1
    tip_top = y//2
    z = Expmodk(x, tip_top, k)
    a = z*z%k
    if y%2==0 :
        return a
    else :
        return a*(x%k)%k

def décompo(n):
    i = 2
    l = []
    if isPrime(n):
        l.append(n)
        return l
    while i <= n:
        while n % i == 0:
            l.append(i)
            n = n // i
            if isPrime(n):
                l.append(n)
                return l
        i += 1
    return l

