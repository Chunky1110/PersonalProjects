// Functions used by driver.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "functions.h"

node_t* createList(FILE* input, node_t** nodePtr)
{
    //Allocate a node pointer to be the head of the linked list
    node_t* head = malloc(sizeof(node_t));
    
    //count the number of rows in the file and 
    //return the file pointer to the start
    int rows = 0;
    for(char c = getc(input); c != EOF; c = getc(input))
    {
        if(c == '\n')
        {
            rows++;
        }
    }
    rewind(input);

    //Go through each row of the file and store the node in the linked list
    //Sets each pointer in an allocated block of double pointers to a node
    //containing the data from the file
    for(int i = 0; i < rows; i++)
    {
        nodePtr[i]  = readNodeInfo(input);
    }
    
    //Set next node pointer for every node except the last
    for(int i = 0; i < rows - 1; i++)   
    {
        nodePtr[i]->next_node = nodePtr[i+1];
    }
    
    //Sets the head node to the first node in the block
    head = *nodePtr;
    return head;
}

void add(node_t** node, node_t** head)
{
    //Allocate memory for two different nodes
    node_t* tempNode = malloc(sizeof(node_t));
    node_t* curNode = malloc(sizeof(node_t));
    
    //If the list is empty, assign the given node to the head
    if(head == NULL)
    {
        head = node;
    }
    
    //Assign current node to the head
    //Assign the temporary node to the node after head
    curNode = (*head);
    tempNode = (*head)->next_node;
    
    //Point head to the new node
    head = node;
    
    //Set the next node for head to current node
    //Sets the node after head to what head previously was
    (*head)->next_node = curNode;
    
    //while current node is not at the end of the list
    //The node after the current node to the node pointed to by temp node
    //set the temp node to the node after the next node of the current node
    //set the current node to the one after it
    while(curNode != NULL)
    {
        curNode->next_node = tempNode;
        tempNode = curNode->next_node->next_node;
        curNode = curNode->next_node;
    }
    
    //release memory for curNode and tempNode
    free(tempNode);
    free(curNode);
}

node_t* readNodeInfo(FILE* input)
{
    //Allocates a single node pointer
    node_t* node = malloc(sizeof(node_t));
    
    //Reads in the data from one row of the file and stores it in node
    fscanf(input,"%[^,]%*c",(*node).lName);
    fscanf(input,"%[^,]%*c",(*node).fName);
    fscanf(input,"%[^,]%*c",(*node).birthday.m);
    fscanf(input,"%[^,]%*c",(*node).birthday.d);
    fscanf(input,"%[^,]%*c",(*node).birthday.y);
    fscanf(input,"%[^,]%*c",(*node).favSong);
    fscanf(input,"%[^,]%*c",(*node).passTime);
    fscanf(input,"%[^\n]%*c",(*node).whyCS);
    
    return node;
    
}

void printList(FILE* output, node_t* head)
{
        //Print 80 *
        //Print List Info header
        printBorder(output);
        fprintf(output,"\nList Info: \n");
        
        //Print statement if input file is empty
        if(head == NULL)
        {
            printf("Input file has no data, exiting\n");
            exit(0);
        }
        
        //While we are not at the end of the list
        //Print the data of the node in the desired format
        while(head != NULL)
        {            
            fprintf(output,"Name: %s %s\n", (*head).fName, (*head).lName);
            fprintf(output,"Date of Birth: ");
            //If statements to convert numeric months to written names
            if(strcmp("1",(*head).birthday.m) == 0)
                fprintf(output,"January ");
            if(strcmp("2",(*head).birthday.m) == 0)
                fprintf(output,"February ");
            if(strcmp("3",(*head).birthday.m) == 0)
                fprintf(output,"March ");
            if(strcmp("4",(*head).birthday.m) == 0)
                fprintf(output,"April ");
            if(strcmp("5",(*head).birthday.m) == 0)
                fprintf(output,"May ");
            if(strcmp("6",(*head).birthday.m) == 0)
                fprintf(output,"June ");
            if(strcmp("7",(*head).birthday.m) == 0)
                fprintf(output,"July ");
            if(strcmp("8",(*head).birthday.m) == 0)
                fprintf(output,"August ");
            if(strcmp("9",(*head).birthday.m) == 0)
                fprintf(output,"September ");
            if(strcmp("10",(*head).birthday.m) == 0)
                fprintf(output,"October ");
            if(strcmp("11",(*head).birthday.m) == 0)
                fprintf(output,"November ");
            if(strcmp("12",(*head).birthday.m) == 0)
                fprintf(output,"December ");
            fprintf(output,"%s, %s\n", (*head).birthday.d, (*head).birthday.y);
            fprintf(output,"Favorite Song: %s\n", (*head).favSong);
            fprintf(output,"Favorite Pastime: %s\n", (*head).passTime);
            fprintf(output,"Why I Chose CS: %s\n", (*head).whyCS);
            head = head->next_node;
        }
        printBorder(output);
}

void printBorder(FILE* output)
{
    for (int i = 0; i < 80; i++)
    {    
        fprintf(output,"*");
    }
}

void deleteList(node_t** list)
{
    free(list);
}
