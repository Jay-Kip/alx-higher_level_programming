#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int s, a, i;
	PyObject *objct;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		objct = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(objct)->tp_name);
	}
}
