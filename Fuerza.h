#ifndef FUERZA_H
#define FUERZA_H

#include "Vector2.h"

class Fuerza
{
    public:
        Fuerza();
        virtual ~Fuerza();
        Real magnitud;
        Vector2* direccion;

    protected:
    private:
};

#endif // FUERZA_H
