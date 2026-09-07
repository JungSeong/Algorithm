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
    TreeNode* insertNode(int left, int right, vector<int>& nums) {
        if (left > right) {
            return nullptr;
        }

        int mid = (left+right)/2;

        TreeNode* node = new TreeNode(nums[mid]);
        node->left = insertNode(left, mid-1, nums);
        node->right = insertNode(mid+1, right, nums);

        return node;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;

        return insertNode(left, right, nums);
    }
};