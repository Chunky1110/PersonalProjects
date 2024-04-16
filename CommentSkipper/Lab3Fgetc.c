// This file takes in a C file as an input and removes all comments from the file and prints the result using the output
// This is one of two approaches which uses the FGETC function

#include <stdio.h>
#include <stdlib.h>
#include "Lab3Fgetc.h"

void start(FILE* in)
{
        unsigned char c;

        // Read through the file and detect and skipp comments, printing the rest
        while(!(feof(in)))
        {
                c = fgetc(in);
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

// Function to skip to determine if a comment is single or multi-line and call the appropriate skip function
void rcomment(FILE* in)
{

        if(fgetc(in) == '*')
        {
                skipM_comment(in);
        }
        else
        {       
                skipS_comment(in);
        }
}

// Function to skip multi line comments
void skipM_comment(FILE* in)
{
        unsigned char c;
        while(c != '/')
                {
                        c = fgetc(in);
                }
}

// Function to skip single line comments
void skipS_comment(FILE* in)
{
        unsigned char c;
        while(c != '\n')
                {
                        c = fgetc(in);
                }
}
