#ifndef FUERZA_H
#define FUERZA_H

#include "Vector2.h"
#include "precision.h"

using namespace engine;

class Fuerza
{
    public:
        Fuerza(Vector2* direccion, real magnitud);
        virtual ~Fuerza();
        real magnitud;
        Vector2* direccion;

    protected:
    private:
};

#endif // FUERZA_H
