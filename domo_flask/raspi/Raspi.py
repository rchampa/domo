import RPi.GPIO as GPIO
from IRaspi import IRaspi

class Raspi( IRaspi ):
    """Interface to avoid osx error compilation"""
    def turnOn( self ):
        print "Turning on..."

    def turnOff( self ):
        print "Turning off..."