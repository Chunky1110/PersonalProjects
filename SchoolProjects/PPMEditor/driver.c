// Function to manipulate a .ppm file
// Creats a negative of the .ppm and resized .ppm
// Function also removes comments hidden in the original ppm

#include "functions.h"

int main (int argc, char** argv) {
    //Double variables to store user's selected 
    //transformations to width and height
    double widthChoice, heightChoice;
    
    //Double variables to store the calculated
    //new width and height of the PPM
    double newWidth, newHeight;
    
    //Ensure the right number of command line arguments are made
    assert(argc == 2);
    
    //Make an instance of the header struct
    header_t head;
    
    //Open input file to be transformed
    FILE* input = fopen(argv[1], "rb");
    assert(input != NULL);
    
    //Open an output file for the resized image
    FILE* outputSize = fopen("resized.ppm", "wb");
    assert(outputSize != NULL);
    
    //Open an output file for the negative image
    FILE* outputNegative = fopen("negative.ppm", "wb");
    assert(outputNegative != NULL);

    //Store the header data from the input into a header struct
    head = readHeader(input);
    
    //Allocate a 2D array with the pixel data from the input image
    pixel_t** originalData = allocateMemory(head.width, head.height);
    fseek(input,1,SEEK_CUR);

    readPixels(originalData,head,input);

    //Take in and verify user input for the new width of the resized image
    printf("What change would you like to make to the Width?\n");
    scanf("%lf", &widthChoice);
    while(widthChoice + head.width <= 0)
    {
        printf("Invalid Transformation\n");
        printf("What change would you like to make to the Width?\n");
        scanf("%lf", &widthChoice);
    }
    //Calculate what the new width will be
    newWidth = widthChoice + head.width;
    
    //Take in and verify user input for the new height of the resized image
    printf("What change would you like to make to the Height?\n");
    scanf("%lf", &heightChoice);
    while(heightChoice + head.height <= 0)
    {
        printf("Invalid Transformation\n");
        printf("What change would you like to make to the Height?\n");
        scanf("%lf", &heightChoice);
    }
    //Calculate what the new height will be
    newHeight = heightChoice + head.height;
    
    //Call transformation functions to create the two transformed images
    resizePPM(originalData, head, newHeight, newWidth, outputSize);
    negativePPM(originalData,head,outputNegative);

    //Free the original 2D array
    freeMemory(originalData);

    return 0;
}