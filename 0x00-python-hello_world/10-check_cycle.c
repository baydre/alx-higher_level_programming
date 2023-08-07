#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if list is empty
 * @list: creates pointer to head
 * Return: 1 on success and 0 on failure.
 */
int check_cycle(listint_t *list)
{
	listint_t *steady = list, *quick = list;

	if (list == NULL)
		return (0);
	while (steady && quick && quick->next)
	{
		steady = steady->next;
		quick = quick->next->next;
		if (steady == quick)
			return (1);
	}
	return (0);
}
