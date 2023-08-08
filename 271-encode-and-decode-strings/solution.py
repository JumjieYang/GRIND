class Codec:
    def encode(self, strs):
        return chr(257).join(strs)

    def decode(self, s):
        return s.split(chr(257))
