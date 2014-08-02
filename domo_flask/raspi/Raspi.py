import RPi.GPIO as GPIO
from IRaspi import IRaspi

class Raspi( IRaspi ):
    """Interface to avoid osx error compilation"""

    def __init__(self, pin_gpio=17):
    	GPIO.setmode(GPIO.BCM)
    	GPIO.setup(pin_gpio, GPIO.OUT)

    def turnOn( self ):
    	try:
        	print "Turning on..."
        	GPIO.output(17, True)
        except KeyboardInterrupt:
        	super(Raspi, self).cleanGPIO();
        except:
        	super(Raspi, self).cleanGPIO();

    def turnOff( self ):
        try:
        	print "Turning off..."
        	GPIO.output(17, False)
        except KeyboardInterrupt:
        	super(Raspi, self).cleanGPIO();
        except:
        	super(Raspi, self).cleanGPIO();