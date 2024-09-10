#include "lists.h"

/**
  * check_cycle - Checks if a linked list contains a cycle
  * @listint_t *list - Pointer to a pointer to a node
  *
  * Return: 0 if no cycle, 1 if cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	if (list == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
