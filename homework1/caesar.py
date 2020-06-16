def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    
    for char in plaintext:
        if "a" <= char <= "z":
            code = ord(char) + 3
            if (code > ord("z")):
                code = code - 26
        elif "A" <= char <= "Z":
            code = ord(char) + 3
            if (code > ord("Z")):
                code = code - 26
        else:
            code = ord(char)
        ciphertext += chr(code)
   
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    for char in ciphertext:
        if "a" <= char <= "z":
            code = ord(char) - 3
            if (code < ord("a")):
                code = code + 26
        elif "A" <= char <= "Z":
            code = ord(char) - 3
            if (code < ord("A")):
                code = code + 26
        else:
            code = ord(char)
        plaintext += chr(code)
    
    return plaintext
