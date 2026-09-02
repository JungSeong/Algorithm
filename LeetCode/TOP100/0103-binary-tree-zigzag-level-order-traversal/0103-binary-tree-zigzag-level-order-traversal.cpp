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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        deque<TreeNode*> dq;
        
        if (!root) {
            return answer;
        }
        else {
            int level = 0;
            dq.push_back(root);

            while (!dq.empty()) {
                vector<int> cur_val;
                deque<TreeNode*> next_level;

                while (!dq.empty()) {
                    TreeNode* Node = dq.front();
                    dq.pop_front();
                    cur_val.push_back(Node->val);

                    if (Node->left) {
                        next_level.push_back(Node->left);
                    }

                    if (Node->right) {
                        next_level.push_back(Node->right);
                    }
                }

                if (level%2!=0) { // 홀수 레벨인 경우
                    reverse(cur_val.begin(), cur_val.end());
                }
                answer.push_back(cur_val);
                
                for (const auto& Node : next_level) {
                    dq.push_back(Node);
                }

                level++;
            }

            return answer;
        }
    }
};