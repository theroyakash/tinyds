#include <iostream>

using namespace std;

// Instead of using a custom implementation for stack it is recommended to use a vector stl or a stack stl

int main() {
    // Usage of a vector as a stack
    vector<int> stk;
    
    // push into a stack
    stk.push_back(12);

    // popping some stack elements
    stk.pop_back();

    return 0;
}