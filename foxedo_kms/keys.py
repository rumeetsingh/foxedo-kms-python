import base64
import requests
import argon2
import nacl.secret


class Foxedo:

    def __init__(self,access_key):
        self.access_key = access_key

    def decrypt_string(self,response):
        access_key = base64.b64decode(bytes(self.access_key,'utf-8'))
        response = response.split(':')
        nonce = base64.b64decode(response[0])
        encrypted = base64.b64decode(response[1])
        return nacl.secret.SecretBox(access_key).decrypt(encrypted, nonce).decode('utf-8')
        
    def get_key(self,key_id):
        data = {"id":key_id,"access":argon2.PasswordHasher().hash(self.access_key)}
        key = requests.post('https://foxedokmsapi.herokuapp.com/api/keys/fetchkey/',json=data).json()
        return self.decrypt_string(key)
