/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
const int N = 100001;
vector<int>adj[N];
class Solution {
    public:
      struct TraverseDists {
        int distToDisease = 0;
        int length = 0;
    };

    int amountOfTime(TreeNode* root, int start) {
        int time = 0;
        traverse(root, start, time);
        return time;
    }

    TraverseDists traverse(TreeNode* root, int start, int& time) {
        TraverseDists result;
        if (!root)
            return result;

        // We traverse nodes from root to left subtree first
        // If we find disease node in that subtree we need to return distance from root to disease node
        // If we wont find disease node in that subtree than we need to find distance to longest leaf
        TraverseDists left = traverse(root->left, start, time);
        TraverseDists right = traverse(root->right, start, time);

        // Current node is a node with disease
        if (root->val == start) {
            time = max(left.length, right.length);
            result.distToDisease = 1;
            return result;
        }

        // We haven't found node with disease on any of child subtrees
        // In that case we need to return distance to most far leaf from those subtrees
        if (left.distToDisease == 0 && right.distToDisease == 0) {
            result.length = max(left.length, right.length) + 1;
            return result;
        }

        // One of subtrees has disease
        if (left.distToDisease > 0) {
            time = max(time, right.length + left.distToDisease);
            result.distToDisease = left.distToDisease + 1;
            return result;
        }

        if (right.distToDisease > 0) {
            time = max(time, left.length + right.distToDisease);
            result.distToDisease = right.distToDisease + 1;
            return result;
        }

        return result;
    }
};