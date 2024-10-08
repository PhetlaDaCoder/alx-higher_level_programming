#include "lists.h"

/**
 * insert_node - a function that inserts number into sorted singly-linked list.
 * @head: Pointer to head of linked list.
 * @number: Pointer to number to insert.
 *
 * Return: NULL if fail or pointer to node is succes.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
