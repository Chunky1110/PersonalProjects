#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#ifndef FUNCTIONS_H_
#define FUNCTIONS_H_

typedef struct Header {
    char        magicNumber[5]; 
    double      width;
    double      height;
    double      maxSize;
}header_t;

typedef struct Pixel {
    unsigned char   b;
    unsigned char   r;
    unsigned char   g;
}pixel_t;

header_t readHeader(FILE*);

void writeHeader(FILE*, header_t);

void removeComments(FILE*);

pixel_t** allocateMemory(double, double);

void readPixels(pixel_t**, header_t, FILE*);

void createImage(FILE*, pixel_t**, header_t);

void freeMemory(pixel_t**);

void resizePPM(pixel_t**, header_t, double, double, FILE*);

void negativePPM(pixel_t**, header_t, FILE*);

#endif