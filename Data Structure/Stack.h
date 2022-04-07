#pragma once
#include <iostream>
using namespace std;

template<class T>
class Stack
{
private:
	T* stk;
	int capacity;
	int ptr;

public:
	Stack(int);
	~Stack();
	int __len__();
	bool is_empty();
	bool is_full();
	void push(T);
	T pop();
	T peak();
	void clear();
	int find(T);
	int count(T);
	bool __contains__(T);
	void show();
};

#include "Stack.hpp"
