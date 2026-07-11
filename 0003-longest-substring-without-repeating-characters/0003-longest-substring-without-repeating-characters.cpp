class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_set<char> st;

        int i = 0;
        int ans = 0;

        for (int j = 0; j < s.size(); j++) {

            // Jab tak duplicate hai, left se remove karo
            while (st.find(s[j]) != st.end()) {
                st.erase(s[i]);
                i++;
            }

            // Current character add karo
            st.insert(s[j]);

            // Maximum length update karo
            ans = max(ans, j - i + 1);
        }

        return ans;
    }
};