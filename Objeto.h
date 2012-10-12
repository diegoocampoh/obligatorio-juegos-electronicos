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
        real* vertices;
        real* colores;
        std::list<Fuerza*> fuerzas;
        Vector2* posicion;
        Vector2* velocidad;

        Vector2* calcularAceleracion();
        void actualizarPosicion();
        virtual void pintar();
    protected:
    private:
};

#endif // OBJETO_H
