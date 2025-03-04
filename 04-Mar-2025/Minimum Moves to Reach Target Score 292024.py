# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxi: int) -> int:
        count = 0

        while target > 1:
            if maxi == 0:
                count += target - 1
                break

            if maxi > 0 and target % 2 == 0:
                target //= 2
                maxi -= 1
                
            else:
                target -= 1
            count += 1
            
        return count

       
        

       

        