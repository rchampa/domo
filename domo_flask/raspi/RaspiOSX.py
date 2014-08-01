from IRaspi import IRaspi

"""Interface to avoid osx error compilation"""
class RaspiOSX( IRaspi ):

    def turnOn( self ):
        print "Turning on..."

    def turnOff( self ):
        print "Turning off..."