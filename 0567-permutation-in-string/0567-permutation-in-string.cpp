class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size())
    return false;
        sort (s1.begin() , s1.end());
        int k = s1.size();
        for(int j = 0 ; j <= s2.size()-k; j++){
           string temp = s2.substr(j,k);
           sort(temp.begin(), temp.end());
           if(temp == s1)
            return true;
        }
        return false;
    }
};