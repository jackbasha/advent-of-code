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
        bool find_rest(int, int);
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

bool XmasSolver::find_rest(int i, int j)
{
    if(i == 0 || i == n - 1 || j == 0 || j == m - 1)
        return false;

    const int DIR_X[] = {1, -1, 1, -1};
    const int DIR_Y[] = {-1, 1, 1, -1};
    
    int slashes = 0;
    
    for(int k = 0 ; k < 4 ; k += 2)
    {
        if(arr[i + DIR_X[k]][j + DIR_Y[k]] == 'S' &&
            arr[i + DIR_X[k + 1]][j + DIR_Y[k + 1]] == 'M')
            slashes += 1;
        else if(arr[i + DIR_X[k]][j + DIR_Y[k]] == 'M' &&
            arr[i + DIR_X[k + 1]][j + DIR_Y[k + 1]] == 'S')
            slashes += 1;   
    }
    
    return slashes == 2;
}

int XmasSolver::find_a()
{
    int ans = 0;

    for(int i = 0 ; i < this->n ; i++)
    {
        for(int j = 0 ; j < this->m ; j++)
        {
            if(this->arr[i][j] == 'A')
            {
                if(find_rest(i, j))
                    ans += 1;
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
    int ans = solver.find_a();

    printf("%d", ans);

    return 0;
}