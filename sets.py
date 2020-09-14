s = set([1,2,3])
t = set([3,4,5])

# Unión de sets (no pueden tener valores repetidos)
print('_____ s | t _____')
print(s.union(t))
print(s|t)

# Intersección (valores comunes)
print('_____ s & t _____')
print(s.intersection(t))
print(s&t)

# Diferencia entre sets (valores que no tiene s respecto a t o viceversa)
print('_____ s - t _____')
print(s.difference(t))
print(s-t)
print('_____ t - s _____')
print(t.difference(s))
print(t-s)

# Diferencia Simétrica - Full outer join (valores que no coinciden en s y t)
print('_____ s ^ t _____')
print(s.symmetric_difference(t))
print(t^s)


