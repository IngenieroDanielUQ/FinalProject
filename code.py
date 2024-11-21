#Codigo creado originalmente por el canal Computadoras y Sensores // y NerdCave
#Codigo modificado y adaptado por Hector Daniel Gonzalez Sanchez.
#Estudiante de Ingenieria de Sistemas y computacion de la Universidad del Quindio (Armenia - Colombia)

# Importamos las librerías necesarias
import time  # Para gestionar pausas en el programa
import digitalio  # Para manejar entradas y salidas digitales
import analogio  # Para manejar entradas analógicas
import board  # Para definir los pines de la Raspberry Pi Pico
import usb_hid  # Para habilitar las funciones del dispositivo HID (teclado y mouse)
from adafruit_hid.keyboard import Keyboard  # Para simular un teclado
from adafruit_hid.keycode import Keycode  # Para usar combinaciones de teclas
from adafruit_hid.mouse import Mouse  # Para simular un mouse

# Inicializamos el mouse y el teclado como dispositivos HID
mouse = Mouse(usb_hid.devices)
teclado = Keyboard(usb_hid.devices)

# Definimos los pines donde están conectados los botones
boton1_pin = board.GP15
boton2_pin = board.GP16
boton3_pin = board.GP17
boton4_pin = board.GP18
boton5_pin = board.GP19

# Definimos los pines para las entradas analógicas (joystick)
x_axis = analogio.AnalogIn(board.GP27)  # Eje X
y_axis = analogio.AnalogIn(board.GP26)  # Eje Y

# Definimos el pin del botón de selección del joystick
select = digitalio.DigitalInOut(board.GP14)
select.direction = digitalio.Direction.INPUT  # Es una entrada
select.pull = digitalio.Pull.UP  # Activamos la resistencia de pull-up

# Configuramos los botones como entradas digitales con pull-down
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

# Definimos los valores mínimos y máximos del joystick (en voltios)
pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0  # Dividimos el rango en 20 pasos

# Función para convertir el valor del pin analógico en voltaje
def get_voltage(pin):
    return (pin.value * 3.3) / 65536  # Escalamos el valor a 3.3V

# Función para mapear el voltaje a un rango de 0-20 pasos
def steps(axis):
    return round((axis - pot_min) / step)

# Bucle principal
while True:
    # Comprobamos si se presionan los botones y realizamos las acciones correspondientes
    if boton1.value:
        print("Botón 1 - Guardar")
        teclado.press(Keycode.CONTROL, Keycode.S)  # CTRL + S
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.S)
    if boton2.value:
        print("Botón 2 - Copiar")
        teclado.press(Keycode.CONTROL, Keycode.C)  # CTRL + C
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.C)
    if boton3.value:
        print("Botón 3 - Pegar")
        teclado.press(Keycode.CONTROL, Keycode.V)  # CTRL + V
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.V)
    if boton4.value:
        print("Botón 4 - Seleccionar todo")
        teclado.press(Keycode.CONTROL, Keycode.A)  # CTRL + A
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.A)
    if boton5.value:
        print("Botón 5 - Deshacer")
        teclado.press(Keycode.CONTROL, Keycode.Z)  # CTRL + Z
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.Z)
    
    time.sleep(0.1)  # Pequeña pausa para evitar sobrecarga

    # Leemos los pasos del joystick (invertimos los ejes)
    x_steps = steps(get_voltage(y_axis))  # Eje X controlado por el eje Y del joystick
    y_steps = steps(get_voltage(x_axis))  # Eje Y controlado por el eje X del joystick

    # Si el botón del joystick se presiona, realizamos un clic izquierdo
    if not select.value:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.1)  # Retardo para evitar múltiples clics

    # Control del movimiento del mouse en el eje X (horizontal)
    if x_steps > 19.0:
        mouse.move(x=-16)  # Mover rápido a la izquierda
    elif x_steps > 11.0:
        mouse.move(x=-4)   # Mover lento a la izquierda
    elif x_steps < 9.0:
        mouse.move(x=16)   # Mover rápido a la derecha
    elif x_steps < 8.0:
        mouse.move(x=4)    # Mover lento a la derecha

    # Control del movimiento del mouse en el eje Y (vertical)
    if y_steps > 19.0:
        mouse.move(y=16)   # Mover rápido hacia abajo
    elif y_steps > 11.0:
        mouse.move(y=4)    # Mover lento hacia abajo
    elif y_steps < 9.0:
        mouse.move(y=-16)  # Mover rápido hacia arriba
    elif y_steps < 1.0:
        mouse.move(y=-4)   # Mover lento hacia arriba