#value is 10 base
# Note that type of return value is string 
def baseTransform(value: int, base: int)->str:
    next = int(value/base)
    if(next):
        return baseTransform(next, base) + str(value%base)
    return str(value%base)
