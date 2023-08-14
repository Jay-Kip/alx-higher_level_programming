#include <python.h>


void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = Py_SIZE(p);
	/*alloc = ((PyListObject *)p)->allocated;*/

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %zd: ", i);

		obj = PyList_Getltm(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
