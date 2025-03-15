# create class
class IOString():
#Constructor set to default value
  def _init_(self):
    self.str1=""

    #function to get input from user
    def get_string(self):
        self.str1= input("Enter string:")
        #function to print the uppercase
        def print_String(self):
            print("Result is:",self.str1.upper())
                   # object creation
str1=IOString()
                   #call function
str1.get_string()
str1.print_string