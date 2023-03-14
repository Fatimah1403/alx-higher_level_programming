#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
* print_python_list_info - prints some basic info about pytohn lists
* @p: python object to be printed
* Return: Nothing
**/

void print_python_list_info(PyObject *p)
{
	int i, size, alloc;
	pyobject *item;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated  = %d\n", alloc);

	for (i = 0; i < size; ++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(p, i)
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
