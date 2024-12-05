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
        int find_a();

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

int XmasSolver::find_a()
{
    int ans = 0, slashes = 0;
    const int DIR_X[] = {1, -1, 1, -1};
    const int DIR_Y[] = {-1, 1, 1, -1};

    for(int i = 0 ; i < this->n ; i++)
    {
        for(int j = 0 ; j < this->m ; j++)
        {
            if(this->arr[i][j] == 'A')
            {
                if(i >= 1 && i < n - 1 && j > 1 && j < m - 1)
                {
                    slashes = 0;

                    for(int k = 0 ; k < 4 ; k += 2)
                    {
                        if(arr[i + DIR_X[k]][j + DIR_Y[k]] == 'S' &&
                            arr[i + DIR_X[k + 1]][j + DIR_Y[k + 1]] == 'M')
                            slashes += 1;
                        else if(arr[i + DIR_X[k]][j + DIR_Y[k]] == 'M' &&
                            arr[i + DIR_X[k + 1]][j + DIR_Y[k + 1]] == 'S')
                            slashes += 1;
                        
                    }

                    if(slashes == 2)
                        ans += 1;
                }
            }
        }
    }

    return ans;
}

int main()
{
    FILE *f = fopen("small_input.txt", "r");
    char c, arr[150][150];
    int i = 0, j = 0;

    while(fgets(arr[i], 150, f) != NULL)
    {
        i++;
    }

    for(j = 0 ; arr[0][j] != '\0' ; j++)
    {}

    XmasSolver solver = XmasSolver(i, j, arr);
    int ans = solver.find_a();

    printf("%d", ans);

    return 0;
}