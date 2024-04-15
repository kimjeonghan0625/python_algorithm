#include <stdio.h>

int main(void)
{
    double x, y;
    printf("좌표 x, y 입력 >> ");
    scanf("%lf%lf", &x, &y);
    int p;
    if (x > 0 && y > 0)
    {
        p = 1;
    }
    else if (x < 0 && y > 0)
    {
        p = 2;
    }
    else if (x < 0 && y < 0)
    {
        p = 3;
    }
    else
    {
        p = 4;
    }
    printf("좌표 (%.2lf, %.2lf): %d사분면\n", x, y, p);
    return 0;
}