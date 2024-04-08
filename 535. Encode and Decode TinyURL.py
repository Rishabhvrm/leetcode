class Codec:
    def __init__(self):
        '''
        the problem with using just a single map is 
        that it can store the same url multiple times if same
        encode request comes again
        map = {count: longUrl}
        Hence, it make sense to store the url as the key instead of the value
        '''
        self.encode_map = {}    # longUrl: count
        self.decode_map = {}    # count: longUrl
        self.count = 0


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_map:        # need this condition so that on multiple request for the same url, key won't get updated, count won't get exhausted
            self.count += 1
            shortUrl = self.count
            self.encode_map[longUrl] = shortUrl
            self.decode_map[shortUrl] = longUrl
        return self.encode_map[longUrl]
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))