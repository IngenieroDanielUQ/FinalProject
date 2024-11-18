#Codigo creado originalmente por el canal Computadoras y Sensores.
#Codigo modificado y adaptado por Hector Daniel Gonzalez Sanchez.
    #Estudiante de Ingenieria de Sistemas y computacion de la Universidad del Quindio (Armenia - Colombia)


#Se importan las librerias time (Para que el codigo acceda al tiempo real de la memoria)
#Digitalio


import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP15
boton2_pin= board.GP16
boton3_pin= board.GP17
boton4_pin= board.GP18
boton5_pin= board.GP19

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

boton2 = digitalio.DigitalInOut(boton2_pin)
boton2.direction = digitalio.Direction.INPUT
boton2.pull = digitalio.Pull.DOWN

boton3 = digitalio.DigitalInOut(boton3_pin)
boton3.direction = digitalio.Direction.INPUT
boton3.pull = digitalio.Pull.DOWN

boton4 = digitalio.DigitalInOut(boton4_pin)
boton4.direction = digitalio.Direction.INPUT
boton4.pull = digitalio.Pull.DOWN

boton5 = digitalio.DigitalInOut(boton5_pin)
boton5.direction = digitalio.Direction.INPUT
boton5.pull = digitalio.Pull.DOWN

while True:
    if boton1.value:
        print("Botón 1 - Guardar")
        teclado.press(Keycode.CONTROL, Keycode.S)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.S)
    if boton2.value:
        print("Botón 2 - Copiar")
        teclado.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.C)
    if boton3.value:
        print("Botón 3 - Pegar")
        teclado.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.V)
    if boton4.value:
        print("Botón 4 - Seleccionar todo")
        teclado.press(Keycode.CONTROL, Keycode.A)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.A)
    if boton5.value:
        print("Botón 5 - Deshacer")
        teclado.press(Keycode.CONTROL, Keycode.Z)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.Z)
    time.sleep(0.1)
    