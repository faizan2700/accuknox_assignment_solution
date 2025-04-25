class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

def main(): 
    x = Rectangle(4, 3) 
    for a in x: 
        print(a, end=', ') 

if __name__ == '__main__': 
    main() 