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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> k;
        int len=lists.size()-1;
        if(lists.size()==0){
            return NULL;
        }
        for(int i=0 ;i<=len;i++){
            ListNode* p=lists[i];
            if(p==NULL){
                continue;
            }
            while(p!=NULL){
                k.push_back(p->val);
                p=p->next;
            }
        }
        sort(k.begin(),k.end());
        if(k.size()==0){
            return NULL;
        }
        ListNode* ans= new ListNode();
        ListNode* curr=ans;
        int length=k.size();
        for(int i=0;i<length;i++){
            curr->val=k[i];
            if(i<length-1){
                curr->next=new ListNode();
                curr=curr->next;
            }
        }
        return ans;
    }
};