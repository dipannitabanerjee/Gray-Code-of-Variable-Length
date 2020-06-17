def decimalToBinaryNumber(x, n): 
    binaryNumber = [0]*x; 
    i = 0; 
    while (x > 0): 
        binaryNumber[i] = x % 2; 
        x = x // 2; 
        i += 1; 
   
    for j in range(0, n - i): 
        print('0', end ="");                # leftmost digits are filled with 0
  
    for j in range(i - 1, -1, -1): 
        print(binaryNumber[j], end =""); 
  
 
def generateGrayarr(n):                     # Function to generate gray code
    N = 1 << n; 
    for i in range(N): 
          
        x = i ^ (i >> 1);                   # generate gray code of corresponding binary number of integer i
  
        decimalToBinaryNumber(x, n);        # printing gray code 
                
        print();
        
 
if __name__ == '__main__':                  # Driver code
    n = int(input('Enter n: '))
    generateGrayarr(n);
