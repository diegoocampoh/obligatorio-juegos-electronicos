#ifndef OBJETO_H
#define OBJETO_H

#include <list>
#include "Fuerza.h"
#include "Vector2.h"

using namespace std;
class Objeto
{
    public:
        Objeto();
        virtual ~Objeto();
        Real* vertices;
        Real* colores;
        std::list<Fuerza*> fuerzas;
        Vector2* posicion;
        Vector2* velocidad;

        Vector2* calcularAceleracion();
        void actualizarPosicion();
        void pintar
    protected:
    private:
};

#endif // OBJETO_H
