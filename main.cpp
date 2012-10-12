#include <stdlib.h>
#include <SDL.h>
#include <iostream>
#include "Vector2.h"
#include <string>
#include "matrix.h"
#include <gl/gl.h>
#include "Engine.h"
#include "Escenario.h"
#include "Rectangulo.h"

using namespace std;

int main ( int argc, char** argv )
{


    real verticesCuadrado [] = {
                                1, 1, 1,  -1, 1, 1,  -1,-1, 1,      // v0-v1-v2 (adelante)
                       -1,-1, 1,   1,-1, 1,   1, 1, 1      // v2-v3-v0
                                };
        real coloresCuadrado[]   = {
                        1, 1, 1,   1, 1, 0,   1, 0, 0,      // v0-v1-v2 (adelante)
                        1, 0, 0,   1, 0, 1,   1, 1, 1  };    // v2-v3-v0

    real vertices[] = {
                        1, 1, 1,  -1, 1, 1,  -1,-1, 1,      // v0-v1-v2 (adelante)
                       -1,-1, 1,   1,-1, 1,   1, 1, 1,      // v2-v3-v0

                        1, 1, 1,   1,-1, 1,   1,-1,-1,      // v0-v3-v4 (derecha)
                        1,-1,-1,   1, 1,-1,   1, 1, 1,      // v4-v5-v0

                        1, 1, 1,   1, 1,-1,  -1, 1,-1,      // v0-v5-v6 (arriba)
                       -1, 1,-1,  -1, 1, 1,   1, 1, 1,      // v6-v1-v0

                       -1, 1, 1,  -1, 1,-1,  -1,-1,-1,      // v1-v6-v7 (izquierda)
                       -1,-1,-1,  -1,-1, 1,  -1, 1, 1,      // v7-v2-v1

                       -1,-1,-1,   1,-1,-1,   1,-1, 1,      // v7-v4-v3 (abajo)
                        1,-1, 1,  -1,-1, 1,  -1,-1,-1,      // v3-v2-v7

                        1,-1,-1,  -1,-1,-1,  -1, 1,-1,      // v4-v7-v6 (atras)
                       -1, 1,-1,   1, 1,-1,   1,-1,-1 };    // v6-v5-v4

    real colores[]   = {
                        1, 1, 1,   1, 1, 0,   1, 0, 0,      // v0-v1-v2 (adelante)
                        1, 0, 0,   1, 0, 1,   1, 1, 1,      // v2-v3-v0

                        1, 1, 1,   1, 0, 1,   0, 0, 1,      // v0-v3-v4 (derecha)
                        0, 0, 1,   0, 1, 1,   1, 1, 1,      // v4-v5-v0

                        1, 1, 1,   0, 1, 1,   0, 1, 0,      // v0-v5-v6 (arriba)
                        0, 1, 0,   1, 1, 0,   1, 1, 1,      // v6-v1-v0

                        1, 1, 0,   0, 1, 0,   0, 0, 0,      // v1-v6-v7 (izquierda)
                        0, 0, 0,   1, 0, 0,   1, 1, 0,      // v7-v2-v1

                        0, 0, 0,   0, 0, 1,   1, 0, 1,      // v7-v4-v3 (abajo)
                        1, 0, 1,   1, 0, 0,   0, 0, 0,      // v3-v2-v7

                        0, 0, 1,   0, 0, 0,   0, 1, 0,      // v4-v7-v6 (atras)
                        0, 1, 0,   0, 1, 1,   0, 0, 1 };    // v6-v5-v4

    float theta = 0.0f;
    // program main loop
    bool done = false;
    Escenario* esc = new Escenario();
    Engine* Eng = Engine::Instance();
    Rectangulo* obj = new Rectangulo();
    obj->posicion = new Vector2(0,0);
    obj->fuerzas.push_back(new Fuerza(new Vector2(0,1), 1));
    esc->objetos.push_back(obj);
    Eng->clear();
    Eng->update();

    while (!done){
//         message processing loop
        SDL_Event event;

        while (SDL_PollEvent(&event)){
//             check for messages
            switch (event.type){
//                 exit if the window is closed
                case SDL_QUIT:
                    done = true;
                    break;
 //                check for keypresses
                case SDL_KEYDOWN:{
   //                  exit if ESCAPE is pressed
                    if (event.key.keysym.sym == SDLK_ESCAPE)
                        done = true;
                    if(event.key.keysym.sym == SDLK_DOWN)
                    {
                        obj->posicion->y-=0.05f;
                    }
                    if(event.key.keysym.sym == SDLK_UP)
                    {
                        obj->posicion->y+=0.05f;
                    }
                    if(event.key.keysym.sym == SDLK_RIGHT)
                    {
                        obj->posicion->x+=0.05f;
                    }
                    if(event.key.keysym.sym == SDLK_LEFT)
                    {
                        obj->posicion->x-=0.05f;
                    }
                    esc->pintar();
                    break;
                }
            } // end switch
        } // end of message processing

    } // end main loop
    return 0;
}
