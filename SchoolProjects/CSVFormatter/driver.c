// Main function that takes in data from a CSV and creates a formatted output VSV

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "functions.h"

int main(int argc, char *argv[])
{
    //Make sure the correct number of command line arguments are made
    assert(argc = 3);
    
    //Opening file to read in information from and
    //print out to
    FILE* input = fopen(argv[1], "r");
    FILE* output = fopen(argv[2],"w+");

    //Ensuring both files opened correctly
    assert(input != NULL);
    assert(output != NULL);
    
    //Calculate how many rows are in the file
    int rows = 0;
    for(char c = getc(input); c != EOF; c = getc(input))
    {
        if(c == '\n')
        {
            rows++;
        }
    }
    rewind(input);

    //Allocate a double node pointer the with one node for every row
    node_t** doublePtr = malloc(sizeof(node_t*) * rows);
    
    //Allicate a node pointer the size of one node
    node_t* head = malloc(sizeof(node_t));

    //Call createList setting head as the head node and using the block
    //of memory pointed to by doublePtr to create a list of all the data
    //in the file
    head = createList(input,doublePtr);

    //Print all the data from the file to an output file with 
    //the correct format
    printList(output, head);

    //Free the memory
    deleteList(doublePtr);
    free(head);
        
    return 0;
}
