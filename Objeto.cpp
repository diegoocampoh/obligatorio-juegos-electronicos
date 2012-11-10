#include "Objeto.h"

Objeto::Objeto()
{

}



Objeto::~Objeto()
{

}

void Objeto::pintar()
{

}

void Objeto::actualizarPosicion()
{
    std::list<Vector2*>::const_iterator pos;
    Vector2 resultante = Vector2(0,0);
    for(pos = fuerzas.begin(); pos != fuerzas.end(); ++pos)
        resultante = *((Vector2*) *pos) + resultante;
    Vector2 Naceleracion = resultante * (1/masa);
    Vector2 Nvelocidad = *this->velocidad + Naceleracion;
    *this->posicion = *this->posicion + Nvelocidad;
}
