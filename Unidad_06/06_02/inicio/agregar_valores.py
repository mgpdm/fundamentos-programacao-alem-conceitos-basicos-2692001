archivoN = open('/workspaces/fundamentos-programacao-alem-conceitos-basicos-2692001/Unidad_06/06_02/inicio/valores.txt', 'rt')
archivoS = open('/workspaces/fundamentos-programacao-alem-conceitos-basicos-2692001/Unidad_06/06_02/inicio/valores_totales.txt', 'wt')
print('Procesando entrada')
suma = 0
for linea in archivoN:
    suma += int(linea)
    print(linea.rstrip(), file=archivoS)
print('\nTotal: ' + str(suma), file=archivoS)
archivoS.close()
print('Salida completa')
