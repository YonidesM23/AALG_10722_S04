furniture = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
a = furniture [0:len(furniture)//2]
print (a)
print ('escritorio' in furniture)

furniture = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
mesa, silla, armario, estante, banco, escritorio = furniture
mesa, silla, armario, estante, banco, escritorio = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']

e = 10
f = 20

tmp = e
e = f
f = tmp
print(e, ' ', f)

e, f = f, e
print(e, ' ', f)    

#furniture = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
#furniture.append('librero')
#print (furniture)

#furniture = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
#furniture.insert(1, 'librero')
#print (furniture)

#furniture = ['mesa', 'silla', 'armario', 'estante']
#del furniture[2]
#print (furniture)
#del furniture[2]
#print (furniture)

#furniture = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
#furniture.remove('estante')
#print (furniture)