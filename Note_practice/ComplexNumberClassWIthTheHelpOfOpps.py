
""" 
Create a python named `ComplexNumber` to represent a complex number

Theory:
A complex number is a number that represents a real part and an imaginary part . 
It is typically written in the form a+bi, where 'a' is that real part ,and 'b' is the imaginary part, and 'i' is the imaginary unit (✓-1). 


Operations:

1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Divide(/)
5. Comparison(== , !=)

"""


class ComplexNumber:
    def __init__(self,real=0,image=0):
        self.real = real
        self.image = image
    
    def __str__(self):  #magic method
        if (self.real == 0):
            return f"{self.image}i"
        elif(self.image<0):
            s = f"({self.real}{self.image}i)"
        else:
            s = f"({self.real} + {self.image}i)"  
        return s
    
    def __add__(self,other):
        resultReal = 0
        resultImage = 0
        resultReal = self.real + other.real
        resultImage = self.image + other.image
        ans = ComplexNumber(resultReal, resultImage)
        return ans
    
    def __sub__(self,other):
        resultReal = 0
        resultImage = 0
        resultReal = self.real - other.real
        resultImage = self.image - other.image
        ans = ComplexNumber(resultReal, resultImage)
        return ans
    
    def __mul__(self,other):
        resultReal = 0
        resultImage = 0
        resultReal = self.real * other.real - self.image * other.image
        resultImage = self.real * other.image + other.real * self.image
        ans = ComplexNumber(resultReal, resultImage)
        return ans
    
    def __truediv__(self,other):
        resultReal = 0
        resultImage = 0
        den = other.real**2 + other.image**2
        ans = self* ComplexNumber(other.real/den,(-1*other.image)/den)      
        return ans
        
    def __eq__(self,other):
        return (self.real == other.real) and (self.image == other.image) 
        
    def conjugate(self):
        return ComplexNumber(self.real ,-1*self.image)
        




      
cn1 = ComplexNumber(3,4)  
cn2 = ComplexNumber(4,5)
cn3 = ComplexNumber(3,5)
cn4 = ComplexNumber(9,7)
print(cn1.conjugate())