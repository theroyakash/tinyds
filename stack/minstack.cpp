#include <iostream>
#include <vector>

using namespace std;

class MinStack{
private:
    vector<int> stack;
    vector<int> auxStack;
    int ClassPrivateSize;

public:
    MinStack(){
        ClassPrivateSize = 0;
    }

    int size(){
        return ClassPrivateSize;
    }

    void push(int value){

        if (ClassPrivateSize == 0){
            stack.push_back(value);
            auxStack.push_back(value);
            ClassPrivateSize += 1;
        }else{
            if (value < auxStack.back()){
                stack.push_back(value);
                auxStack.push_back(value);
            }else{
                stack.push_back(value);
            }
            ClassPrivateSize += 1;
        }
    }

    int pop(){
        if (ClassPrivateSize == 0){
            throw runtime_error("pop(): Empty Stack");
        }else{

            if (auxStack.back() == stack.back()){
                int value = stack.back();
                auxStack.pop_back();
                stack.pop_back();

                return value;
            }else{
                int value = stack.back();
                stack.pop_back();
                return value;
            }
            ClassPrivateSize -=1;
        }
    }

    bool isEmpty() const{
        if (ClassPrivateSize == 0){
            return true;
        }
        return false;
    }

    int min(){
        return auxStack.back();
    }

    int peek() {
        return stack.back();
    }

};
