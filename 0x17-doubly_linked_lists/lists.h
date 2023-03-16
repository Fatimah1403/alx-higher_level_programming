#ifndef LISTS_H
#define LISTS_H

 #include <stdio.h>
 /**
  * struct dlistint_s - doubly linked list
  * @n: integer
  * @prev: points to the previous node
  * @next: points to the next node
  *
 11  * Description: doubly linked list node structure
 12  *
 13  */
 14 typedef struct dlistint_s
 15 {
 16     int n;
 17     struct dlistint_s *prev;
 18     struct dlistint_s *next;
 19 } dlistint_t;
 20
 21
 22 #endif

