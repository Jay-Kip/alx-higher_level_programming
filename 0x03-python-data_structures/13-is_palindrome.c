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
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;

	return (*head);
}
/**
 * is_palindrome - Function to check if a linked list is a palindrome
 * @head: pointer to the list
 * Return: 1 or o
 */

int is_palindrome(listint_t **head)
{
	listint_t *temporary, *reverse, *middle;
	size_t size = 0, i;

	temporary = *head;
	while (temporary)
	{
		size++;
		temporary = temporary->next;
	}

	temporary = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		return (0);
	}

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
