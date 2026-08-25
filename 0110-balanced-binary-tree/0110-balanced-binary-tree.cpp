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
    int height(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        return 1+max(height(node->left), height(node->right));
    }

    bool isBalanced(TreeNode* root) {
        deque<TreeNode*> dq;
        if (!root) {
            return true;
        }
        else {
            dq.push_back(root);
        }

        while (!dq.empty()) {
            TreeNode* node = dq.front();
            dq.pop_front();

            if (abs(height(node->left)-height(node->right)) > 1) {
                return false;
            }

            if (node->left) {
                dq.push_back(node->left);
            }
            if (node->right) {
                dq.push_back(node->right);
            }
        }

        return true;
    }
};