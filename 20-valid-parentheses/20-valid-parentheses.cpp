class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 0){
            return true;
        }
        if (s.length() == 1){
            return false;
        }
        stack <char> stack;
        for (int i = 0; i < s.length(); i++){
            char temp = s[i];
            if (temp == '(' || s[i] == '[' || s[i] == '{'){
                stack.push(temp);
            } 
            else if (temp == ']' ||temp == '}' ||temp == ')'){
                if (stack.size() == 0){
                    return false;
                }else if(temp == ']' && stack.top() == '['){
                    stack.pop();
                } else if(temp == '}' && stack.top() == '{'){
                    stack.pop();
                } else if (temp == ')' && stack.top() == '('){
                    stack.pop();
                }else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        if (stack.size() == 0){
            return true;
        }
        return false;
    }
};
