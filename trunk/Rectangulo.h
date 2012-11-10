#ifndef RECTANGULO_H
#define RECTANGULO_H

#include "Objeto.h"
#include "precision.h"

class Rectangulo : public Objeto
{
    public:
        Rectangulo(real largo, real ancho, real masa);
        virtual void pintar();
        virtual ~Rectangulo();
    protected:
    private:

};

#endif // RECTANGULO_H
