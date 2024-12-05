#include<stdio.h>
#include<iostream>

using namespace std;

class XmasSolver
{
    private:
        int n, m;
        char arr[150][150];
        const string MAGIC_WORD = "XMAS";
    public:
        int find_rest(int, int, int, int, int);
        int find_x();

    XmasSolver(int n, int m, char arr[150][150])
    {
        this->n = n;
        this->m = m;

        for(int i = 0; i < n ; i++)
        {
            for(int j = 0; j < m ; j++)
            {
                this->arr[i][j] = arr[i][j];
            }
        }
    }
};

int XmasSolver::find_rest(int i, int j, int dir_x, int dir_y, int curr_letter)
{
    if(curr_letter == this->MAGIC_WORD.size())
        return 1;

    i += dir_x;
    j += dir_y;

    if(i < this->n && i >= 0 && j < this->m && j >= 0)
    {    
        if(this->arr[i][j] == this->MAGIC_WORD[curr_letter])
        {
            return find_rest(i, j, dir_x, dir_y, curr_letter + 1);
        }
    }
    
    return 0;
}

int XmasSolver::find_x()
{
    int ans = 0;
    const int DIR_X[] = {0, 0, 1, 1, 1, -1, -1, -1};
    const int DIR_Y[] = {-1, 1, -1, 0, 1, -1, 0, 1};

    for(int i = 0 ; i < this->n ; i++)
    {
        for(int j = 0 ; j < this->m ; j++)
        {
            if(this->arr[i][j] == 'X')
            {
                for(int d = 0; d < 8; d++)
                {
                    ans += find_rest(i, j, DIR_X[d], DIR_Y[d], 1);
                }
            }
        }
    }

    return ans;
}

int main()
{
    FILE *f = fopen("input.txt", "r");
    char c, arr[150][150];
    int i = 0, j = 0;

    while(fgets(arr[i], 150, f) != NULL)
    {
        i++;
    }

    for(j = 0 ; arr[0][j] != '\0' ; j++)
    {}

    XmasSolver solver = XmasSolver(i, j, arr);
    int ans = solver.find_x();

    printf("%d", ans);

    return 0;
}