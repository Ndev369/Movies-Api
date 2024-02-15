from jose.jwt import encode,decode


def create_token(data:dict):
    token:str = encode(data , key="123456", algorithm='HS256')   
    return token 

def validate_token(token:str)->dict:
    data:dict = decode(token,key="123456", algorithms=['HS256'])
    return data