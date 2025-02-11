#function created to avoid problems with the string/int data type for numbers

def is_valid_integer(value):
    if isinstance(value, int):
        return True,int(value)

    try:
        value = eval(value)
        return True,value
    except:
        pass

    try:
        int(value)
        return True,int(value)
    except ValueError:
        return False
