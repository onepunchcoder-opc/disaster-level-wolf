# Brutal force O(m*n)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for x in arr1:
            count = 1
            for y in arr2:
                if abs(x - y) <= d:
                    count = 0
                    break
            ans += count
        return ans
        
        
  # Binary Search O(n*lgn)    
  class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:      
        ans, l = 0, len(arr2)
        arr2.sort()  # sort
        for num in arr1:
            index = bisect.bisect_left(arr2, num)  # binary search
            min_dist = float('inf')
            if index > 0:  # check left neighbour
                min_dist = min(min_dist, abs(num - arr2[index - 1]))
            if index < l:  # check right neighbour
                min_dist = min(min_dist, abs(num - arr2[index]))
            if min_dist > d:  # compare
                ans += 1
        return ans
