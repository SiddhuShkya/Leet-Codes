#include <stdio.h>
#include <stdbool.h>

// Function remains the same, using int** for a 2D array
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int rows, cols, r, c;
    rows = matrixSize;
    cols = *matrixColSize;  // Dereference pointer to get number of columns
    r = 0;
    c = cols - 1;

    while (r < rows && c >= 0) {
        if (matrix[r][c] == target) {
            return true;
        } else if (matrix[r][c] < target) {
            r += 1;
        } else {
            c -= 1;
        }
    }
    return false;
}

int main() {
    int target = 3;
    int arr[3][4] = {
        {1, 3, 5, 7}, 
        {10, 11, 16, 20}, 
        {23, 30, 34, 60}
    };

    int* matrix[3];  // Array of pointers to represent the rows of the matrix
    for (int i = 0; i < 3; i++) {
        matrix[i] = arr[i];  // Point each row pointer to the respective row in arr
    }

    int matrixSize = sizeof(arr) / sizeof(arr[0]);  // Number of rows
    int matrixColSize = sizeof(arr[0]) / sizeof(arr[0][0]);  // Number of columns

    // Pass the array of pointers and column size as pointer to the function
    bool res = searchMatrix(matrix, matrixSize, &matrixColSize, target);
    printf("res = %d\n", res);  // Output will be 1 if true, 0 if false
    
    return 0;
}
