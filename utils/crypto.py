import hashlib
# from base58 import b58decode, b58encode

class Crypto:

    def sha256(self, pattern) -> str:
        if not isinstance(pattern, (bytes, bytearray, str)):
            raise TypeError("pattern should be bytes, bytearray or string")
        if isinstance(pattern, str):
            pattern = pattern.encode("utf-8")
        return hashlib.sha256(pattern).hexdigest()

    def ripemd160(self, pattern) -> str:
        if not isinstance(pattern, (bytes, bytearray, str)):
            raise TypeError("pattern should be bytes, bytearray or string")
        if isinstance(pattern, str):
            pattern = pattern.encode("utf-8")
        return hashlib.new("ripemd160", pattern).hexdigest()


