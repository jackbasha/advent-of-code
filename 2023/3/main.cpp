#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    FILE *f = fopen("input.txt", "r");
    char c = fgetc(f);

    int itr_max = 150;
    char arr[150][150];
    bool truth_arr[150][150];

    for(int i = 0 ; i < itr_max ; i++)
    {
        for(int i = 0 ; i < itr_max ; i++)
        {
            truth_arr[i][j] = false;
        }
    }

    while(c != EOF)
    {

    }

	return 0;
}