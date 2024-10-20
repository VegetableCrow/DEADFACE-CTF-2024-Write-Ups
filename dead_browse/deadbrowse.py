def xor_decrypt(obfuscated_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_len = len(key_bytes)
    
    for i in range(len(obfuscated_bytes)):
        decrypted_byte = obfuscated_bytes[i] ^ key_bytes[i % key_len]
        decrypted_bytes.append(decrypted_byte)
        
    return decrypted_bytes.decode('utf-8', errors='ignore')

# The obfuscated string in bytes (as specified)
obfuscated_string = b'\x0b\x15>\x14\x1e\x16!V&,F\x0eJ\x14T\r@\x13P \x16G;F\t\x16\x01\x04'
print(obfuscated_string)
# The key in bytes
key = b'my_secret_key'

# Decrypt the string
decrypted_string = xor_decrypt(obfuscated_string, key)
print(decrypted_string)
