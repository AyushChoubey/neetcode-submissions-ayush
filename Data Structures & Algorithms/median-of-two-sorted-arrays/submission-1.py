class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Please check th bonus pdf from the book Coding Interview Patterns
        # the median will exist in the middle of the merged array
        # so let's count the total elements in the merged array 
       
        
        if len(nums1)> len(nums2):
            nums1, nums2 = nums2, nums1
        m , n = len(nums1), len(nums2)
        left, right  = 0, m-1
        half_part = (m+n)//2
        while True:
            l1_index = (left+right)//2
            l2_index = half_part -(l1_index+1)-1

            L1 = float('-inf') if l1_index< 0 else nums1[l1_index]
            L2 = float('-inf') if l2_index< 0 else nums2[l2_index]
            R1 = float('inf') if l1_index>= m-1 else nums1[l1_index+1]
            R2 = float('inf') if l2_index>= n-1 else nums2[l2_index+1]

            if L1 >R2:
                right = l1_index -1
            elif L2> R1:
                left = l1_index +1
            else:
                if ((m+n)%2) == 0:
                    return (max(L1,L2)+min(R1,R2))/2.0 
                    
                else:
                    return min(R1,R2) 
  





            