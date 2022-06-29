#include <iostream>

using namespace std;

// Definition of the tree node
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


void inOrderTraversal(TreeNode *node){

    if (node != nullptr) {
        inOrderTraversal(node->left);
        printf("%d ", node->data);
        inOrderTraversal(node->right);
    }
}

void preOrderTraversal(TreeNode *node){

    if (node != nullptr) {
        printf("%d ", node->data);
        preOrderTraversal(node->left);
        preOrderTraversal(node->right);
    }
}

void postOrderTraversal(TreeNode *node){

    if (node != nullptr) {
        postOrderTraversal(node->left);
        postOrderTraversal(node->right);

        printf("%d ", node->data);
    }
}


int main() {
    TreeNode* node = new TreeNode(1200);
    node->left = new TreeNode(23);
    node->right = new TreeNode(314);

    node->right->right = new TreeNode(14124);

    inOrderTraversal(node);
}