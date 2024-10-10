#include <stdio.h>
#include <math.h>
#define ANGLE 30.0
int main() {
// Convert angle to radians
double radians = ANGLE * (M_PI / 180.0);
// Calculate unit vector components
double x = cos(radians);
double y = sin(radians);
// Open file for writing
FILE *file = fopen("output.txt", "w");
if (file == NULL) {
printf("Error opening file!\n");
return 1;
}
// Write the vector components to the file
fprintf(file, "%f %f\n", x, y);
// Close the file
fclose(file);
return 0;
}
