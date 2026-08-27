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
    bool compTree(TreeNode* rootNode, TreeNode* subrootNode) {
        if (!rootNode && !subrootNode) { // 두 Node모두 존재하지 않는다면 (해당 방향으로 모두 이상이 없다면)
            return true;
        }
        else if ((!rootNode && subrootNode) || (rootNode && !subrootNode)) { // 하나의 Node만 존재한다면
            return false;
        }
        else {
            if (rootNode->val != subrootNode->val) {
                return false;
            }
            else {
                return compTree(rootNode->left, subrootNode->left) && compTree(rootNode->right, subrootNode->right);
            }
        }
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        deque<TreeNode*> dq;
        TreeNode* Root;
        bool answer = false;
        dq.push_back(root);

        while (!dq.empty()) {
            Root = dq.front();
            dq.pop_front();
            
            if (compTree(Root, subRoot)) {
                answer = true;
                break;
            }
            else {
                if (Root->left) {
                    dq.push_back(Root->left);
                }
                if (Root->right) {
                    dq.push_back(Root->right);
                }
            }
        }

        return answer;
    }
};