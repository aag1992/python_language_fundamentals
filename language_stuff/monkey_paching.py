
# basically this is used to replace the behaviour of a method in a class during runtime

class monkey:
    def patch(self):
          print ("patch() is being called")

def monk_p(self):
    print ("monk_p() is being called")

monkey.patch = monk_p

obj = monkey()

obj.patch()
# monk_p() is being called