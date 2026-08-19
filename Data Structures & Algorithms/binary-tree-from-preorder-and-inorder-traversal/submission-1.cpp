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

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() or inorder.empty()) return nullptr;

        TreeNode* root = new TreeNode(preorder[0]);

        auto it = find(inorder.begin(), inorder.end(), preorder[0]);
        int index = distance(inorder.begin(), it);

        vector<int> preleft(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> inleft(inorder.begin(), inorder.begin() + index);   
        root->left = buildTree(preleft, inleft);

        vector<int> preright(preorder.begin() + index + 1, preorder.end());
        vector<int> inright(inorder.begin() + index + 1, inorder.end());   
        root->right = buildTree(preright, inright);

        return root;
    }
};
