#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function to insert a node
 * @head: node
 * @number: number to be inserted
 * Return: inserted number
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (NULL);
	}

	current = *head;

	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
