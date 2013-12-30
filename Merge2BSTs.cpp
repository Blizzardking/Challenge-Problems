#include <iostream>
#include <stack>
using namespace std;
/* A binary tree tNode has data, pointer to left child
and a pointer to right child */
struct tNode
{
        int data;
        struct tNode* left;
        struct tNode* right;
};

struct tNode* newtNode(int data)
{
        struct tNode* tNode = new struct tNode();
        tNode->data = data;
        tNode->left = NULL;
        tNode->right = NULL;

        return tNode;
}

void left_side_stack(struct tNode* root, stack<struct tNode*> &stack) {
        if (NULL == root)
                return;
        stack.push(root);
        if (NULL == root->left)
                return;
        else
                left_side_stack(root->left, stack);
}

void print_merge(stack<struct tNode*> &stack1, stack<struct tNode*> &stack2) {
        while (!stack1.empty() && !stack2.empty()) {
                struct tNode* top1 = stack1.top();
                struct tNode* top2 = stack2.top();
                if (top1->data < top2->data) {
                        cout << top1->data << " ";
                        stack1.pop();
                        if (NULL != top1->right)
                                left_side_stack(top1->right, stack1);
                }
                else {
                        cout << top2->data << " ";
                        stack2.pop();
                        if (NULL != top2->right)
                                left_side_stack(top2->right, stack2);
                }

        }
        while (!stack1.empty()) {
                struct tNode* top1 = stack1.top();
                cout << top1->data << " ";
                stack1.pop();
                if (NULL != top1->right)
                        left_side_stack(top1->right, stack1);
        }
        while (!stack2.empty()) {
                struct tNode* top2 = stack2.top();
                cout << top2->data << " ";
                stack2.pop();
                if (NULL != top2->right)
                        left_side_stack(top2->right, stack2);
        }
}

void merge_BSTs(struct tNode* root1, struct tNode* root2) {
        stack<struct tNode*> stack1, stack2;

        left_side_stack(root1, stack1);
        left_side_stack(root2, stack2);
        print_merge(stack1, stack2);
}


int main() {


        /* Constructed binary tree is
        4
        /   \
        2      5
        /  \
        1     3
        */
        struct tNode *root1 = newtNode(4);
        root1->left = newtNode(2);
        root1->right = newtNode(5);
        root1->left->left = newtNode(1);
        root1->left->right = newtNode(3);
        struct tNode *root2 = newtNode(5);
        root2->left = newtNode(3);
        root2->right = newtNode(6);
        root2->left->left = newtNode(2);
        root2->left->right = newtNode(4);
        stack<struct tNode*> stack1;

        merge_BSTs(root1, root2);
}


