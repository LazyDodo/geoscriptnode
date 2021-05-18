class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def add_item_callback(self,item,value):
        #print("Callback for %s : %s " % (item,value))
        pass 

    def __setitem__(self, key, value):
        if key=='val':
            raise TypeError()
        self.add_item_callback(key,value)
        dict.__setitem__(self, key, value)


    def __getattr__(self, item):
        """Maps values to attributes.
        Only called if there *isn't* an attribute with this name
        """
        #print("Getattr %s " % (item))
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, item, value):
        """Maps attributes to values.
        Only if we are initialised
        """
        #print("Setattr %s = %s" % (item,value))
        self.add_item_callback(item,value)
        if not '_attrExample__initialised' in self.__dict__:  # this test allows attributes to be set in the __init__ method
            return dict.__setattr__(self, item, value)
        elif item in self.__dict__:       # any normal attributes are handled normally
            dict.__setattr__(self, item, value)
        else:
            self.__setitem__(item, value)