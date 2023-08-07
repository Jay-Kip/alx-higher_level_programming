#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - function to check if there is a cycle in a list
 * @list: list to be checked
 * Return: 1 if present 0 if absent
 */

int check_cycle(listint_t *list)
{
	listint_t *now;
	listint_t *see;

	if (list == NULL || list->next == NULL)
		return (0);

	now = list;
	see = now->next;

	while (now != NULL && see->next != NULL && see->next->next != NULL)
	{
		if (now == see)
			return (1);
		now = now->next;
		see = see->next->next;
	}
	return (0);
}
