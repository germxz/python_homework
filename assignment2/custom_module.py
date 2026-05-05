secret = "shazam!"

def set_secret(new_secret):
   global secret
   secret = new_secret
   
def set_that_secret(value):
    set_secret(value)
    