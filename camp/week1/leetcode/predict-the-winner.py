class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        
        def predict(l,r,turn):
            if l>r:
                return [0,0]
            if turn =='p1':
                left=predict(l+1,r,'p2')
                left[0]+=nums[l]
                right=predict(l,r-1,'p2')
                right[0]+=nums[r]

                if left[0]>right[0]:
                    return left
                return right
            else:
                left=predict(l+1,r,'p1')
                left[1]+=nums[l]
                right=predict(l,r-1,'p1')
                right[1]+=nums[r]

                if left[1]>right[1]:
                    return left
                return right
        ans=predict(0,len(nums)-1,'p1')
        return ans[0]>=ans[1]
           