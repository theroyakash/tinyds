#include <iostream>
#include <vector>

using std::cout;
using std::endl;

/** 
 * Interface: MaxHeapify of std::vector vector, and the violation is at atIndex
 * Only solves a single violation
 * This is for maintaining the heap property
*/
void maxHeapify(std::vector<int> *vector, int atIndex){

    int leftChildren = atIndex*2 + 1;
    int rightChildren = atIndex*2 + 2;

    int largest = atIndex;

    // Now check of what is larger the left children or the current Index?
    if ((leftChildren < vector->size()) && ((*vector)[leftChildren] > (*vector)[largest])){
        largest = leftChildren;

    }

    // Now check of what is larger the right children or the current Index?
    if ((rightChildren < vector->size()) && ((*vector)[rightChildren] > (*vector)[largest])){
        largest = rightChildren;
    }

    // If some largest is either present in the left or right children means a swap is needed.
    if (largest != atIndex){
        std::swap((*vector)[atIndex], (*vector)[largest]);

        // Recursively call to maxHeapify the affected children
        maxHeapify(vector, largest);
    }
}

/** 
 * Build heap procedure. Runs in O(N) time in-place.
 * Each leaf-node in a heap is a heap. The procedure BUILD-MAX-HEAP goes through the remaining nodes of the
 * tree and runs MAX-HEAPIFY on each one
*/
void buildMaxHeap(std::vector<int> *vector){

    int heapSize = vector->size();

    int lastHeadIndex = heapSize / 2 - 1;

    for (int i = lastHeadIndex; i >= 0; i--) {
        maxHeapify(vector, i);
    }
}
