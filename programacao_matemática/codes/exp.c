#include <stdio.h>
#include <math.h>

float f(int x) {
  int base = 2;
  return pow(base, x);
}

int main(int argc, char *argv[]) {
  for (int i = 0; i < 20; i++) {
    printf("%f\n", f(i));
  }
  return 0;
}
