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
        if (!node) {
            return 0;
        }
        int left = height(node->left);
        int right = height(node->right);

        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int answer = 0;
        deque<TreeNode*> dq;

        if (root) {
            dq.push_back(root);
        }
        else {
            return 0;
        }

        while (!dq.empty()) {
            TreeNode* Node = dq.front();
            dq.pop_front();

            int diam = height(Node->left)+height(Node->right);

            answer = max(answer, diam);

            if (Node->left) {
                dq.push_back(Node->left);
            }
            if (Node->right) {
                dq.push_back(Node->right);
            }
        }

        return answer;
    }
};