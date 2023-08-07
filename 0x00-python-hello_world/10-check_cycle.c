#include <stdio.h>
#include "lists.h"
#include <stdlib.h>


int check_cycle(listint_t *list)
{
	listint_t *now;
	listint_t *see;

	if (list == NULL || list->next == NULL)
		return (1);

	now = list;
	see = now->next;

	while (see != NULL && see->next != NULL && see->next == NULL && see->next->next != NULL)
	{
		if (now == see)
			return (1);
		now = now->next;
		now->next = now->next->next;
	}
	return (0);
}
