#include <stdlib.h>
#include <SDL.h>
#include <iostream>
#include "Vector2.h"
#include <string>
#include "matrix.h"
#include <gl/gl.h>
#include "Engine.h"
#include "Escenario.h"

using namespace std;

int main ( int argc, char** argv )
{

    float theta = 0.0f;
    bool done = false;
    Escenario* esc = new Escenario();
    Engine* Eng = Engine::Instance();
    Engine::Instance()->push();
    glTranslatef(0.0,0.0,-4.0);
    Rectangulo* obj = new Rectangulo(0.05f,0.05f, 0.0005f);
    obj->posicion = new Vector2(0,0);
    obj->fuerzas.push_back(new Vector2(0,0.005f));
    esc->objetos.push_back(obj);
    Eng->clear();
    Eng->update();

    // program main loop
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
                    break;
                    esc->pintar();
                }
            } // end switch
        } // end of message processing

    } // end main loop
    return 0;
}
