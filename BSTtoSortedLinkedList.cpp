#include <iostream>

using namespace std;
/* A binary tree tNode has data, pointer to left child
and a pointer to right child */
class tNode
{
public:
        int data;
        tNode* left;
        tNode* right;
    tNode() {}
        tNode(int data) {
                this->data = data;
                this->left = NULL;
                this->right = NULL;
        }
};


void bstToList(tNode *&root, tNode **head, tNode **tail){
    if (root->left != NULL) {
        tNode *left_head;
        tNode *left_tail;
        bstToList(root->left, &left_head, &left_tail);
        left_tail->right = root;
        root->left = left_tail;
        *head = left_head;
    }
    else
        *head = root;
    
    if (root->right != NULL) {
        tNode *right_head;
        tNode *right_tail;
        bstToList(root->right, &right_head, &right_tail);
        root->right = right_head;
        right_head->left = root;
        *tail = right_tail;
    }
    else
        *tail = root;
}
        


int main() {
        /* Constructed binary tree is
                4
              /   \
            2      5
          /  \
        1     3
        */
        tNode *root1 = new tNode(4);
        root1->left = new tNode(2);
        root1->right = new tNode(5);
        root1->left->left = new tNode(1);
        root1->left->right = new tNode(3);
    tNode *head;
    tNode *tail;
    
    bstToList(root1, &head, &tail);
    while(NULL != head) {
        cout<<head->data<<endl;
        head = head->right;
    }
        return 0;
}
