"""
    1 2 3 4 5 6
    ===========
  1|a b c d e f
  2|g h i j k l
  3|m n o p q r
  4|s t u v w x
  5|y z 1 2 3 4
  6|5 6 7 8 9 0
"""
import math


class Polybius:
    def __init__(self, alphabet: str) -> None:
        self.encode_decode_map = self.build_grid(alphabet=alphabet)

    def build_grid(self, alphabet: str) -> dict:
        encode_decode_map = {}
        n = int(math.sqrt(len(alphabet)))  # len(alphabet) must be a perfect square number
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                encoded: str = str(j) + str(i)
                character = alphabet[(j - 1) * n + (i - 1)]
                encode_decode_map[character] = encoded
                encode_decode_map[encoded] = character
        return encode_decode_map

    def encode(self, message: str) -> list[int]:
        encoded = []
        for c in message:
            encoded.append(int(self.encode_decode_map[c]))
        return encoded

    def decode(self, message: list[int]):
        decoded = ""
        for c in message:
            decoded += self.encode_decode_map[str(c)]
        return decoded


pb = Polybius("abcdefghijklmnopqrstuvwxyz1234567890")
assert pb.encode("hello") == [22, 15, 26, 26, 33]
assert pb.decode([22, 15, 26, 26, 33]) == "hello"
assert pb.decode(pb.encode("hello")) == "hello"
