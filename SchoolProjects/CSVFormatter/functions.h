/**************************
 * Carson Crockett
 * CPSC 2310 Fall '22
 * UserName: Cdcrock
 * Instructor: Dr. Yvon Feaster
 *************************/

#ifndef FUNCTION_H_
#define FUNCTION_H_

#include <stdio.h>
struct Birthday
{
    char    m[3], d[3], y[5];
};

typedef struct Node
{
    char            fName[20];
    char            lName[20];
    char            favSong[100];
    char            passTime[100];
    char            whyCS[500];
    struct Birthday birthday;
    struct Node     *next_node;  
}node_t;

/*Parameters:   FILE* - file pointer to where the information 
                stored in the list will come from
*               node_t** - 
*Return:        Returns a node pointer that points to the head of the list
*This function creates a linked list given a file to read 
*data from and returns a pointer to the head of that list
*/
node_t* createList(FILE*, node_t**);

/*Parameters:   node_t** node - a double pointer to the node to be added 
                to the list
*               node_t** head - double pointer to the head of the linked 
                list to be edited
*Return:        Has no return value
*This function adds a given node to a list
*/
void add(node_t** node, node_t** head);

/*Parameters:   FILE* input - the file containing the 
*               information for the list
*
*Return:        Returns a pointer to the head of the linked list c
*               ontaining the information
*This function is meant to be used in createList to create a linked 
*list by reading in data from a given file pointer using scanset
*/
node_t* readNodeInfo(FILE* input);

/*Parameters:   FILE* - A file pointer to a file where the output
*               will be printed
*               node_t* - A node pointer pointing to the list to
*               be printed
*Return:        Has no return value
*This function prints out all the information of a given list to
*a given file. If the list is empty a message will be printed to
*stderr
*/
void printList(FILE*, node_t*);

/**Parameters:  FILE* - A file pointer to the output file where
 *              the border will be printed
 * Return:      Has no return value
 * This function prints 80 asterisks to an output file
 */
void printBorder(FILE*);

/**Parameters:  node_t** - A block of memory pointing to the linked list
 * 
 * Return:      Has no return type
 * This functions frees any memory that was allocated for the linked list
 */
void deleteList(node_t**);

#endif