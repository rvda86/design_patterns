from abc import ABC, abstractmethod

class Compressor(ABC):    
    @abstractmethod
    def compress(self):
        pass

class PNGCompressor(Compressor):
    def compress(self, image):
        image = "a small PNG image"
        return image
        
class JPGLibrary:
    def minify_jpg(self, file):
        file = "a small JPG image"
        return file

class JPGCompressorAdapter(Compressor):
    def __init__(self):
        self.adaptee = JPGLibrary()

    def compress(self, image):
        return self.adaptee.minify_jpg(image)

class Client:
    def __init__(self, compressor):
        self.compressor = compressor

    def compress_image(self, image):
        return self.compressor.compress(image)

client_a = Client(PNGCompressor())
image = "A big PNG image"
compressed_image = client_a.compress_image(image)
print(compressed_image)

client_b = Client(JPGCompressorAdapter())
image = "A big JPG image"
compressed_image = client_b.compress_image(image)
print(compressed_image)