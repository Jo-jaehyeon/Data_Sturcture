#pragma once
#include <iostream>
using namespace std;

template<class T>
class Arrays
{
private:
	T* arr;
	int capacity;
	int size;

public:
	Arrays(int);
	~Arrays();
	int __len__();
	bool is_full();
	bool is_empty();
	void insert(int, T);
	void replace(int, T);
	void remove(int);
	T at(int);
};

#include "Arrays.hpp"

