import tableaux as t
def lsToY(ls):
    if '-' in ls[0]:
        form = t.Tree('-',None,t.Tree(ls[0].replace('-',''),None,None))
    else:
        form = t.Tree(ls[0],None,None)
    for i in range(1,len(ls)):
        if '-' in ls[0]:
            form = t.Tree('Y',form,t.Tree('-',None,t.Tree(ls[i].replace('-',''),None,None)))
        else:
            form = t.Tree('Y',form,t.Tree(ls[i],None,None))
    return form

def lstoO(ls):
    form = ls[0]
    for i in range(1,len(ls)):
        form = t.Tree('O',form,ls[i])
    return form

def listatoNPI(lista , str):
    if(len(lista) == 1):
        return lista[0] + str
    else:
        x = len(lista)/2
        str = lista[x] + str
        return listatoNPI(lista[x+1:len(lista)], str.rstrip('Y')) + listatoNPI(lista[0:x], str)

def genaux(letras):
    aux = []
    for i in range (len(letras)*2 - 1):
        if i % 2 == 0:
            if '-' in letras[i/2]:
                tmp = letras[i/2][1] + letras[i/2][0]
                aux.append(tmp)
            else:
                aux.append(letras[i/2])
        else:
            aux.append('Y')
    return aux
Regla3 = {'b':'b-f-c-bYY>','l':'l-k-h-lYY>','o':'o-n-k-oYY>','m':'m-n-i-mYY>','d':'d-h-c-dYY>', 'e':'e-i-f-eYY>','i':'i-m-j-Ye-iYYm-j-iYYj-e-iYYOO>','h':'h-l-g-hYY>','c':'c-d-g-Yb-cYYg-b-cYYd-b-cYYOO>','n':'n-j-o-Ym-nYYo-m-nYYj-m-nYYOO>','g':'g-f-k-Yh-c-YYh-c-f-YYOc-f-k-YYf-k-h-YYk-h-c-YYOOOgY>','f':'f-e-j-Yg-b-YYg-b-e-YYOb-e-j-YYe-j-g-YYj-g-b-YYOOOfY>','j':'j-i-n-Yk-f-YYk-f-i-YYOf-i-n-YYi-n-k-YYn-h-f-YYOOOjY>','k':'k-j-o-Yl-g-YYl-g-j-YYOg-j-o-YYj-o-l-YYo-l-g-YYOOOkY>'} 
Regla4 = {'b':'fc-Yf-cYObY','e':'if-Yi-fYOeY','l':'kh-Yk-hYOlY','o':'nk-Yn-kYOoY','m':'inYmY','d':'hcYdY','g':'k-h-YfcYYk-hYf-cYYkh-Yf-cYYOOk-hYfc-YYkh-Yfc-YYkhYf-c-YYOOgY','k':'o-l-YjgYYo-lYj-gYYol-Yj-gYYOOo-lYjg-YYol-Yjg-YYolYj-g-YYOOkY','j':'n-k-YifYYn-kYi-fYYnk-Yi-fYYOOn-kYif-YYnk-Yif-YYnkYi-f-YYOOjY','n':'o-jmYYoj-mYYojm-YYOOnY','h':'g-ldYYgl-dYYgld-YYOOhY','c':'d-gbYYdg-bYYdgb-YYOOcY','i':'m-jeYYmj-eYYmje-YYOOiY','f':'j-g-YebYYj-gYe-bYYOjg-Ye-bYYOj-gYeb-YYjg-Yeb-YYOjgYe-b-YYOOfY'}

#
