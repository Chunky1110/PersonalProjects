#pragma once

#include <vector>

template <class T>
int linearSearch(std::vector<T> data, T target){
        for(int i  = 0; i < data.size(); i++)
        {
                if(data[i] == target)
                {
                        return i;
                }
        }
        return -1;
}


template <class T>
int binarySearch(std::vector<T> data, T target){
        
        int low = 0;
        int high = data.size() - 1;
        int mid = (low + high) / 2;

        while(data[mid] != target && low <= high)
        {
                if(data[mid] < target)
                {
                        low = mid + 1;
                }
                
                else
                {
                        high = mid - 1;
                }

                mid = (low + high) / 2;
        }

        if(data[mid] == target)
        {
                return mid;
        }
        else
                return -1;
}
