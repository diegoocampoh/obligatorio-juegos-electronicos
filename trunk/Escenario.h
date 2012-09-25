#ifndef ESCENARIO_H
#define ESCENARIO_H
#include "Objeto.h"
#include <list>

using namespace std;

class Escenario
{
    public:
        Escenario();
        virtual ~Escenario();
        std::list<Objeto*> objetos;

    protected:
    private:
};

#endif // ESCENARIO_H
