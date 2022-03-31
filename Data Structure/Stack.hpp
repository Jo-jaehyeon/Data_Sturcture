template<class T>
Stack<T>::Stack(int n)
{
	capacity = n;
	ptr = 0;
	stk = new T[capacity];
}

template<class T>
int Stack<T>::__len__() 
{ 
	return ptr; 
}

template<class T>
bool Stack<T>::is_empty() 
{ 
	return ptr <= 0; 
}

template<class T>
bool Stack<T>::is_full()
{ 
	return ptr >= capacity; 
}

template<class T>
void Stack<T>::push(T value)
{
	if (is_full())
		return;

	stk[ptr] = value;
	ptr += 1;
}

template<class T>
T Stack<T>::pop()
{
	if (is_empty())
		return NULL;
	ptr -= 1;
	return stk[ptr];
}

template<class T>
T Stack<T>::peak()
{
	if (is_empty())
		return -1;

	return stk[ptr - 1];
}

template<class T>
void Stack<T>::clear()
{
	ptr = 0;
	return;
}

template<class T>
int Stack<T>::find(T value)
{
	for (int i = ptr - 1; i > 0; i--)
	{
		if (stk[i] == value)
			return i;
	}
	return -1;
}

template<class T>
int Stack<T>::count(T value)
{
	int c = 0;
	for (int i = 0; i < ptr; i++)
	{
		if (stk[i] == value)
			c += 1;
	}
	return c;
}

template<class T>
bool Stack<T>::__contains__(T value)
{
	if (count(value) > 0)
		return true;
	else
		return false;
}

template<class T>
void Stack<T>::dump()
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
