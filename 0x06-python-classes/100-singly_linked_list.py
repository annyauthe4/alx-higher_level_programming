#!/usr/bin/python3
"""
This module defines a Node class and
a SinglyLinkedList class for managing
nodes in a singly linked list,
with methods for sorted insertion.
"""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node with
        data and an optional next node.

        Args:
            data (int): The data value of the node.
            next_node (Node or None): The next node
            in the linked list.

        Raises:
            TypeError: If data is not an integer or
        next_node is not None or a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node, ensuring it is an integer.

        Args:
            value (int): The data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, ensuring it is
        either None or a Node instance.

        Args:
            value (Node or None): The next node in the linked list.

        Raises:
            TypeError: If value is not None
        and not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize the head of the
        linked list as None.
        """
        self.__head = None

    def __str__(self):
        """Define how the linked list is
        printed (one node data per line).
        """
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the list
        in the correct sorted position.

        Args:
            value (int): The value to insert into the linked list.
        """
        new_node = Node(value)

        # If the list is empty or the new node,insert @d head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            # Traverse to find the correct position to insert
            while (current.next_node is not None
                   and current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
