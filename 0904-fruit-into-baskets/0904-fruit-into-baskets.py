class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        max_fruits = 0
        fruit_count = {}

        for high in range(len(fruits)):
            fruit = fruits[high]

            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

            while len(fruit_count) > 2:
                left_fruit = fruits[low]
                fruit_count[left_fruit] -= 1

                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]

                low += 1

            max_fruits = max(max_fruits, high - low + 1)

        return max_fruits
        
            
           
                
                
                    
                
                
                    
                       
                    
        