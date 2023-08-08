class Codec:
    def __init__(self):
        self.count = 0
        self.encode_map = {}
        self.decode_map = {}

    def encode(self, longUrl):
        if longUrl not in self.encode_map:
            self.encode_map[longUrl] = str(self.count)
            self.decode_map[str(self.count)] = longUrl
            self.count += 1

        return self.encode_map[longUrl]

    def decode(self, shortUrl):
        if shortUrl in self.decode_map:
            return self.decode_map[shortUrl]

        return ''
