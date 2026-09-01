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

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty()) {
            return nullptr;
        }

        TreeNode* answer = new TreeNode(preorder[0]);

        auto it = find(inorder.begin(), inorder.end(), preorder[0]);
        if (it != inorder.end()) {
            int idx = distance(inorder.begin(), it);

            vector<int> preleft(preorder.begin()+1, preorder.begin()+1+idx);
            vector<int> preright(preorder.begin()+idx+1, preorder.end());
            vector<int> inleft(inorder.begin(), inorder.begin()+idx);
            vector<int> inright(inorder.begin()+idx+1, inorder.end());

            answer->left = buildTree(preleft, inleft);
            answer->right = buildTree(preright, inright);
        }

        return answer;
    }
};