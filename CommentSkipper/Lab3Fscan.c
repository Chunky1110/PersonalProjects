// This file takes in a C file as an input and removes all comments from the file and prints the result using the output
// This is one of two approaches which uses the FSCAN function

#include <stdio.h>
#include <stdlib.h>
#include "Lab3Fscan.h"


// Function to read through the file while skipping comments
void start(FILE* in)
{
        char c;

        // While we are not at the EOF
        while(!(feof(in)))
        {
                // Detect comments and call function to skip them
                fscanf(in, "%c", &c);
                if(c == '/')
                {                        
                        rcomment(in);
                }
                else
                {
                        printf("%c", c);  
                }  
        }  
}

// Determine the type of comment and call apropriate function
void rcomment(FILE* in)
{
        char ch = ' ';
        fscanf(in, "%c", &ch);
        if(ch == '*')
        {       
                skipM_comment(in);               
        }
        if(ch == '/')
        {       
                skipS_comment(in);
        }
}

// Function to skip multi line comments
void skipM_comment(FILE* in)
{
        char ch = ' ';
        while(ch != '*')
        {
                fscanf(in, "%c", &ch);
        }
}

// Function to skip single line comments
void skipS_comment(FILE* in)
{
        char ch = ' ';
        while(ch != '\n')
        {
                fscanf(in, "%c", &ch);
        }
}
