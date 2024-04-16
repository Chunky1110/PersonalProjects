#include "functions.h"

/** Parameters: 
 *  input - FILE pointer to the file where we will be reading
 *  header data from
 *  Return:     header_t - an instnace of the Header stuct containing the 
 *              header from the input file
 *  This function reads in the header of a PPM file from a given FILE
 *  pointer and returns it as an instance of the Header struct
 */
header_t readHeader(FILE* input) {
    
    header_t header;
    
    fscanf(input, "%s", header.magicNumber);
    removeComments(input);

    fscanf(input, "%le", &header.width);
    removeComments(input);

    fscanf(input, "%le", &header.height);
    removeComments(input);

    fscanf(input, "%le", &header.maxSize);

    return header;
}
/** Parameters: 
 *  output - FILE pointer to the file where the output will be written
 *  header - An instnace of the Header struct containing the header data to
 *  be written to the output file
 *  This function writes the data from an instance of Header to a given output
 *  PPM file
 */
void writeHeader(FILE* output, header_t header) {
    fprintf(output, "%s\n%.0lf\n%.0lf\n%.0lf\n", header.magicNumber, 
        header.width, header.height, header.maxSize);
}

/** Parameters: 
 *  input - FILE pointer to the file we are removing comments from
 *  This functions starts at a point in a FILE and reads all comments between
 *  the current point and the next non-comment
 */
void removeComments(FILE* input) {
    char c = fgetc(input);
    
    //If the next char is a # eat the comment
    //If the next char is a newline or space check the next character again
    //If it is a # eat the comment, otherwise move the pointer backwards 
    //one char
    while(c == '#' || c == '\n' || c == ' ')
    {
        if(c == '\n' || c == ' ')
        {
            c = fgetc(input);
        }
        if(c == '#') {
            while(c != '\n')
            {
                c = fgetc(input);
            }
        }
        else
            fseek(input,-1,SEEK_CUR);
    }
}

/**
 * Parameters:  
 * width - a double to store the width of the image being allocated
 * height - a double to store the height of the image being allocated
 * Return: 
 * pixel_t** - double pixel_t pointer pointing to the allocated memory 
 * of width * height number of pixels
 * This function allocates enough memory for the pixel data of a PPM image
 * with a given width and height
 */
pixel_t** allocateMemory(double width, double height) {
    pixel_t** ptr =  malloc(sizeof(pixel_t*) * height);
    for(int i = 0; i < height; i++)
    {
        ptr[i] = malloc(sizeof(pixel_t) * width);
    }
    return ptr;
}

/**
 * Parameters:
 * data - a double pixel_t pointer that points to an empty block of memory
 * that will be used to store the pixel data from the input file
 * head - a header_t object containing the header data from the input file
 * input - a FILE pointer that points to the file containing the pixel data
 * This function reads in the pixel data from a given FILE and stores it in
 * a block of memory that has already been allocated to the proper size for the
 * image
 */
void readPixels(pixel_t** data, header_t head, FILE* input) {
    for(int r = 0; r < head.height; r++)
    {
        for(int c = 0; c < head.width; c++)
        {
            fread(&data[r][c],sizeof(pixel_t), 1, input);
        }   
    }
}

/**
 * Parameters:
 * output - a FILE pointer that points to the FILE where the new image should
 * be stored
 * data - a double pixel_t pointer that points to the pixel data to be written
 * to the new image
 * head - a header_t object containing the header data to be written in the new
 * image
 * This function takes in the header and pixel data of a PPM image and writes
 * it to a given FILE
 */
void createImage(FILE* output, pixel_t** data, header_t head){
    
    writeHeader(output,head);
    for(int r = 0; r < head.height; r++)
    {
        for(int c = 0; c < head.width; c++)
        {
            fwrite(&data[r][c],sizeof(pixel_t), 1, output);
        }   
    }
}

/**
 * Parameters: 
 * ptr - a double pixel_t pointer that points to a block of memory to be freed
 * This function frees a block of data allocated for the pixel data of a PPM
 */
void freeMemory(pixel_t** ptr){
    free(ptr);
}

/**
 * Parameters:
 * original - a double pixel_t pointer that points to the pixel data of a PPM
 * image to be transformed
 * head - a header_t object containing the header data of the image to be 
 * transformed
 * newHeight - a double containing the specified height of the new image
 * newWidth - a double containing the specified width of the new image
 * output - a FILE pointer that points to the file where the new image's
 * data should be written
 * This function takes in the header and pixel data of a PPM and using
 * a desired new width and height transforms the image so that it is resized
 * to that new resolution and stores it in a new PPM file
 */
void resizePPM(pixel_t** original, header_t head, double newHeight, double newWidth, FILE* output) {
    //newHeight is the # of rows
    //newWidth  is the # of cols
    
    int r,c;

    double relativeWidth = head.width / newWidth;
    double realtiveHeight = head.height / newHeight;
    
    double relativeRow, relativeColumn;

    pixel_t** newData = allocateMemory(newWidth, newHeight);

    for(r = 0; r < newHeight; r++)
    {
        for(c = 0; c < newWidth; c++)
        {   
            relativeRow = r * realtiveHeight;
            relativeColumn = c * relativeWidth;

            newData[r][c] = original[(int)relativeRow][(int)relativeColumn];
        }
    }
    
    header_t newHead;
    strcpy(newHead.magicNumber, head.magicNumber);
    newHead.width = newWidth;
    newHead.height = newHeight;
    newHead.maxSize = head.maxSize;

    createImage(output, newData, newHead);
    freeMemory(newData);
    
}

/**
 * Parameters:
 * original - a double pixel_t pointer that points to the pixel data of a PPM
 * image to be transformed
 * head - a header_t object containing the header data of the image to be 
 * transformed 
 * output - a FILE pointer that points to the file where the new image's
 * data should be written
 * This function takes in the pixel and header data of a PPM file and
 * transforms the pixel data into a negative of the original image and stores
 * the new negative data in a new PPM image
 */
void negativePPM(pixel_t** original, header_t head, FILE* output){
    
    pixel_t** newData = allocateMemory(head.width, head.height);
    assert(sizeof(newData) == sizeof(original));

    for(int r = 0; r < head.height; r++)
    {
        for(int c = 0; c < head.width; c++)
        {   
            newData[r][c].r = (head.maxSize - (original[r][c].r));
            newData[r][c].g = (head.maxSize - (original[r][c].g));
            newData[r][c].b = (head.maxSize - (original[r][c].b));

            //printf("<%d,%d> Old: %u %u %u New: %u %u %u\n", r, c, original[r][c].r, original[r][c].g, original[r][c].b, newData[r][c].r, newData[r][c].g, newData[r][c].b);
        }
    }

    createImage(output, newData, head);
    freeMemory(newData);
}