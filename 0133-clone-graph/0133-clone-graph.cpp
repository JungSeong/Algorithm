/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<Node*, Node*> cloned;

    Node* dfs(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        if (cloned.count(node)) {
            return cloned[node];
        }

        Node* copy = new Node(node->val);
        cloned[node] = copy;

        for (Node* next : node->neighbors) {
            copy->neighbors.push_back(dfs(next));
        }

        return copy;
    }

    Node* cloneGraph(Node* node) {
        return dfs(node);
    }
};