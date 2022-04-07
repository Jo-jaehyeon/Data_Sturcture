template<class T>
Arrays<T>::Arrays(int n) 
{
	capacity = n;
	arr = new T[capacity];
	size = 0;
}

template<class T>
Arrays<T>::~Arrays() { delete[] arr; }

template<class T>
int Arrays<T>::__len__() { return size; }

template<class T>
bool Arrays<T>::is_full() { return size >= capacity; }

template<class T>
bool Arrays<T>::is_empty() { return size <= 0; }

template<class T>
void Arrays<T>::insert(int idx, T value)
{
	if (is_full())
		return;

	for (int i = idx; i < capacity - 1; i++)
		arr[i + 1] = arr[i];

	arr[idx] = value;
	size++;
}

template<class T>
void Arrays<T>::replace(int idx, T value)
{
	if (is_empty())
		return;

	arr[idx] = value;
}

template<class T>
void Arrays<T>::remove(int idx)
{
	if (is_empty())
		return;

	for (int i = idx; i < capacity - 1; i++)
		arr[i] = arr[i + 1];
	size--;
}

template<class T>
T Arrays<T>::at(int idx)
{
	if (is_empty())
		return NULL;
	else
		return arr[idx];
}

template<class T>
void Arrays<T>::show()
{
	if (is_empty())
		cout << "Array가 비어있습니다.";
	else
	{
		for (int i = 0; i < size; i++)
			cout << arr[i] << " ";
		cout << endl;
	}
}