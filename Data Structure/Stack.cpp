#include <iostream>
using namespace std;

template<class T>
class Stack
{
private:
	T * stk;
	int capacity;
	int ptr = 0;
	
public:
	Stack(int n)
	{
		capacity = n;
		ptr = 0;
		stk = new T[capacity];
	}

	int __len__()
	{
		return ptr;
	}

	bool is_empty()
	{
		return ptr <= 0;
	}

	bool is_full()
	{
		return ptr >= capacity;
	}

	void push(T value)
	{
		if (is_full())
			return;

		stk[ptr] = value;
		ptr += 1;
	}

	T pop()
	{
		if (is_empty())
			return NULL;
		ptr -= 1;
		return stk[ptr];
	}

	T peak()
	{
		if (is_empty())
			return -1;

		return stk[ptr-1];
	}

	void clear()
	{
		ptr = 0;
		return;
	}

	int find(T value)
	{
		for (int i = ptr - 1; i > 0; i--)
		{
			if (stk[i] == value)
				return i;
		}
		return -1;
	}

	int count(T value)
	{
		int c = 0;
		for (int i = 0; i < ptr; i++)
		{
			if (stk[i] == value)
				c += 1;	
		}
		return c;
	}

	bool __contains__(T value)
	{
		if (count(value) > 0)
			return true;
		else
			return false;
	}

	void dump()
	{
		if (is_empty())
			cout << "스택이 비어있습니다." << endl;
		else
		{
			for (int i = 0; i < ptr; i++)
				cout << stk[i] << " ";
			cout << endl;
		}
	}
};

int main()
{
	Stack<char> s = Stack<char>(5);

	s.push('a');
	s.push('b');
	s.push('c');
	char pop = s.pop();
	cout << pop << endl;
	s.dump();

	return 0;
}
