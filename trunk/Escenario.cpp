#include "Escenario.h"
#include "Engine.h"
Escenario::Escenario()
{

}


Escenario::~Escenario()
{

}

void Escenario::pintar()
{
    Engine::Instance()->clear();
    std::list<Objeto*>::const_iterator pos;
    for(pos = objetos.begin(); pos != objetos.end(); ++pos)
        ((Objeto*) *pos)->pintar();
    Engine::Instance()->update();
}
