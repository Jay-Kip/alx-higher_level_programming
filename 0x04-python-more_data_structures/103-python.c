#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	char *str;
	long int sze, i l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sze = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sze);
	printf("  trying string: %s\n", str);

	if (sze > = 10)
		l = 10;
	else
		l = sze + 1;


	printf("  first %ld bytes:", limit);

	for (i = 0; i < l; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
	
	}
	printf("\n")
}


void print_python_list(PyObject *p)
{
	long int sze, i;
	PyLitObject *lst;
	PyObject *o;

	sze = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < sze; i++)
	{
		o = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
