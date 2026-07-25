class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # Stores unique triplets found during the search
        nums.sort() # sorting allows for two pointers and skip duplicates

        #iterate through list treating each as a root
        for i, a in enumerate(nums): 
            if a > 0: # positive roots cannot ever sum to zero
                break # stop loop because remaining numbers are positive

            #Check if current root matches previous root
            if i > 0 and a == nums[i-1]:
                continue #skip duplicate roots to avoid repeating triplets.

            #Set pointers at start and end remaining
            left, right = i+1, len(nums)-1
            while left < right: #Shrink window until two pointers meet.
                threeSum = a + nums[left] + nums[right] #Calculate current sum of the chosen three.
                if threeSum > 0: #Current total is too large for 0
                    right -= 1   # Decrease right pointer to reduce the Sum
                elif threeSum < 0:  #Current total is too small for 0
                    left += 1  #Increase left pointer to enlarge the Sum


                else:#Total exactly zero so valid triplet found
                    res.append([a,nums[left],nums[right]]) # add current valid triplet tp results list.
                    left += 1 #Move left and rigth pointer to find next combination
                    right -= 1
                    #Check if the new left value is duplicate
                    while nums[left] == nums[left-1] and left < right:
                        left += 1 # skip duplicate values to ensure unique results
            
            #Return the list containing all unique triplets
        return res 
