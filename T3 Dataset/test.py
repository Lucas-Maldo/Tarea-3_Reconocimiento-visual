lista_act = ['Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Francisco De-la-maza', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Jaime Fernandez', 'Jaime Fernandez', 'Jaime Fernandez', 'Jaime Fernandez', 'Jaime Fernandez', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Maria Marin', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Diaz', 'Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Vicente Gana', 'Vicente Gana', 'Vicente Gana', 'Vicente Gana', 'Vicente Gana']
lista_pred = ['Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente','Gonzalo Vicente', 'Gonzalo Vicente', 'Gonzalo Vicente', 'Jaime Fernandez','Jaime Fernandez', 'Jaime Fernandez', 'Jaime Fernandez', 'Jaime Fernandez','Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza', 'Jorge Plaza','Jorge Plaza', 'Jorge Plaza', 'Jose Queirolo', 'Jose Queirolo','Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo', 'Jose Queirolo','Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt','Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt','Manuel Bentjerodt', 'Manuel Bentjerodt', 'Manuel Bentjerodt','Manuel Bentjerodt', 'Raimundo Martinez', 'Raimundo Martinez','Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez','Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez','Raimundo Martinez', 'Raimundo Martinez', 'Raimundo Martinez','Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada','Rodrigo Quezada', 'Rodrigo Quezada', 'Rodrigo Quezada', 'Raimundo Martinez','Raimundo Martinez', 'Rodrigo Quezada', 'Jose Queirolo', 'Jose Queirolo','Jose Queirolo', 'Gonzalo Vicente', 'Raimundo Martinez', 'Jose Queirolo','Raimundo Martinez', 'Jose Queirolo', 'Jose Queirolo', 'Raimundo Martinez','Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Sebastian Ma-shichoy','Sebastian Ma-shichoy', 'Sebastian Ma-shichoy', 'Vicente Gana','Vicente Gana', 'Vicente Gana', 'Vicente Gana', 'Vicente Gana']
# print(set(lista_act))
# print()
# print(set(lista_pred))
# print()
# print(len(set(lista_act).union(lista_pred)))
lista_nueva = []
for i in lista_act:
    if(i not in lista_nueva):
        lista_nueva.append(i)
print(lista_nueva)