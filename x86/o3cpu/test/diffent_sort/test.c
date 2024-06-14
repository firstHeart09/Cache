#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void test_1();
int test_2();
int test_3();
int test_4();
int test_5();

int main()
{
    test_1();
    test_2();
    test_3();
    test_4();
    test_5();
    test_3();
    return 0;
}

// 编程1：有1,2,3,4个数字，能组成多少个互不相同的无重复数字的三位数？都是多少？
void test_1()
{
    int i, j, k;
    printf("\n");
    for (i = 1; i < 5; i++)
    {
        for (j = 1; j < 5; j++)
        {
            for (k = 1; k < 5; k++)
            {
                if (i != k && i != j && k != j)
                    printf("%d%d%d\n", i, j, k);
            }
        }
    }
    test_2();
}

// 有一对兔子，从出生第三个月之后，每个月生一对兔子，小兔子长到第三个月又生一对兔子，假如兔子不死，求每个月兔子的数量是多少？一年之后是多少？
int test_2()
{
    long f1, f2;
    int i;
    f1 = f2 = 1;
    for (i = 1; i <= 12; i++)
    {
        printf("%12ld %12ld", f1, f2);
        if (i % 2 == 0)
            printf("\n");
        f1 = f1 + f2;
        f2 = f1 + f2;
    }
    return 0;
}

// 打印100-1000内的水仙花数
int test_3()
{
    int i, j, k, n;
    for (n = 100; n < 1000; n++)
    {
        i = n / 100;
        j = n / 10 % 10;
        k = n % 10;
        if (i * 100 + j * 10 + k == i * i * i + j * j * j + k * k * k)
            printf("%-5d", n);
    }
    return 0;
}

// 一球从100米高度自由落下，每次落地反弹后跳回原来高度的一半，再落下，求十次落地后，共经过多少米？第10次多高？
int test_4()
{
    float s = 100.0, h = 50;
    int i, cnt = 1;
    for (i = 2; i <= 10; i++)
    {
        s = s + h * 2; // 第一次下落s=100米 反弹高度=下落高度  =2*h
        h /= 2;        // 减半
        cnt++;
        printf("第%d次   %f米\n", cnt, s);
    }
    printf("共经过%f米\n", s);
    printf("第10次高度是%f米\n", h);
    return 0;
}

// 猴子吃桃问题：猴子第一天摘了若干个桃子，当即吃了一半，不过瘾，又吃了一个，第二天早上又将剩下的桃子吃了一半，又多吃了一个。以后每天都吃了前一天的一半多一个，到第10天只剩一个桃子。求第一天吃了多少？
int test_5()
{
    int day, x1 = 0, x2;
    day = 9;
    x2 = 1;
    test_1();
    while (day > 0)
    {
        x1 = (x2 + 1) * 2; // 第一天的桃子数是第2天桃子数加1后的2倍
        x2 = x1;
        day--;
    }
    printf("总数为 %d\n", x1);
    test_3();
    return 0;
}
