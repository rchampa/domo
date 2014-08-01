class IRaspi( object ):
    """Interface to avoid osx error compilation"""
    def turnOn( self ):
        raise NotImplementedError( "Should have implemented this" )

    def turnOff( self ):
        raise NotImplementedError( "Should have implemented this" )

