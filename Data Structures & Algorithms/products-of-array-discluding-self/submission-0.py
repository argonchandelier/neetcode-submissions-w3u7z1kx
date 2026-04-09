class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mults_forward = [1] * n
        mults_backward = [1] * n
        product_forward = 1
        product_backward = 1
        for i in range(n-1):
            rev_i = n-i-1
            product_forward *= nums[i]
            product_backward *= nums[rev_i]
            mults_forward[i] = product_forward
            mults_backward[rev_i] = product_backward
        print(mults_forward, mults_backward)
        outputs = [1] * n
        for i in range(n):
            prev_product = 1
            for_product = 1
            if i > 0:
                prev_product = mults_forward[i-1]
            if i < n-1:
                for_product = mults_backward[i+1]
            outputs[i] = prev_product*for_product
        
        return outputs
            