class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (n<=1 || k==0) return;
        
        k = k%n;
        
        vector<int> temp;
        
        for (int i = 0; i < n; i++){
            temp.push_back(nums[(n - k + i)%n]);
        }
        
        nums = temp;
        
    }
};