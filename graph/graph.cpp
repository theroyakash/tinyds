#include <iostream>
#include <list>
#include <unordered_map>
#include <vector>
#include <utility>

using namespace std;

// Directed graph implementation
class Graph{ 
private:
	// adj_list structure: vertex -> pair<vertex, edge_weight>
    unordered_map<char, list<pair<char, int>>> adj_list;
    vector<pair<char, char>> E; // edge set
public:
    vector<pair<char, char>> edges(){
        return E;
    }

    void add_edge(char vertex1, char vertex2, int weight){
        adj_list[vertex1].push_front(make_pair(
            vertex2, weight
        ));

        E.push_back({vertex1, vertex2});
    }

    void register_vertex(vector<char> vertices){
        for (auto v:vertices){
            list<pair<char, int>> l;
            adj_list.insert({v, l});
        }
    }

    unordered_map<char, list<pair<char, int>>> view(){
        return adj_list;
    }
};
