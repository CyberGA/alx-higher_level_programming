#include "lists.h"

/**
 * check_cycle - check for circular linked list
 * @list: address of the head node
 * Return: 0 if no circle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *temp;

	if (list == NULL)
		return (0);

	head = list;
	temp = list->next;

	while (head && temp)
	{
		if (head == temp)
			return (1);
		temp = temp->next;
	}
	return (0);
}
