#ifndef LISTS_H
#define LISTS_H

/**
 * struct list_k - the single linked list
 * @n: Integer n
 * @next: pointer to the next node
 */

typedef struct list_k
{
	int n;
	struct list_k *next;
} list_k;
size_t print_listint(const listint_t *h);

#endif
