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
	int __len__();
	bool is_empty();
	bool is_full();
	void enque(T value);
	T deque();
	T peak();
	void clear();
	int find(T value);
	int count(T value);
	bool __contains__(T value);
	void dump();
};

#include "Queue.hpp"

