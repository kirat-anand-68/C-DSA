#include <iostream>
#include <cstdlib> // For malloc()
using namespace std;

struct node {
    int data;
    struct node* link;
} *start = NULL;

void Insert_atStart(int key) {
    struct node* ptr;
    ptr = (struct node*)malloc(sizeof(struct node)); // Allocate memory for new node

    if (ptr != NULL) {
        ptr->data = key;
        ptr->link = start;
        start = ptr;
    } else {
        cout << "Memory Unavailable" << endl;
    }
}

void print() {
    struct node* ptr = start;
    while (ptr != NULL) {
        cout << ptr->data << " -> ";
        ptr = ptr->link;
    }
    cout << "NULL" << endl; // Indicate the end of the list
}

int main() {
    Insert_atStart(10);
    Insert_atStart(20);
    Insert_atStart(30);

    cout << "Linked List Traversal: ";
    print();

    return 0;
}
