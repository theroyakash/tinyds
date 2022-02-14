<h1 align="center">
  <br>
  TinyDS
  <br>
</h1>

<h4 align="center">Python Package for your SDE interviews.</h4>

<p align="center">
  <a href="https://algorithms.theroyakash.com/">Getting started</a> •
  <a href="https://github.com/theroyakash/tinyds/blob/main/LICENSE">License</a>
</p>

[![TinyDS Tests](https://github.com/theroyakash/tinyds/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/theroyakash/tinyds/actions/workflows/tests.yml)
[![Python3](https://img.shields.io/badge/python-3.9-blue.svg)](https://github.com/theroyakash/reddit-api)
[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/theroyakash/AKDSFramework/blob/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-theroyakash-red)](https://www.theroyakash.com/contact)

# What is it?
Small and simple pythonic implementations for most of your coding problems that are asked in SDE I or II interviews at FAANGs that you will be able to implement on the spot if asked. You can also install the package and start using it in Leetcode problems. Think of it as a tiny implementation of the `stl` library from C++. If you want to contribute please open a pull request.

# What it supports?
## Data Structures
- Linked List as a class
- Queues as a class, Queue with `Max()` API
- Stacks as a class, Stack with `Max()` API
- Circular Queue
- Heaps as a class instead of the default `heapq` usage
- Trees and graphs as a class
- BiMap (Bi-directional Maps) Implementation, (HashMap implementation is not covered because on one will implement `dict = {}` if you can use it).
- Multi-threaded dictionary Implementation

# Algorithms
- BFS, DFS
- Few sorting algorithms
- Binary Search
- Djikstra, Bellman ford, floyd warshall algorithm
- In-order Pre-order, Post-order traversal of Binary trees
- Tree Satisfiability
    - Given Binary Tree is BST
    - Given Binary Tree is Max or MinHeap
    - Given Binary Tree is height-balanced
    - Given Binary Tree is symmetric
- Binary Tree Generation algorithm
- Few DP problems and a decorator for DP function call caching