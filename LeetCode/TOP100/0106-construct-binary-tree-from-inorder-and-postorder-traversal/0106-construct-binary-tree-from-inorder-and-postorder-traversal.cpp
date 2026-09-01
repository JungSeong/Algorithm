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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.empty()) {
            return nullptr;
        }

        int root = postorder.back(); // 가장 마지막 원소가 해당 subTree의 root값이다
        auto it = find(inorder.begin(), inorder.end(), root);
        TreeNode* answer = new TreeNode(root);

        if (it != inorder.end()) {
            int idx = distance(inorder.begin(), it);
            vector<int> leftinorder(inorder.begin(), inorder.begin()+idx);
            vector<int> rightinorder(inorder.begin()+idx+1, inorder.end());
            vector<int> leftpostorder(postorder.begin(), postorder.begin()+idx);
            vector<int> rightpostorder(postorder.begin()+idx, postorder.end()-1);

            answer->left = buildTree(leftinorder, leftpostorder);
            answer->right = buildTree(rightinorder, rightpostorder);
        }

        return answer;
    }
};