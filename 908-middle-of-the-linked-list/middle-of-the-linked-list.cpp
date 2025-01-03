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
    ListNode* middleNode(ListNode* head) {
        ListNode *ptr=head;
        int length=1;
        while (ptr->next !=NULL){
            ptr=ptr->next;
            length++;
        } 
                ListNode* temp = head;
        for (int i = 1; i < (length / 2) + 1; i++) {
            temp = temp->next;
        }
        return temp;
    }
};