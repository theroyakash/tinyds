#include <iostream>
#include <vector>

using namespace std;

// without using union by rank optimization
class DSU {
private:
    int size;
    vector<int> dsuArray;
public:
    DSU(int n) {
        int size = n;
        for (int i=0;i<n+1;i++) {
            dsuArray.push_back(i);
        }
    }
    
    vector<int> getArray() {
        return dsuArray;
    }
    
    int find(int n) {
        return dsuArray[n];
    }
    
    bool makeUnion(int i, int j) {
        int parent_i = find(i);
        int parent_j = find(j);
        
        if (parent_i == parent_j) return false;
        
        // find all occurences of parent_j
        // set to parent_i to make the Union
        for (int i=1; i<dsuArray.size(); i++) {
            if (dsuArray[i] == parent_j) {
                dsuArray[i] = parent_i;
            }
        }
        
        return true;
    }
};

int main() {

    int numberOfNodes = 5;

    // check if some edge is possible to add (to not create a cycle)
    DSU dsu = DSU(numberOfNodes);
    vector<vector<int>> edges = {{1,2}, {2,3}, {3,4}, {4, 5}, {1,5}};
    
    for (auto edge : edges) {
        int from = edge[0];
        int to = edge[1];

        bool possible = dsu.makeUnion(from, to);
        if (not possible) {
            cout << "Edge from " << from << " to " << to << " is not possible to add" << endl;
        } else {
            cout << "Edge from " << from << " to " << to << " added successfully" << endl;
        }
    }
    
    return 0;
}