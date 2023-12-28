class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>x;
        for(int i=0;i<nums.size();i++){
           int counter=0;
            for(int j=0;j<nums.size();j++){
               if(nums[i]>nums[j]) counter++;
            }
            x.push_back(counter);
        }
        return x;
    }
};