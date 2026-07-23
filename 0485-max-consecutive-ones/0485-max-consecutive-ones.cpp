class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int one = 0;
        
        for(int j = 0 ; j < nums.size() ; j++){
               if(nums[j] == 1){
                one++;
               }
               else{
                one = 0;
               }
                ans = max(ans,one);
            
        }
        return ans;
    }
};