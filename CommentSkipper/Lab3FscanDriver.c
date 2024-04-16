// Main function for Lab3Fscan.c
// Assers the correct number of CLAs
// Takes in desired c file as input ("input.c")

#include <stdio.h>
#include <stdlib.h>
#include <cassert>
#include "Lab3Fscan.h"

int main(int argc, char* argv[])
{
        assert(argc == 2);
        FILE* input = fopen(argv[1], "r");
        assert(input != NULL);

        start(input);
}