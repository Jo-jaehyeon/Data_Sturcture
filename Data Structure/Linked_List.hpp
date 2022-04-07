template<class T>
Linked_List<T>::Linked_List()
{
	head = NULL;
	tail = NULL;
}

template<class T>
Linked_List<T>::~Linked_List()
{
	Node<T>* ptr = head; 

	while (ptr != nullptr)
	{
		head = ptr->next; 
		delete ptr; 
		ptr = head;
	}
	
	delete head; // null ������ ���� 
	size = 0; 
	cout << "����Ʈ�� �����Ǿ����ϴ�" << endl;
}
template<class T>
int Linked_List<T>::__len__() { return size; }

template<class T>
bool Linked_List<T>::is_empty() { return size <= 0; }

template<class T>
void Linked_List<T>::addNode(T value)
{
	Node<T> *temp = new Node<T>;
	temp->data = value;
	temp->next = nullptr;

	if (head == NULL)
	{
		head = temp;
		tail = temp;
	}
	else
	{
		tail->next = temp;
		tail = temp;
	}
	size++;
}

template<class T>
void Linked_List<T>::insertNode(int idx, T value)
{
	Node<T>* node = new Node<T>;
	node->data = value;
	node->next = nullptr;

	Node<T>* ptr = head;
	if (idx > size)
		cout << "������ ��� �ε��� ���Դϴ�." << endl;
	else
	{
		for (int i = 0; i < idx - 1; i++)
			ptr = ptr->next;

		node->next = ptr->next;
		ptr->next = node;
		size++;
	}
}

template<class T>
void Linked_List<T>::removeNode(int idx)
{
	if (idx > size)
		cout << "������ ��� �ε��� ���Դϴ�." << endl;
	else
	{
		Node<T>* target = head;
		Node<T>* pre = target;

		for (int i = 0; i < idx; i++)
		{ 
			pre = target;
			target = target->next;
		}
		cout << "������ " << idx << "��° ����� ��: " << target->data << endl;
		pre->next = target->next;
		size--;

		delete target;
	}
}

template<class T>
void Linked_List<T>::show()
{
	Node<T>* node = head;

	cout << node->data;
	node = node->next;
	
	while (node != nullptr)
	{
		cout << " -> " << node->data;
		node = node->next;	
	}
	cout << endl;
}