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
    Engine::Instance()->push();
    glTranslatef(0.0,0.0,-4.0);

    std::list<Objeto*>::const_iterator pos;
    for(pos = objetos.begin(); pos != objetos.end(); ++pos)
        ((Objeto*) *pos)->pintar();

    Engine::Instance()->pop();
    Engine::Instance()->update();
}
