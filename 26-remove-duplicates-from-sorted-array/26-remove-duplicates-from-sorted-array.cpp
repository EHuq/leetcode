class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if (len > 0){
            
            int tmp = nums[0];
            for (int i = 0; i < nums.size(); i++){
                if (i > 0){
                    if (tmp != nums[i] && i != 0){
                        tmp = nums[i];
                    }else {
                        nums.erase(nums.begin()+i);
                        i--;
                    }    
                }
                
            }
            
        }
        return nums.size();
        
    }
};