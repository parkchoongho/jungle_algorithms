#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int arr[2] = {0 ,1};
    int target = atoi(argv[1]);

    for (int i = 3; i <= target; i++) {
        if (i % 2 == 0)
            arr[1] = arr[0] + arr[1];
        else
            arr[0] = arr[0] + arr[1]; 
    }

    if (target % 2 == 0)
        printf("%d번째 수는 %d입니다.\n", target, arr[1]);
    else
        printf("%d번째 수는 %d입니다.\n", target, arr[0]);
}