#include<stdio.h>
#include<iostream>

using namespace std;

class GuardPatrol
{
    private:
        int x, y, dir_x, dir_y, n, m;
        char map[150][150];
    public:
        GuardPatrol(int starting_x, int starting_y, int dir_x, int dir_y, int n, int m, char map[150][150])
        {
            this->x = starting_x;
            this->y = starting_y;
            this->dir_x = dir_x;
            this->dir_y = dir_y;
            this->n = n;
            this->m = m;

            for(int i = 0 ; i < n ; i++)
            {
                for(int j = 0 ; j < m ; j++)
                {
                    this->map[i][j] = map[i][j];
                }
            }
        }

        void change_dir()
        {
            if(this->dir_x == -1 && this->dir_y == 0)
            {
                // Pointing up, change to right
                this->dir_x = 0;
                this->dir_y = 1;
            }
            else if (this->dir_x == 0 && this->dir_y == 1)
            {
                // Pointing right, change to down
                this->dir_x = 1;
                this->dir_y = 0;
            }
            else if (this->dir_x == 1 && this->dir_y == 0)
            {
                // Pointing down, change to left
                this->dir_x = 0;
                this->dir_y = -1;
            }
            else
            {
                // Pointing left, change to up
                this->dir_x = -1;
                this->dir_y = 0;
            }
        }

        int find_distinct_positions()
        {
            int ans = 0;
            bool visited[150][150] = {false};
            int x = this->x;
            int y = this->y;

            while(x > 0 && x < this->n && y > 0 && y < this->m)
            {
                if(!visited[x][y])
                {
                    visited[x][y] = true;
                    ans++;
                }

                // While loop rather than if statement in case there was
                // multiple walls
                while(this->map[x + this->dir_x][y + this->dir_y] == '#')
                {
                    this->change_dir();
                }

                x += this->dir_x;
                y += this->dir_y;
            }

            return ans;
        }
};

int main()
{
    FILE *f = fopen("input.txt", "r");
    char c, arr[150][150];
    int i = 0, j = 0, x = -1, y = -1, dir_x = 0, dir_y = 0;
    int n = -1, m = -1;

    while(fgets(arr[i], 150, f) != NULL)
    {
        if(m == -1 || x == -1)
        {
            for(j = 0 ; arr[i][j] != '\0' ; j++)
            {
                if(arr[i][j] != '.' && arr[i][j] != '#' && arr[i][j] != '\n')
                {
                    // This is where the guard starts at
                    x = i;
                    y = j;

                    if(arr[i][j] == '^')
                        dir_x = -1;
                    else if(arr[i][j] == 'v')
                        dir_x = 1;
                    else if(arr[i][j] == '<')
                        dir_y = -1;
                    else if(arr[i][j] == '>')
                        dir_y = 1;
                }
            }
        }

        if(arr[i][j] == '\0' && m == -1)
            m = j;

        i++;
    }

    n = i;

    GuardPatrol solver = GuardPatrol(x, y, dir_x, dir_y, n, m, arr);
    int ans = solver.find_distinct_positions();

    printf("%d", ans);

    return 0;
}