#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * print_listint - prints all elements of a listint_t list
  * @h: pointer to head of list
  * Return: number of nodes
  */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
  * add_nodeint_end - adds a new node at the end of a listint_t list
  * @head: pointer to pointer of first node of listint_t list
  * @n: integer to be included in new node
  * Return: address of the new element or NULL if it fails
  */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	return (new);
}

/**
  * free_listint - frees a listint_t list
  * @head: pointer to list to be freed
  * Return: void
  */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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
