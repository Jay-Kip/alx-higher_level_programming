#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - function to reverse the list
 * @head: pointer to the list
 * Return: pointer to the list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *nxt, *pre = NULL;

	while (node)
	{
		nxt = node->next;
		node->next = pre;
		pre = node;
		node = nxt;
	}
	*head = pre;

	return (*head);
}
/**
 * is_palindrome - Function to check if a linked list is a palindrome
 * @head: pointer to the list
 * Return: 1 or o
 */

int is_palindrome(listint_t **head)
{
	listint_t *temporary;
	listint_t *reverse;
	listint_t *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temporary = *head;
	while (temporary)
	{
		size++;
		temporary = temporary->next;
	}

	temporary = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		temporary = temporary->next;
	}

	if ((size % 2 == 0 && temporary->n != temporary->next->n))
			return (0);

	temporary = temporary->next->next;
	reverse = reverse_listint(&temporary);
	middle = reverse;

	temporary = *head;
	while (reverse)
	{
		if (temporary->n != reverse->n)
			return (0);
		temporary = temporary->next;
		reverse = reverse->next;
	}
	reverse_listint(&middle);

	return (1);
}
