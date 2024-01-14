from token_manager import api_locker
import base64

class Cryption:
    def __init__(self):
        self.crypted_value = ""

    def recall_values(self):
        for key, value in api_locker.items():
            self.crypted_value += value + '\n'

        return self.crypted_value

    def encode_values(self):
        if self.crypted_value:
            bytes_value = self.crypted_value.encode("ascii")
            base64_bytes = base64.b64encode(bytes_value)
            print(base64_bytes)


cryption = Cryption()
cryption.recall_values()
cryption.encode_values()


