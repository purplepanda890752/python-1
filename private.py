class myClass:

    _privateVar = 27;
    
    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private Variable value: ", myClass._privateVar)

foo = myClass()
foo.hello()
foo.__privMeth