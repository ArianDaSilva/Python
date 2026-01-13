lugares_visitables = ['japón','alaska','paraguay','españa','china']
print(lugares_visitables) # Lista original.
print(sorted(lugares_visitables)) # Lista en orden alfabético.
print(lugares_visitables) # Lista original sin cambios.
print(sorted(lugares_visitables, reverse = True)) # Lista en orden alfabético inverso.
print(lugares_visitables) # Lista original sin cambios.
lugares_visitables.reverse()
print(lugares_visitables) # Lista invertida.
lugares_visitables.reverse()
print(lugares_visitables) # La lista vuelve a su orden original.
lugares_visitables.sort()
print(lugares_visitables) # Lista en orden alfabético.
lugares_visitables.sort(reverse = True)
print(lugares_visitables) # Lista en orden alfabético inverso.