#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int extractCalibrationValue(const char* line);

int main() 
{
    FILE *fptr;
    char line[256];
    int totalSum = 0;

    const char *filePath = "InputFile";

    // Open file in read mode
    fptr = fopen(filePath, "r");
    if (fptr == NULL) 
    {
        printf("Error! opening file\n");
        exit(1);
    }

    // Reads the file
    while (fgets(line, sizeof(line), fptr))
    {
        // Extract the calibration value of the current line
        int calibrationValue = extractCalibrationValue(line);
        // Adds the value to the whole sum
        totalSum += calibrationValue;
    }

    // Close the file
    fclose(fptr);

    // Prints the solution
    printf("The sum of all calibration values is: %d\n", totalSum);

    return 0;
}

int extractCalibrationValue(const char* line) 
{
    int firstDigit = -1;
    int lastDigit = -1;

    // Finds first and last number
    for (const char* p = line; *p != '\0'; ++p) 
    {
        if (isdigit(*p)) 
        {
            if (firstDigit == -1) 
            {
                // Cast from char to int
                firstDigit = *p - '0';
            }
            // Safes last number
            lastDigit = *p - '0';
        }
    }

    // If there is no number, then there will be 0 returned
    if (firstDigit == -1 || lastDigit == -1) 
    {
        return 0;
    }

    // Combines both numbers
    return firstDigit * 10 + lastDigit;
}