#include "Escenario.h"


Escenario::Escenario()
{
    //ctor
}

void addObjeto(Objeto * obj)
{
    objetos.push_back(obj);
}


Escenario::~Escenario()
{
    //dtor
}
