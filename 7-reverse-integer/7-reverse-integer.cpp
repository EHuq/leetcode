class Solution {
public:
    int reverse(int x) {
        int fac = 1;
        if (x < 0 && x < INT_MAX *-1){
            return 0;
        }
        if (x < 0){
            fac = -1;
            x *= -1;
        }
        int num = 0;
        while (x > 0 && num <= ceil(INT_MAX / 10)) {
            num = num *10 + x%10;
            x /= 10;
        }

        if (num > ceil(INT_MAX / 10) && x > 0){
            return 0;
        }
        return num * fac;
    }
};