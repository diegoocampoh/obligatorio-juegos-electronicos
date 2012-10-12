#ifndef ENGINE_H
#define ENGINE_H

#include "Vector2.h"
#include <gl/gl.h>
#include <SDL.h>
#include <assert.h>

using namespace engine;

class Engine
{
    public:
        static Engine* Instance();
        virtual ~Engine();
        void clear();
        void update();
        void close();
        void set_rotation(real angle);
        void set_translation(real x, real y);
        void set_scale(real x, real y);
        void push();
        void pop();
        void reset();

        SDL_Surface * Surface;
        void draw_test(real *vertices, real *colores, int cantVertices);
    protected:

      Engine();
      Engine(const Engine & ) ;
      Engine &operator= (const Engine & ) ;
    private:
        int Width,Height;
        static Engine* pinstance;
};

#endif // ENGINE_H
