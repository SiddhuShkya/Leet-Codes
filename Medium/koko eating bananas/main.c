
#include <stdio.h>
#include <stdbool.h>

int maxPiles(int *piles, int size) {
    int max = piles[0];
    for (int i = 1; i < size; i++) {
        if (max < piles[i]) {
            max = piles[i];
        }
    }
    return max;
}

bool canFinish(int *piles, int pilesSize, int K, int H) {
    int hours_needed = 0;
    
    for (int i = 0; i < pilesSize; i++) {
        hours_needed += (piles[i] + K - 1) / K; // equivalent to math.ceil(piles[i] / K)
    }

    return hours_needed <= H;
}

int minEatingSpeed(int* piles, int pilesSize, int h) {
    int l, r;
    l = 1;
    r = maxPiles(piles, pilesSize);
    
    while (l < r) {
        int mid = (l + r) / 2;
        if (canFinish(piles, pilesSize, mid, h)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    
    return l;
}

int main() {
    int piles[] = {3, 6, 7, 11};
    int h = 8;
    int result = minEatingSpeed(piles, 4, h);
    printf("%d\n", result);  // Expected output: 4
    return 0;
}
