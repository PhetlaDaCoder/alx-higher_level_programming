#include "lists.h"
#include <stdlib.h>

/**
 * cycle_check - A function that checks if a singly-linked list has a cycle.
 * @list: Pointer to singly-linked list.
 *
 * Return: 1 if success or 0 in failed.
 */

int cycle_check(listint_t *list)
{
	listint_t *slow, *quick;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	quick = list->next->next;

	while (slow && quick && quick->next)
	{
		if (slow == quick)
			return (1);

		slow = slow->next;
		quick = quick->next->next;
	}

	return (0);
}
