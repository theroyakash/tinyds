#include <iostream>

using std::cout;
using std::endl;

// Singly Linked List implementation

// Make a list node this will be the
// building block for the main linked list.
class ListNode {
public:
    int value;
    ListNode *next;

    ListNode(int value) {
        this->value = value;
        this->next = nullptr;
    }
};

class LinkedList {
private:
    ListNode *head;
public:
    LinkedList(ListNode* start) {
        head = start;
    }

    ListNode* getHead() {
        return head;
    }

    void push_front(ListNode* newNode) {
        ListNode* oldHead = head;
        head = newNode;
        newNode->next = oldHead;
    }
};

int main() {
    return 0;
}