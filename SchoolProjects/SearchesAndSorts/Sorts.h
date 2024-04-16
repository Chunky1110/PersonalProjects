/*
 * Name: Carson Crockett
 * Date Submitted: 06/03/2022
 * Lab Section: 001 
 * Assignment Name: Searches and Sorts
 */

#pragma once

#include <vector>
#include <stdlib.h>

template <class T>
std::vector<T> mergeSort(std::vector<T> lst)
{        
        std::vector<T> firstHalf, secondHalf, sorted;   
        int x = 0, y = 0;
 
        if(lst.size() <= 1)
        {
                return lst;
        }

        for (int i = 0; i < lst.size() / 2; i++)
        {
                firstHalf.push_back(lst[i]);
        }

        for (int i = lst.size() / 2; i < lst.size(); i++)
        {
                secondHalf.push_back(lst[i]);
        }

        firstHalf = mergeSort(firstHalf);
        secondHalf = mergeSort(secondHalf);

        
        while(x < firstHalf.size() && y < secondHalf.size())
        {
                if (firstHalf[x] <= secondHalf[y])
                {
                        sorted.push_back(firstHalf[x++]);
                }
                else
                {
                        sorted.push_back(secondHalf[y++]);
                }
        }
                
        while(x < firstHalf.size())
        {
                sorted.push_back(firstHalf[x++]);
        }
        while(y < secondHalf.size())
        {
                sorted.push_back(secondHalf[y++]);
        }

        return sorted;
}



template <class T>
std::vector<T> quickSort(std::vector<T> lst){
        
        std::vector<T> vec1, vec2, sorted;

        if(lst.size() <= 1)
        {
                return lst;
        }

        int pivotIndex = rand() % lst.size();

        T temp = lst[0];
        lst[0] = lst[pivotIndex];
        lst[pivotIndex] = temp;
        pivotIndex = 0;

        for(int i = 1; i < lst.size(); i++)
        {
                if(lst[i] < lst[0])
                {
                        pivotIndex++;
                        temp = lst[pivotIndex];
                        lst[pivotIndex] = lst[i];
                        lst[i] = temp;
                }
        }

        temp = lst[pivotIndex];
        lst[pivotIndex] = lst[0];
        lst[0] = temp;

        for(int i = 0; i < pivotIndex; i++)
        {
                vec1.push_back(lst[i]);
        }

        for(int i = pivotIndex + 1; i < lst.size(); i++)
        {
                vec2.push_back(lst[i]);
        }
        
        vec1 = quickSort(vec1);
        vec2 = quickSort(vec2);

        for(int i = 0; i < vec1.size(); i++)
        {
                sorted.push_back(vec1[i]);
        }

        sorted.push_back(lst[pivotIndex]);

        for(int i = 0; i < vec2.size(); i++)
        {
                sorted.push_back(vec2[i]);
        }  

        return sorted;      

}
