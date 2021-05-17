from array import array

class Grid:
    
    def __init__(self, rows, columns, fill_value=None):
        self.data = array(rows)
        for row in range(rows):
            self.data[row] = array(columns, fill_value)
            
    def get_heigth(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getItem__(self, index):
        return self.data[index]
    
    def __str__(self):
        return super().__str__()
    
        for row in range(self.get_heigth()):
            for col in range(self.get_width()):
                result +=str(self.data[row][col]) + ' '
                
            result += '\n'
        return str(result)
    
matriz = Grid(3,3)
print(matriz)