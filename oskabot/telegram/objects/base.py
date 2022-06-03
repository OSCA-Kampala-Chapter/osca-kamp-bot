#base class for all the telegram objects

class TgmObjectBase:
    
    def encode (self):
        """ should be implemented by the subclass to json
        encode the object.
        """
        raise NotImplementedError
