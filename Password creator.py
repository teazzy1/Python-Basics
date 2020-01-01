mypass = str(input("type your passsword in the box "))
def data(password):

    if len(password) >= 8:
        return True

    else:
        return False
print(data(mypass))


    