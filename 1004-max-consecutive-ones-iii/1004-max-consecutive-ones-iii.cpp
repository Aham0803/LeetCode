class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // int ans = 0;
        // for(int i = 0 ; i < nums.size(); i++){
        //     int zero = 0;
        //     for(int j = i ; j < nums.size() ; j++){
        //         if(nums[j] == 0){
        //         zero++;
        //         }
        //         if(zero > k){
        //         break;
        //         }
        //         ans = max(ans, j-i +1);
        //         }
        //     }
        // return ans;
        int ans = 0 ;
        int i = 0 ;
         int zero = 0;
        for(int j = i ; j < nums.size() ; j++){
            if(nums[j] == 0){
                zero++;
            }
            while(zero > k){
                if(nums[i] == 0){
                    zero --;
                }
                i++;
            }
            ans = max(ans , j-i+1);
        }
        return ans;
    }
};