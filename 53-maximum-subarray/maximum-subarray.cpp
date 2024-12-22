class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current = 0, a = INT_MIN;
        for (int i : nums) {
            current += i;
            a = max(a, current);
            if (current < 0) {
                current = 0;
            }
        }
        return a;
    }
};
