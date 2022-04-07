#pragma once
#include<iostream>

using namespace std;

template<class T>
struct Node
{
	T data;
	struct Node<T> *next = nullptr;
};

template<class T>
class Linked_List
{
private:
	Node<T> *head;
	Node<T> *tail;
	int size = 0;
public:
	Linked_List();
	~Linked_List();
	int __len__();
	bool is_empty();
	void addNode(T);
	void insertNode(int, T);
	void removeNode(int);
	void show();
};

#include "Linked_List.hpp"