# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:47:26 2020

@author: val <3
"""

def Menu():
    print( """¡Hola! Soy  Mai, bienvenido a mi programa ¿Que área deseas que calcule?

Menu
1) Cuadrado
2) Triangulo
3) Cuadrado
4) Division
5) Rombo    
6) Salir""")
    
import sys   
    
def Proceso():

    Menu()
  
    
    try:   
        op = int(input("Selecione Opcion: "))
        if op<=0 or op>6:
            print("Esa opción no existe")
            Proceso()
    except: 
        print("Opcion inexistente")
        Proceso()
    else:
        try:
            #CUADRADO
                if (op==1):      
                    lado=float(input("Ingrese el lado del cuadrado porfavor: "))
                    if lado>0 and lado<=1000000:           
                        res=lado*lado
                        print ("El área del cuadrado es de: ",res)                                        
                    else: 
                        print("La cantidad es demasiado grande o negativa")
                        Proceso()
             #CUADRADO 
                
            #TRIANGULO
                elif (op==2):      
                        base=float(input("Ingrese la base del triangulo porfavor: "))
                        if base>0 and base<=1000000: 
                            altura=float(input("Ingrese la altura del triangulo porfavor: "))
                            if altura>0 and altura<=1000000:                     
                                res=((base*altura)/2)
                                print ("El área del triangulo es de: ",res) 
                            else:
                                print("La cantidad es demasiado grande o negativa")
                                Proceso()
                                                   
                        else: 
                            print("La cantidad es demasiado grande o negativa")
                            Proceso()
            #TRIANGULO                
                            
            #RECTANGULO                
                elif (op==3):      
                        base=float(input("Ingrese la base del rectangulo porfavor: "))
                        if base>0 and base<=1000000: 
                            altura=float(input("Ingrese la altura del rectangulo porfavor: "))
                            if altura>0 and altura<=1000000:                     
                                res=(base*altura)
                                print ("El área del rectangulo es de: ",res) 
                            else:
                                print("La cantidad es demasiado grande o negativa")
                                Proceso()
                                                   
                        else: 
                            print("La cantidad es demasiado grande o negativa")
                            Proceso()
            #RECTANGULO                   
                            
            #CIRCULO                   
                if (op==4):      
                    radio=float(input("Ingrese el radio del circulo porfavor: "))
                    if radio>0 and radio<=1000000:           
                        res=(3.1416*(radio*radio))
                        print ("El área del circulo es de: ",res)                                        
                    else: 
                        print("La cantidad es demasiado grande o negativa")
                        Proceso()
            #CIRCULO     
           
            #ROMBO    
                elif (op==5):      
                    Dmayor=float(input("Ingrese la diagonal mayor del rombo porfavor: "))
                    if Dmayor>0 and Dmayor<=1000000: 
                        Dmenor=float(input("Ingrese la diagonal menor del rombo porfavor: "))
                        if Dmenor>0 and Dmenor<=1000000:                     
                            res=((Dmayor*Dmenor)/2)
                            print ("El área del rombo es de: ",res) 
                        else:
                            print("La cantidad es demasiado grande o negativa")
                            Proceso()
                                               
                    else: 
                        print("La cantidad es demasiado grande o negativa")
                        Proceso()        
            #ROMBO    
        
        except:
            print("Digito incorrecto, intenta de nuevo ;3")
            Proceso()
        
        #SALIR    
            if(op==6):
                print("¡Bye Bye! Regresa pronto ^^")
                sys.exit(1)     
        #SALIR
    
    try:   
        sn=str(input("¿Seguro que desea repetir el programa s/n?"))
        if sn=="s" or sn=="S":
            Proceso() 
        else:
            if sn=="n" or sn=="N":
                print("¡Bye Bye! Regresa pronto ^^")
                sys.exit(1)
    except: 
        print("¡Bye Bye! Regresa pronto ^^")
        sys.exit(1)
    

Proceso()
        