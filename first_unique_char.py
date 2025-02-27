class firstunique:
    def __init__(self, input):
        self.input = input

    # Brute force method
    # Time complexity O(n^2) - Quadratic   
    def fisrt_unique_char(self):
        i = 0
        j = 1
        str_len = len(self.input)
        
        for i in range(str_len):
            count = 0
            for j in range(str_len):
                if self.input[i] == self.input[j]:
                    count+=1
                
            if count == 1:
                return i
        return -1
            
       
stringg= "kookltt"
# stringg= "leelt"
obj = firstunique(stringg)
print(obj.fisrt_unique_char())