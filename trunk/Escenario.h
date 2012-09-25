#ifndef ESCENARIO_H
#define ESCENARIO_H
#include "Objeto.h"
#include <list>

class Escenario
{
    public:
        Escenario();
        virtual ~Escenario();
        void addObjeto(Objeto * obj);
        list<Objeto*> objetos;


    protected:
    private:
};

#endif // ESCENARIO_H
