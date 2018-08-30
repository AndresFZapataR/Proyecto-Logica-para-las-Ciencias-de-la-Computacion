class Tree(object):
  def __init__(self,label,left,right):
    self.left = left
    self.right = right
    self.label = label

conectivos_binarios = ['O','Y','>']
letras = ["p","q","r", "t", "s"]
interps = []
aux = {}
#(-(p>q)>(rOs))Yt
p=Tree('p',None,None)
q=Tree('q',None,None)
r=Tree('r',None,None)
t=Tree('t', None, None)
s = Tree('s',None,None)
pq = Tree('>',p,q)
nopq = Tree('-', None, pq)
ros = Tree('O',r,s)
nopqros = Tree('>',nopq,ros)
formula = Tree('Y', nopqros,t)

for a in letras:
	aux[a]=1
interps.append(aux)
for a in letras:
       	interps_aux=[i for i in interps]
       	for i in interps_aux:
         	aux1={}
          	for b in letras:
              		if a==b:
                  		aux1[b]=1-i[b]
              		else:
                  		aux1[b]=i[b]
      		interps.append(aux1)

print "interpretaciones"
for i in interps:
    	print i
    
    
def val(a,inter):
   	if a.right==None:
       		return inter[a.label]
   	if a.label=='-':
       		if val(a.right,inter)==1:
           		return 0
       		return 1
   	if a.label=='Y':
       		if val(a.right,inter)==1 and val(a.left,inter)==1:
           		return 1
       		else:
           		return 0
   	if a.label=='O':
       		if val(a.right,inter)==1:
           		return 1
       		if val(a.left,inter)==1:
           		return 1
       		return 0
   	if a.label=='>':
       		if val(a.left,inter)==0:
           		return 1
       		return val(a.right,inter)


def equi(a,b,interps):
   	for i in interps:
      		if val(a,i)!=val(b,i):
          		return False
	return True

intertodotrue = []

for i in interps:
	if val(formula, i):
		intertodotrue.append(i)
print "interpretaciones que hacen verdadera la formula: "
for i in intertodotrue:
	print i

