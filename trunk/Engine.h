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
        Engine(int width, int height);
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
    private:
        int Width,Height;
};

#endif // ENGINE_H
