template<class T>
Queue<T>::Queue(int n)
{
	capacity = n;
	front = 0;
	rear = 0;
	no = 0;
	que = new T[capacity];
}

template<class T>
Queue<T>::~Queue() { delete[] que }

template<class T>
int Queue<T>::__len__() { return no; }

template<class T>
bool Queue<T>::is_empty() { return no <= 0; }

template<class T>
bool Queue<T>::is_full() { return no >= capacity; }

template<class T>
void Queue<T>::enque(T value)
{
	if (is_full())
		return;

	que[rear] = value;
	rear += 1;
	no += 1;

	if (rear == capacity)
		rear = 0;
}

template<class T>
T Queue<T>::deque()
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

template<class T>
T Queue<T>::peak()
{
	if (is_empty())
		return NULL;

	return que[front];
}

template<class T>
void Queue<T>::clear()
{
	no = 0;
	front = 0;
	rear = 0;
	return;
}

template<class T>
int Queue<T>::find(T value)
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

template<class T>
int Queue<T>::count(T value)
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

template<class T>
bool Queue<T>::__contains__(T value) { return count(value) > 0; }

template<class T>
void Queue<T>::dump()
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
