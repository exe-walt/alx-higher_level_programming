#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle 
 * Return: 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *duck = list;
	listint_t *goose = list;

	if (!list)
		return (0);

	while (duck && goose && goose->next)
	{
		duck = duck->next;
		goose = fast->next->next;
		if (duck == fast)
			return (1);
	}

	return (0);
}
