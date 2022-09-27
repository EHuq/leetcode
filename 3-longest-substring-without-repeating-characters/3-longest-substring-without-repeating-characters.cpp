class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size(), ans = 0;
        unordered_map<char, int> mp; // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (mp.find(s[j])!= mp.end()) {
                i = max(mp[s[j]], i);
            }
            ans = max(ans, j - i + 1);
            mp[s[j]] =  j + 1;
        }
        return ans;
        
    }
};