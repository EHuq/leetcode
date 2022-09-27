class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right =  height.size() - 1;
        int max = min(height[left], height[right])*(right - left);
        while (right > left){
            if (height[left] > height[right]){
                right--;
            }
            else {
                left++;
            }
            int temp = min(height[left], height[right])*(right - left);
            if (temp > max){
                max = temp;
            }
        }
        return max;
    }
};










