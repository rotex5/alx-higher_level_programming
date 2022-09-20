#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks for cycle in linked list
 * @list: the pointer to first node of linked list
 * Return: 0 if no cycle | 1 if cycle is present
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	if (list == NULL)
		return (0);

	temp2 = temp2->next;

	while (temp1 && temp2 && temp2->next)
	{
		if (temp1 == temp2)
			return (1);

		temp1 = temp1->next;
		temp2 = temp2->next->next;

	}
	return (0);
}
