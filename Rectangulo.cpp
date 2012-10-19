#include "Rectangulo.h"
#include "precision.h"
#include "Engine.h"
Rectangulo::Rectangulo()
{
    this->vertices = new real[18] {
                        1, 1, 1,  -1, 1, 1,  -1,-1, 1,      // v0-v1-v2 (adelante)  |-/
                        -1,-1, 1,   1,-1, 1,   1, 1, 1      // v2-v3-v0  /_|
                        };
    this->colores   = new real[18]{
                    1, 1, 1,   1, 1, 0,   1, 0, 0,      // v0-v1-v2 (adelante)
                    1, 0, 0,   1, 0, 1,   1, 1, 1
                    };    // v2-v3-v0
}

Rectangulo::~Rectangulo()
{
    delete vertices;
    delete colores;
}

void Rectangulo::pintar()
{
    Engine* Eng = Engine::Instance();
    Eng->push();
        Eng->set_translation(this->posicion->x,this->posicion->y);
        Eng->draw_test(vertices,colores,6);
    Eng->pop();
}
