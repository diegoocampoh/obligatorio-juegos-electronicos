#include "Fuerza.h"

Fuerza::Fuerza(Vector2* direccion, real magnitud)
{
    this->direccion = direccion;
    this->magnitud = magnitud;
}

Fuerza::~Fuerza()
{
    delete direccion;
}
