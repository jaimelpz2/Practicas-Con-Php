from math import sqrt
from math import pow
from scipy.stats import norm
from scipy.stats import chi2

def generator(a,c,m,xi):
	return ((a*xi)+c)%m

def n_random_numbers(a,c,m,seed,n):
	r = []
	xi = [0,seed]
	for i in range(1,n+1):
		 xi1 = generator(a,c,m,xi[i])
		 xi.append(xi1)
		 r.append(xi1/(m-1))
	return r

def all_random_numbers(a,c,m,seed):
	r = []
	xi = [0,seed]
	i = 1
	unique_xis = dict()
	while(xi[i] not in unique_xis):
		 xi1 = generator(a,c,m,xi[i])
		 xi.append(xi1)
		 unique_xis[xi[i]] = True
		 r.append(xi1/(m-1))
		 i+=1
	return r
	

def period(a,c,m,seed):
	return len(all_random_numbers(a, c, m, seed))

def meansTest(r,d):
    print("************MeanTest\n")
    f=1-d
    m=len(r)
    suma=0
    p=f/2
    z=1-p
    print(r)
    print(f"\nalpha: {f}")
    print(f"\ntamaño del arreglo :{m}")
    for x in r:
        suma = suma+x
    #er=1/m
    print(f"\nLa suma del arreglo es: {suma}")
    rPrima=1/m*suma
    print(f"\nrPrima del Arreglo es: {rPrima}")
    print(f"Z es: {z}")
    ppf=norm.ppf(z,loc=0,scale=1)
    LLr=0.5-ppf*(1/sqrt(12*m))
    ULr=0.5+ppf*(1/sqrt(12*m))
    print(f"\nEl Punto Critico es: {ppf}")
    print(f"\nEl Limite Superior: {LLr}")
    print(f"\nEl Limite Inferior: {ULr}")
    return LLr<=rPrima<=ULr
 
    

def varianceTest(r,d):
    print("\n************VarianceTest\n")
    f=1-d #1 - 0.95 = 0.050
    p=f/2 #0.050/2 = 0.025
    z=1-p # 1-0.025 = 0.975
    m=len(r)
    suma=0
    vr=0
    ak33=0
    for x in r:
        suma = suma+x
    rPrima=1/m*suma
    print(f"\nrPrima del Arreglo es: {rPrima}")
    for x in r:
        vr=ak33+pow((x-rPrima),2)
    vr=ak33/(m-1)
    print(f"\nVr es: {vr}")
    ULvr=chi2.ppf(z,(m-1))/(12*(m-1))
    LLvr=chi2.ppf(p,(m-1))/(12*(m-1))
    print(f"\nULvr es: {ULvr}")
    print(f"\nLLvr es: {LLvr}")
    return LLvr<=vr<=ULvr
    
def chisquareTest(r,d):
    print("\n************Chis-Square Test\n")
    f=1-d
    m=len(r)
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    
    rangeSize= 1.0/m # m= 87
    startRange=0.0
    endRange=startRange+rangeSize
    print(f"rangesize : {rangeSize}\nstarRange :{startRange}\nendRange: {endRange}")
    n=sqrt(m) #9.3
    print(n)
    u=[]
    for x in range(0,10):     
        x=x/10
        z=x+1/10 
    #for x in range(0,len(r)): MI idea sobre como automatizarla pero no
    #    if r[h]>=v[h] and r[h]<=g[h] funciono y por lo tanto sigue lo de abajo
    #       count +=1
    #    if r[h]!=r[h-1]:
    #       count =0
    for h in range(0,len(r)):
        if r[h]>=0.0 and r[h]<=0.1:
            count+=1
        
        if r[h]>=0.1 and r[h]<=0.2:
            count1+=1
         
        if r[h]>=0.2 and r[h]<=0.3:
            count2+=1
        
        if r[h]>=0.3 and r[h]<=0.4:
            count3+=1
       
        if r[h]>=0.4 and r[h]<=0.5:
            count4+=1
         
        if r[h]>=0.5 and r[h]<=0.6:
            count5+=1
         
        if r[h]>=0.6 and r[h]<=0.7:
            count6+=1
        
        if r[h]>=0.7 and r[h]<=0.8:
            count7+=1
        
        if r[h]>=0.8 and r[h]<=0.9:
            count8+=1
         
        if r[h]>=0.9 and r[h]<=1.0:
            count9+=1
         
    u.append(count)
    u.append(count1)
    u.append(count2)
    u.append(count3)
    u.append(count4)
    u.append(count5)
    u.append(count6)
    u.append(count7)
    u.append(count8)
    u.append(count9)
    
    print(f"OI es: {u}")
    Ei=m/n
    print(f"Ei de Chisquare es: {Ei}")
    w=[]
    t=[]
    for i in range(0,len(u)):
       y=Ei-u[i] 
       w.append(y)
    print(f"\nNuevo Arreglo para potenciarlo: {w}\n")
    x2=[x**2 for x in w]
    print(f"\nElevado el arreglo: {x2}")
    for i in range(0,len(x2)):
        r=x2[i]/Ei
        t.append(r)
    print(f"\nX2 de o para todo Sigma: {t}\n")
    d=0
    for k in range(0,len(t)):
        d=d+t[i]
    print(f"\nX0: {d}\n")
    afk=chi2.ppf(f,(m-1))
    return d<=afk

def aboveAndBelow(r,d):
    print("\n************Runs Above And Below Test\n")
    f=1-d
    p=f/2
    z=1-p
    m=len(r)
    s=[]
    corridas=0
    for x in range(0,len(r)):
        if r[x]<=r[x-1]:
            s.append(0)    
        elif r[x]>r[x-1]:
            s.append(1)
    print(f"r es:\n {r}\n")
    print(f"Si es:\n {s}\n")
    for x in range(0,len(s)-1):
        if s[x]!=s[x+1]: 
                corridas +=1
            
    corridas=corridas   #le agregamos 2 porque a todos los resultados le faltan 2 por agregar
    print(f"\nC0 es: {corridas}")
    ppf=norm.ppf(z,loc=0,scale=1)
    uCo=((2*m)-1)/3
    print(f"\nuC0 es: {uCo}")
    oCuadradaCo=((16*m)-29)/90
    print(f"\no^2co es: {oCuadradaCo}")
    z0=abs((corridas-uCo)/sqrt(oCuadradaCo))
    print(f"\nZ0 es: {z0}")
    return z0 <= ppf
    

generatorValues = {
		'a': 121,
		'c': 553,
		'm': 177,
		'seed': 23
	}

generatorValues2 = {
		'a': 16807,
		'c': 0,
		'm': 2147483647,
		'seed': 1,
        'n': 100
	}

ar=(n_random_numbers(**generatorValues2))
er=(all_random_numbers(**generatorValues))
ed=.95
print("\n\nMETODOS REALIZADOS POR DIFERENTES VALORES {1}\n\n")#generator1
print(meansTest(er,ed))
print(varianceTest(er,ed))
print(chisquareTest(er,ed))
#aboveAndBelow(er,ed)

print("\n\nMETODOS REALIZADOS POR DIFERENTES VALORES {2}\n\n")#generato2
print(meansTest(ar,ed))
print(varianceTest(ar,ed))
print(chisquareTest(ar,ed))
print(aboveAndBelow(ar,ed))


