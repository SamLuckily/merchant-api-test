# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


class AESCipher:
    """
    加解密工具
    """
    def __init__(self, secret_key):
        self.secret_key = secret_key.encode('utf-8')
        self.cipher = AES.new(self.secret_key, AES.MODE_ECB)

    @classmethod
    def aes_encrypt(cls, secret_key, plain_text):
        secret_key = secret_key.encode('utf-8')
        cipher = AES.new(secret_key, AES.MODE_ECB)
        # 填充明文
        padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
        # 加密
        encrypted = cipher.encrypt(padded_text)
        # 返回Hex编码的密文
        return binascii.hexlify(encrypted).decode('utf-8')

    @classmethod
    def aes_decrypt(cls, secret_key, cipher_text):
        secret_key = secret_key.encode('utf-8')
        cipher = AES.new(secret_key, AES.MODE_ECB)
        # 将Hex编码的密文转换为字节
        encrypted_bytes = binascii.unhexlify(cipher_text)
        # 解密
        decrypted = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
        # 返回解密后的明文
        return decrypted.decode('utf-8')
