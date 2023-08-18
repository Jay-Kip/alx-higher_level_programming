#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	char *str;
	long int sze, i, l;

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

	if (sze >= 10)
		l = 10;
	else
		l = sze + 1;


	printf("  first %ld bytes:", l);

	for (i = 0; i < l; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	
	}
	printf("\n");
}


void print_python_list(PyObject *p)
{
	long int sze, i;
	PyListObject *lst;
	PyObject *o;

	sze = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sze);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < sze; i++)
	{
		o = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
	}
}
