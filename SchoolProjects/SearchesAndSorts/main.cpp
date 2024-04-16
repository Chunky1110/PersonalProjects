// This function takes a vector of strings and can apply a set of searches and sorts on them
// The options are described in the searchs and sorts .h files

#include "Searches.h"
#include "Sorts.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
        vector<string> stringTest {"earthlings","greetings","leader","me","take","to","yall","your"};
        vector<string> stringTest2 {"greetings", "yall", "earthlings", "take", "me", "to", "your", "leader"};
        vector<string> a = mergeSort(stringTest2);
        
        for(int i = 0; i < a.size(); i++)
                cout << a[i] << " ";

        
        return 0;
}