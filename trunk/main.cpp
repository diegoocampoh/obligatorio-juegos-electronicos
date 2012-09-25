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
/*
    Vector2* vec = new Vector2(1,-1);
    printf(" %f %f \n",vec->x, vec->y);
    cout << vec->x << "\n"  << vec->y ;
    return 0;
*/

    Escenario* esc = new Escenario();
    Objeto* obj = new Objeto();
    esc->objetos.push_back(obj);
   // esc.addObjeto(obj);


    Engine* Eng = new Engine(500,500);
    Eng->clear();
    Eng->update();



    Real vertices[] = {
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

    Real colores[]   = {
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
/*
    // initialize SDL video
    if ( SDL_Init( SDL_INIT_VIDEO ) < 0 )
    {
        printf( "Unable to init SDL: %s\n", SDL_GetError() );
        return 1;
    }

    // make sure SDL cleans up before exit
    atexit(SDL_Quit);

    // create a new window
    SDL_Surface* screen = SDL_SetVideoMode(640, 480, 16,
                                           SDL_HWSURFACE|SDL_DOUBLEBUF);
    if ( !screen )
    {
        printf("Unable to set 640x480 video: %s\n", SDL_GetError());
        return 1;
    }

    // load an image
    SDL_Surface* bmp = SDL_LoadBMP("cb.bmp");
    if (!bmp)
    {
        printf("Unable to load bitmap: %s\n", SDL_GetError());
        return 1;
    }

    // centre the bitmap on screen
    SDL_Rect dstrect;
    dstrect.x = (screen->w - bmp->w) / 2;
    dstrect.y = (screen->h - bmp->h) / 2;
*/

    float theta = 0.0f;
    // program main loop
    bool done = false;
    while (!done){
        // message processing loop
        SDL_Event event;
        while (SDL_PollEvent(&event)){
            // check for messages
            switch (event.type){
                // exit if the window is closed
                case SDL_QUIT:
                    done = true;
                    break;

                // check for keypresses
                case SDL_KEYDOWN:{
                    // exit if ESCAPE is pressed
                    if (event.key.keysym.sym == SDLK_ESCAPE)
                        done = true;
                    break;
                }
            } // end switch
        } // end of message processing
        Eng->clear();
        Eng->push();
            glTranslatef(0.0,0.0,-4.0);
                Eng->push();
                        Eng->set_translation(-1,0);
                        Eng->set_rotation(theta);
                        Eng->draw_test(vertices,colores,36);
                 Eng->pop();
                 Eng->push();
                        Eng->set_translation(1,0);
                        Eng->set_rotation(-theta*2);
                        Eng->draw_test(vertices,colores,12);
                Eng->pop();
        Eng->pop();
        Eng->update();

        theta += 1.13f;
        // DRAWING STARTS HERE

        // clear screen
//        SDL_FillRect(screen, 0, SDL_MapRGB(screen->format, 0, 0, 0));

        // draw bitmap
  //      SDL_BlitSurface(bmp, 0, screen, &dstrect);

        // DRAWING ENDS HERE

        // finally, update the screen :)
    //    SDL_Flip(screen);
    } // end main loop

    // free loaded bitmap
//    SDL_FreeSurface(bmp);

    // all is well ;)
    //printf("Exited cleanly\n");
    return 0;
}
