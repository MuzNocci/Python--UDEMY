def create_function(func):

    def inside(*args,**kwargs):

        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)

        return result
    
    return inside



def inverts_string(string):

    return string[::-1]



def is_string(param):

    if not isinstance(param, str):
        raise TypeError('O parâmetro deve ser uma string.')




inverts_string_check_param = create_function(inverts_string)
print(inverts_string_check_param(123))