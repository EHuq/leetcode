/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head||!head->next||!head->next->next) return head;
        
        ListNode* odd = head,*prevodd=NULL;
        ListNode* even = head->next,*curr_even=head->next;
        
        while(curr_even&&curr_even->next){
        
            
                odd->next = odd->next->next;
            
                odd = odd->next;    
            
            
                curr_even->next = curr_even->next->next;
                
                curr_even = curr_even->next;    
            
            
        }
        odd->next=even;
        return head;
        
    }
};