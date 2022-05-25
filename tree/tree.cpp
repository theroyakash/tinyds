#include <iostream>

using namespace std;

struct TreeNode {
    int data;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int value) {
        data  = value;
        left  = nullptr;
        right = nullptr;
    }
};

// Create a Tree Structure
int main() {
    TreeNode *root = new TreeNode(12);
    root->left     = new TreeNode(112);
    root->right    = new TreeNode(44);
}
