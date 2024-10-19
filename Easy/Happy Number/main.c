#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isHappy(int n) {
    int seen[1000] = {0};  // Array to track seen numbers
    int idx = 0;           // Index to track the position in the array

    while (n != 1) {
        int total = 0;
        int tmp = n;
        
        while (tmp > 0) {
            int dt = tmp % 10;   // Get last digit
            total += dt * dt;    // Square the digit and add to total
            tmp /= 10;           // Remove last digit
        }

        // Check for cycles
        for (int i = 0; i < idx; i++) {
            if (seen[i] == total) {
                return false;    // Cycle detected, not a happy number
            }
        }

        seen[idx++] = total;  // Add total to the seen array
        n = total;            // Update n to the sum of squares
    }
    return true;  // Happy number if we reach 1
}