#pragma once
#include <iostream>
using namespace std;

template<class T>
class Queue
{
private:
	T* que;
	int capacity;
	int front;
	int rear;
	int no;

public:
	Queue(int);
	~Queue();
	int __len__();
	bool is_empty();
	bool is_full();
	void enque(T);
	T deque();
	T peak();
	void clear();
	int find(T);
	int count(T);
	bool __contains__(T);
	void dump();
};

#include "Queue.hpp"

