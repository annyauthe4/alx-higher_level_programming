#include "lists.h"

/**
  * reverse_listint - Reverses a singly linked list
  * @head: Pointer to the pointer to the first node
  *
  * Return: Pointer to the first node of the reversed list
  */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next, *current;

	*prev = NULL;
	*next = NULL;
	*current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: Double pointer to the head of the list
  *
  * Return: 1 if palindrome, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first_half, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	*slow = *head, *fast = *head, *first_half = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	second_half = reverse_listint(&slow);
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_listint(&slow);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_listint(&slow);
	return (1);
}
