from utils.crypto import Crypto


class Genrator:
    crypto = Crypto()

    def genAddr(self, pub_key) -> str:
        if not isinstance(pub_key, (bytes, bytearray, str)):
            raise TypeError("pub 类型错误，需要str 或者bytes类型！")

        if isinstance(pub_key, str):
            pub_key = pub_key.encode("utf-8")

        # sha256 hash
        pub_sha256 = self.crypto.sha256(pub_key)

        # ripemd160
        ripemd160_value = self.crypto.ripemd160(pub_sha256)
        return ripemd160_value
