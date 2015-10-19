#Jessica Tan
#The number of words in the words.txt file was 109583. So to find the filter size, I multiplied it by the ln(.005) and divided it by the ln(2)^2. Which ended up being 1208454. So filterSize = 1208454. We then take the filtersize and divide it by the number of words added, so 1208454/109583, which is 11.02. We then multiply that by ln(2) which is 7.64. so rounding up, we will use 8 hash functions. hashNum=8.
#filterSize = 109583 *ln(.005)/(ln(2)^2) = 1208454
#hashNum = 1208454/109583 * ln(2) = 7.64= 8
import math
class BitSet:
    def __init__(self, value=0):
        self.value = value    
 
    def __contains__(self, bit ):
        return self.value & 2**bit > 0
    
    def add(self,bit):
        self.value = self.value | 2 ** bit
           
class Bloom:
    def __init__(self,length,hashNum):
        self.bit = set() #or BitSet()
        self.length = length
        self.hashNum = hashNum
    def add(self,val):
        for num in range(0, self.hashNum, 1):
            hashed = val + str(num)  
            self.bit.add(hash(hashed) % self.length)
    

        
    def __contains__(self,val):
        check = True
        inTheFilter= True
        lst=[]
        for num in range(0, self.hashNum, 1):
            lst.append(val + str(num))

        while check:
            for hashed in lst:            
                if not (hash(hashed) % self.length ) in self.bit:
                    check = False
                    inTheFilter = False
            check = False
       
        return inTheFilter
    
def main():
    filterSize = 1208454
    hashNum = 8
    filterB = Bloom(filterSize,hashNum)
    f = open('words.txt',"r")
    dictionary = f.readlines()    
    f.close()
    count=0
    for x in dictionary:
        count += 1
        x = x.rstrip('\n')
        filterB.add(x)

    f = open('declarationofindependence.txt')
    words= f.read().replace('-',' ').split()

    for word in words: 
        word = word.replace('.','').replace(',','').replace(';', '').replace(':', '').replace('\'', '').replace('&', '').lower()

        if word not in filterB:
            print(word)  
   
    f.close()
   
main()
   


        
