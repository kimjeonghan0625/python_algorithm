#include <stdio.h>

int main(void)
{
    int n;
    printf("일자 입력 >> ");
    scanf("%d", &n);
    printf("입력한 날짜: %d\n", n);
    int y = n / 365;
    n = n - 365 * y;
    int m = n / 30;
    n = n - 30 * m;
    int d = n;
    printf("%d년 %d월 %d일\n", y, m, d);
    return 0;
}