#include <iostream>
using namespace std;

template<class T>
class Queue
{
private:
	T * que;
	int capacity;
	int front;
	int rear;
	int no;

public:
	Queue(int n)
	{
		capacity = n;
		front = 0;
		rear = 0;
		no = 0;
		que = new T[capacity];
	}

	int __len__()
	{
		return no;
	}

	bool is_empty()
	{
		return no <= 0;
	}

	bool is_full()
	{
		return no >= capacity;
	}

	void enque(T value)
	{
		if (is_full())
			return;

		que[rear] = value;
		rear += 1;
		no += 1;

		if (rear == capacity)
			rear = 0;
	}

	T deque()
	{
		if (is_empty())
			return NULL;

		T value = que[front];
		front += 1;
		no -= 1;

		if (front == capacity)
			front = 0;

		return value;
	}

	T peak()
	{
		if (is_empty())
			return -1;

		return que[front];
	}

	void clear()
	{
		no = 0;
		front = 0;
		rear = 0;
		return;
	}

	int find(T value)
	{
		int idx = 0;
		for (int i = 0; i < no; i++)
		{
			idx = (i + front) % capacity;
			if (que[idx] == value)
				return idx;
		}
		return -1;
	}

	int count(T value)
	{
		int c = 0;
		int idx = 0;
		for (int i = 0; i < no; i++)
		{
			idx = (i + front) % capacity;
			if (que[i] == value)
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
			for (int i = 0; i < no; i++)
				cout << que[(i + front) % capacity] << " ";
			cout << endl;
		}
	}
};

int main()
{
	Queue<char> q = Queue<char>(5);

	q.enque('a');
	q.enque('c');
	q.enque('b');
	char de = q.deque();
	cout << de << endl;
	q.dump();

	return 0;
}
