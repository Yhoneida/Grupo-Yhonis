def palabraEsdru(nombre_archivo):
    
    vocales_tildadas = "áéíóúÁÉÍÓÚ"
    
    
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        palabras = f.read().split()  
    
    
    with open("C:/Users/linit/Downloads/palabras/esdrujulas.txt", 'w', encoding='utf-8') as esdrujulas:
    
        for palabra in palabras:
            
            if len(palabra) >= 3:
                
                antepenultima_letra = palabra[-3]
                
                
                if antepenultima_letra in "aeiouAEIOU":
                    
                    if any(vocal in palabra for vocal in vocales_tildadas):
                        esdrujulas.write(palabra + "\n")  

