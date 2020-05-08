from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.backends import default_backend

def cryptography(**kwargs):

    ########################################
    texto = kwargs['texto']
    texto = bytes.fromhex(texto)

    ########################################
    key = kwargs['key']
    key  = bytes.fromhex(key)
    
    ########################################
    algorithm = algorithms.TripleDES(key) # ATRIBUI O ALGORITIMO
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend()) # CRIA CIFRA
    encryptor = cipher.encryptor() # APLICA CRIPTOGRAFIA
    ct = encryptor.update(texto)
    resultado = ct.hex()           # CONVERTE PARA HEX
    return resultado


if __name__ == "__main__":
    kwargs = {}
    kwargs['key'] = ''    # DEVE POSSUIR 16 CARACTERES
    kwargs['texto'] = ''

    print(cryptography(kwargs))