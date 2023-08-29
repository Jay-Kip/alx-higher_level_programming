#include <Python.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, item_type);
	}
}


void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
			{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_ size = PyBytes_Size(p);
	char *bytes = PyBytes_AsString(p);
	py_ssize_t i;

	printf("[.] bytes object info\n");
	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", bytes);

	if (size > 10)
		size = 10;

	printf(" first %zd bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)bytes[i]);
		if (i != size - 1)
			printf(" ");
	}
	print("\n");
}



void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
