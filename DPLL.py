class Tree(object):
    def __init__(label,left,right):
        self.labe=label
        self.left=left
        self.right=right

def recu(claus,inter):
    aux=[]
    copia=[]
    if len(claus)==0:
        return True,inter
    for j in claus:
        if len(j)!=0:
            let=j[len(j)-1]
            let=let[len(let)-1]
        else:
            return False,inter
    inter[let]=True
    envi=[]
    for j in claus:
        if not let in j:
            aux=[]
            for i in j:
                if i!="-"+let:
                    aux.append(i)
            envi.append(aux)
    a,b=recu(envi,inter)
    if a:
        return a,inter
    inter[let]=False
    envi=[]
    for j in claus:
        if not "-"+let in j:
            aux=[]
            for i in j:
                if i!=let:
                    aux.append(i)
            envi.append(aux)
    a,b=recu(envi,inter)
    if a:
        return a,inter
    return False,inter

def DPLL(claus):
    inter={}
    a,b=recu(claus,inter)
    if a:
        return inter
    else:
        inter={}
        return inter

m=[["i",0,-1,-1],[0,0,0,-1],[0,-1,0,0],[-1,-1,0,"f"]] #matriz que representa el laberinto
letras="abcdefghijklmnop"
comb = []
muros = []
for i in range(16):
    if m[i/4][i%4]==-1:
        comb.append(["-"+letras[i]])
        muros.append(letras[i])


comb.append(['a'])
comb.append(['p'])
walk = ['-b-e','-c-f','-f-i','-d-g','-g-j','-j-m','-k-n','-l-o']
close = ['-bcf','-lhk','-okn','-efi','-iej','-ijm','-iejm','-gchk','-ghkf','-gkfc','-gfch','-gchkf','-fbgj','-fgje','-fjeb','-febg','-fbgje','-kglo','-kloj','-kojg','-kjgl','-kgloj']
for i in walk:
    j = 0
    aux = []
    while j<len(i):
        if i[j] == '-':
            aux.append(i[j]+i[j+1])
            j+=2
        else:
            aux.append(i[j])
            j+=1
    comb.append(aux)
for i in close:
    j = 0
    aux = []
    while j<len(i):
        if i[j] == '-':
            aux.append(i[j]+i[j+1])
            j+=2
        else:
            aux.append(i[j])
            j+=1
    comb.append(aux)
inter =  DPLL(comb)
print inter
print 'Generando imagen...'
import visualizacion as v
v.dibujar_laberinto(inter,muros,1)
