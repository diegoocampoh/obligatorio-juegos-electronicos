#ifndef ENGINE_H
#define ENGINE_H

#include "Vector2.h"
#include <gl/gl.h>
#include <SDL.h>
#include <assert.h>

class Engine
{
    public:
        Engine(int width, int height);
        virtual ~Engine();
        void clear();
        void update();
        void close();
        void set_rotation(Real angle);
        void set_translation(Real x, Real y);
        void set_scale(Real x, Real y);
        void push();
        void pop();
        void reset();

        SDL_Surface * Surface;
        void draw_test(Real *vertices, Real *colores, int cantVertices);
    protected:
    private:
        int Width,Height;
};

#endif // ENGINE_H
