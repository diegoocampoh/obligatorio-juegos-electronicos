#ifndef PRECISION_H_INCLUDED
#define PRECISION_H_INCLUDED

#include <math.h>

namespace engine {
/**
* Defines a real number precision. Cyclone can be compiled in
* single- or double-precision versions. By default single precision
* is provided.
*/
typedef float real;

/** Defines the precision of the square root operator. */
#define real_sqrt sqrtf
}

#endif // PRECISION_H_INCLUDED
