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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> answer;

        if (!root) {
            return answer;
        }
        else {
            deque<TreeNode*> dq;
            dq.push_back(root);

            while (!dq.empty()) {
                vector<TreeNode*> subNodes;
                vector<int> vals;

                while (!dq.empty()) {
                    TreeNode* Node = dq.front();
                    dq.pop_front();
                    
                    vals.push_back(Node->val);
                    if (Node->left) {
                        subNodes.push_back(Node->left);
                    }
                    if (Node->right) {
                        subNodes.push_back(Node->right);
                    }
                }

                if (!subNodes.empty()) {
                    for (const auto& Node : subNodes) {
                        dq.push_back(Node);
                    }
                }

                if (!vals.empty()) {
                    answer.push_back(vals);
                }
            }

            return answer;
        }
    }
};