class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftsum(n);
        vector<int> rightsum(n);

        int left = 0;
        for(int i = 1 ; i < n ; i++){
            leftsum[0] = 0;
            
            left += nums[i-1];
             leftsum[i] = left;
        }

        int right = 0;
        for(int i = n-2 ; i >= 0 ; i--){
            rightsum[n-1] = 0;
           
            right += nums[i+1];
           rightsum[i] = right;
        }
        for(int i = 0 ; i < nums.size() ; i++){
            nums[i] = abs(rightsum[i] - leftsum[i]);
        }
        return nums;
    }
};