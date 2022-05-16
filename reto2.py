def cliente(informacion:dict):
    if informacion['edad'] > 18:
        atraccionV = 'X-Treme'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            # aplicaría dsecuento
            pass
        else:
            # no aplicaría descuento
            pass
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccionV = 'Carros chocones'
        aptoV = True 
        if informacion['primer_ingreso'] == True:
            # aplicaría dsecuento
            pass
        else:
            # no aplicaría descuento
            pass
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccionV = 'Sillas voladoras'
        aptoV = True
        # verificar valor boleta
        
        
    else:
        atraccionV = 'N/A'
        totalBoletaV = 'N/A'
        aptoV = False
        
    dicSalida = {
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion': atraccionV,
        'apto': aptoV,
        'primer_ingreso':informacion['primer_ingreso']
        # valor boleta
        
    }
    return dicSalida
    

# En imaster no se colocan los prints, ni el diccionario de entrado, solo la función
informacion = {}
print(cliente(informacion))