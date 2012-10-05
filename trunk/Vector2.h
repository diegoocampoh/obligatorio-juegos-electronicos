#ifndef VECTOR2_H
#define VECTOR2_H

#include "precision.h"

namespace engine {
/**
* Holds a vector in 3 dimensions. Four data members are allocated
* to ensure alignment in an array.
*/
    class Vector2{
        public:
            real x;
            real y;

            private:
                real pad;
            public:

            Vector2() : x(0), y(0) {}
            Vector2(const real x, const real y) : x(x), y(y) {}
            void invert(){
                x = -x;
                y = -y;
            }

            real magnitude() const { return real_sqrt(x*x+y*y); }
            real squareMagnitude() const { return x*x+y*y; }
            /** Turns a non-zero vector into a vector of unit length. */
            void normalize() {
                real l = magnitude();
                if (l > 0) {
                    (*this)*=((real)1)/l;
                }
            }

            /** Multiplies this vector by the given scalar. */
            void operator*=(const real value) {
                x *= value;
                y *= value;
            }

            /** Returns a copy of this vector scaled to the given value. */
            Vector2 operator*(const real value) const {
                return Vector2(x*value, y*value);
            }

            /** Adds the given vector to this. */
            void operator+=(const Vector2& v) {
                x += v.x;
                y += v.y;
            }
            /**
            * Returns the value of the given vector added to this.
            */
            Vector2 operator+(const Vector2& v) const {
                return Vector2(x+v.x, y+v.y);
            }

            /** Subtracts the given vector from this. */
            void operator-=(const Vector2& v) {
                x -= v.x;
                y -= v.y;
            }

            /**
            * Returns the value of the given vector subtracted from this.
            */
            Vector2 operator-(const Vector2& v) const {
                return Vector2(x-v.x, y-v.y);
            }

            /**
            * Adds the given vector to this, scaled by the given amount.
            */
            void addScaledVector(const Vector2& vector, real scale) {
                x += vector.x * scale;
                y += vector.y * scale;
            }

            /**
            * Calculates and returns a component-wise product of this
            * vector with the given vector.
            */
            Vector2 componentProduct(const Vector2 &vector) const {
                return Vector2(x * vector.x, y * vector.y);
            }

            /**
            * Performs a component-wise product with the given vector and
            * sets this vector to its result.
            */
            void componentProductUpdate(const Vector2 &vector) {
                x *= vector.x;
                y *= vector.y;
            }

            /**
            * Calculates and returns the scalar product of this vector
            * with the given vector.
            */
            real scalarProduct(const Vector2 &vector) const {
                return x*vector.x + y*vector.y;
            }

            /**
            * Calculates and returns the scalar product of this vector
            * with the given vector.
            */
            real operator *(const Vector2 &vector) const {
                return x*vector.x + y*vector.y;
            }

            /*
            El producto de vectores en dos dimensiones es en el eje z
            Vector2 vectorProduct(const Vector2 &vector) const {
                return Vector2(y*vector.z - z*vector.y,
                                z*vector.x - x*vector.z,
                                x*vector.y - y*vector.x);
            }
            */


            // Updates this vector to be the vector product of its current
            // value and the given vector.
/*
            void operator %=(const Vector2 &vector)
            {
                *this = vectorProduct(vector);
            }
  //          * Calculates and returns the vector product of this vector
    //        * with the given vector.
            Vector2 operator%(const Vector2 &vector) const
            {
                return Vector2(y*vector.z-z*vector.y,
                z*vector.x-x*vector.z,
                x*vector.y-y*vector.x);
            }
*/

    };
}

#endif
