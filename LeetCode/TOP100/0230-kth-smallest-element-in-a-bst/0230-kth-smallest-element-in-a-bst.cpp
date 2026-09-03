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
    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        deque<TreeNode*> dq;
        TreeNode* Node;

        dq.push_back(root);

        while (!dq.empty()) {
            Node = dq.front();
            dq.pop_front();
            pq.push(Node->val);

            if (Node->left) {
                dq.push_back(Node->left);
            }

            if (Node->right) {
                dq.push_back(Node->right);
            }
        }

        for (int i=0; i<k-1; i++) {
            pq.pop();
        }

        return pq.top();
    }
};