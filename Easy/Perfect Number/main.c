#include <stdio.h>
#include <stdbool.h>
 
bool checkPerfectNumber(int);

bool checkPerfectNumber(int num) {
    if (num <= 1){
        return false;
    }
    int total = 1;
    int i = 2;
    while (i * i <= num){
        if (num%i == 0){
            total += i;
            if (i != (int) num/i){
                total += (int) num/i;
            }
        }
        i++;
    }
    return total == num;
}

int main(){
    int n = 6;
    bool res = checkPerfectNumber(n);
    if (res){
        printf("%d is perfect number.\n", n);
        return 0;
    }
    printf("%d is not a perfect number.\n", n);
    return 0;
}