#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

LED_RED = 3 #Définit le numéro du port GPIO qui alimente la led rouge
LED_GREEN = 5 #Définit le numéro du port GPIO qui alimente la led verte
RFID_UID = [179, 165, 146, 96, 228] #Définit l'UID du badge RFID

#Définit la fonction permettant d'allumer une led
def turn_led_on (led) :
    GPIO.setup(led, GPIO.OUT) #Active le contrôle du GPIO
    GPIO.output(led, GPIO.HIGH) #Allume la led

#Définit la fonction permettant d'éteindre une led
def turn_led_off (led) :
    GPIO.setup(led, GPIO.OUT) #Active le contrôle du GPIO
    GPIO.output(led, GPIO.LOW) #Eteind la led

#Définit la fonction permettant d'allumer la rouge et éteindre la verte
def turn_red_on () :
    turn_led_off(LED_GREEN) #Eteind la led verte
    turn_led_on(LED_RED) #Allume la led rouge
    time.sleep(1)
    turn_both_off()

#Définit la fonction permettant d'allumer la verte et éteindre la rouge
def turn_green_on () :
    turn_led_off(LED_RED) #Eteind la led rouge
    turn_led_on(LED_GREEN) #Allume la led verte
    time.sleep(2)
    turn_both_off()

# Eteint les deux leds au démarrage du programme
def turn_both_off():
    turn_led_off(LED_RED)
    turn_led_off(LED_GREEN)
