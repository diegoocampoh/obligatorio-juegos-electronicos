#include <stdlib.h>
#include <SDL.h>
#include <iostream>
#include "Vector2.h"
#include <string>

using namespace std;

int main ( int argc, char** argv )
{

    Vector2* vec = new Vector2(1,-1);
    printf(" %f %f \n",vec->x, vec->y);
    cout << vec->x << "\n"  << vec->y ;
    return 0;
}
