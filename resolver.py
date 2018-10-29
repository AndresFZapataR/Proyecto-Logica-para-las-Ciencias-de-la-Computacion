import tableaux as t
import funciones_res as fun
import visualizacion as v

# Genero las baldosas
# a b c d
# e f g h
# i j k l
# m n o p
atomos = 'abcdefghijklmnop'
baldosas = []
for i in atomos:
    baldosas.append(i)
# Regla #1: El laberinto debe tener un inicio y un final
inicio = t.Tree('a',None,None)
final = t.Tree('p',None,None)

# Genero los muros, estos deben ser diferentes a las baldosas de inicio y final
m = 'bdhjmno'
muros = []
for i in m:
	if i != inicio.label and i != final.label:
    		muros.append(t.Tree('-',None,t.Tree(i,None,None)))
# Genero todos las combinaciones de las baldosas
print "generando caminos..."
bina=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
caminos = t.Tree('-',None,t.Tree(baldosas[0],None,None))
for i in range(1,len(bina)):
	caminos = t.Tree('Y',caminos,t.Tree('-',None,t.Tree(baldosas[i],None,None)))

while bina[15]!=  2:
	if bina[0] == 0:
            f = t.Tree('-',None,t.Tree(baldosas[0],None,None))
        else:
            f = t.Tree(baldosas[0],None,None)

        for i in range(1,len(bina)):
            if bina[i] == 0:
                f = t.Tree('Y',f,t.Tree('-',None,t.Tree(baldosas[i],None,None)))
            else:
                f = t.Tree('Y',f,t.Tree(baldosas[i],None,None))
        caminos = t.Tree('O',f,caminos)
        bina[0] += 1
        for i in range(15):
            if bina[i] == 2:
                bina[i+1] += 1
                bina[i] = 0

# Regla #2: Los muros no pertenecen a ningun camino posible
formula = [caminos]
formula.append(inicio)
formula.append(final)
for i in range(len(muros)):
	formula.append(muros[i])

satis, sol_parcial = t.Tableaux([formula],baldosas)

for i in sol_parcial:
	print i     #imprimo las interpretaciones

# Convierto las interpretaciones que arrojo el tableaux denuevo a formulas para aplicar nuevas reglas
formula = []
temporal = []
for i in sol_parcial:
    temporal.append(t.StringtoTree(fun.listatoNPI(fun.genaux(i),''),baldosas))

form = temporal[0]
for i in range(1,len(temporal)):
    form = t.Tree('O',form,temporal[i])
formula.append(form)
formula.append(t.StringtoTree('eb-Ye-bYO',baldosas)) #desde el inicio solo se puede ir a un unico sitio
formula.append(t.StringtoTree('lo-Yl-oYO', baldosas)) #solo se puede llegar al final por l o por o
print t.imprime_hoja(formula)
satis, sol_parcial = t.Tableaux([formula],baldosas)
for i in sol_parcial:
	print i
# Regla #3: identificar caminos cerrados
noMuros = [x for x in baldosas if (x not in m) and (x != 'a') and (x != 'p')] # Escojo las baldosasa que no son muros y son diferentes a el inicio y el final
formula = []
temporal = []
for i in sol_parcial:
    temporal.append(t.StringtoTree(fun.listatoNPI(fun.genaux(i),''),baldosas))
form = temporal[0]
for i in range(1,len(temporal)):
    form = t.Tree('O',form,temporal[i])
formula.append(form)

for i in noMuros :
    if len(sol_parcial) == 1:
        break
    formula.append(t.StringtoTree(fun.Regla3[i],baldosas))
    print t.imprime_hoja(formula)

    satis, sol_parcial = t.Tableaux([formula],baldosas)
    formula = []
    temporal = []
    for i in sol_parcial:
        temporal.append(t.StringtoTree(fun.listatoNPI(fun.genaux(i),''),baldosas))
    form = temporal[0]
    for i in range(1,len(temporal)):
        form = t.Tree('O',form,temporal[i])
    formula.append(form)
# Regla #4: No se puede mover en diagonal y no se puede retroceder
formula = []
temporal = []
for i in sol_parcial:
    temporal.append(t.StringtoTree(fun.listatoNPI(fun.genaux(i),''),baldosas))
form = temporal[0]
for i in range(1,len(temporal)):
    form = t.Tree('O',form,temporal[i])
formula.append(form)
for i in noMuros :
    if len(sol_parcial) == 1:
        break
    formula.append(t.StringtoTree(fun.Regla4[i],baldosas))
    print t.imprime_hoja(formula)
    satis, sol_parcial = t.Tableaux([formula],baldosas)
    formula = []
    temporal = []
    for i in sol_parcial:
        temporal.append(t.StringtoTree(fun.listatoNPI(fun.genaux(i),''),baldosas))
    form = temporal[0]
    for i in range(1,len(temporal)):
        form = t.Tree('O',form,temporal[i])
    formula.append(form)

count = 1;
for i in sol_parcial:
    v.dibujar_tablero(sol_parcial,muros,count)
    count += 1
