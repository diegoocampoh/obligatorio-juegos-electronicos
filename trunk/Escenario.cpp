#include "Escenario.h"
#include "Engine.h"
#include "Rectangulo.h"

Escenario::Escenario()
{
    Engine* Eng = Engine::Instance();
    Rectangulo* obj = new Rectangulo();
    obj->posicion = new Vector2(0,0);
    obj->fuerzas.push_back(new Fuerza(new Vector2(0,1), 1));
    this->objetos.push_back(obj);
    Eng->clear();
    Eng->update();
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
