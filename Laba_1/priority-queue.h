#pragma once
#include <iostream>
#include <vector>
#include <algorithm>

template <typename T, template <typename V> class Container = std::vector>
class Priority_queue
{
private:
	Container<T> heap;
	void heapify(uint64_t index)
	{
		uint64_t largest = index;
		uint64_t left = 2 * index + 1;
		uint64_t right = 2 * index + 2;

		uint64_t size = _size();

		if (left < size && heap[left] > heap[largest])
			largest = left;
		if (right < size && heap[right] > heap[largest])
			largest = right;

		if (largest != index) {
			std::swap(heap[index], heap[largest]);
			heapify(largest);
		}
	}
public:
	bool is_empty(void)  
	{
		return heap.empty();
	}
	uint64_t _size(void) 
	{
		return heap.size();
	}
	void push(T data) 
	{
		uint64_t size = _size();
		if (size == 0) {
			heap.push_back(data);
		}
		else {
			heap.push_back(data);
			for (int i = size / 2 - 1; i >= 0; i--)
				heapify(i);
		}
	}
	void pop() 
	{
		try {
			if (_size() == 0)
			{
				throw std::out_of_range("Out of range");
			}

			heap[0] = heap.back();
			heap.pop_back();
			heapify(0);
		}
		catch (const std::out_of_range& e) {
			std::cout << std::endl << e.what();
		}
	}
	T max_elem(void) 
	{
		if (is_empty())
		{
			return NULL;
		}
		else
		{
			return heap[0];
		}
	}
	void print(void) {
		uint64_t size = _size();
		for (size_t i = 0; i < size; i++) {
			std::cout << max_elem() << " ";
			pop();
		}
		std::cout << std::endl;
	}
};