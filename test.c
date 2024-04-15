#include <stdio.h>
#define PI 3.14
#define radius 8.32

int main(void)
{
    printf("구의 체적은 %.3lf입니다.",4.0/3.0*PI*radius*radius*radius);
    printf("구의 표면적은 %.3lf입니다.", 4.0*PI*radius);
    return 0;
}