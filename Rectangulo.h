#ifndef RECTANGULO_H
#define RECTANGULO_H

#include "Objeto.h"


class Rectangulo : public Objeto
{
    public:
        Rectangulo();
        virtual void pintar();
        virtual ~Rectangulo();
    protected:
    private:

};

#endif // RECTANGULO_H
