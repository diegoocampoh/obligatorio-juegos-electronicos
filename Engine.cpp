#include "Engine.h"

Engine* Engine::pinstance = 0;
Engine* Engine::Instance()
{
    if(pinstance == 0)
        pinstance = new Engine();
    return pinstance;
}

Engine::Engine(){
    int width, height;
    height = 800;
    width = 800;
    Surface = NULL;
    this->Width = width;
    this->Height = height;
    assert (SDL_Init(SDL_INIT_VIDEO) == 0);
    Surface = SDL_SetVideoMode(this->Width,this->Height,0,SDL_OPENGL|SDL_DOUBLEBUF);
    assert(Surface != NULL);

    SDL_WM_SetCaption("GL y SDL LOCO",NULL);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-1,1,-1,1,1,100);
    glViewport(0, 0, this->Width, this->Height);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glClearColor(0.0f,0.0f,0.0f,0.0f);

        /** zbuffer **/
    glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
        /** back face culling **/
    glEnable(GL_CULL_FACE);
}

void Engine::clear(){
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void Engine::update(){
    SDL_GL_SwapBuffers();
}

void Engine::close(){
    SDL_Quit();
}

void Engine::set_rotation(real angle){
    glRotatef(angle,1,-1,1);
}

void Engine::set_translation(real x,real y){
    glTranslatef(x,y,0);
}

void Engine::set_scale(real x, real y){
    glScalef(x,y,1);
}

void Engine::push(){
    glPushMatrix();
}

void Engine::pop(){
    glPopMatrix();
}

void Engine::reset(){
    glLoadIdentity();
}

void Engine::draw_test(real *vertices, real *colores, int cantVertices){
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);

    glVertexPointer(3,GL_FLOAT,0,vertices);
    glColorPointer(3, GL_FLOAT, 0, colores);
    glDrawArrays(GL_TRIANGLES,0,cantVertices);

    glDisableClientState(GL_COLOR_ARRAY);
    glDisableClientState(GL_VERTEX_ARRAY);
}


Engine::~Engine(){
    delete(Surface);
}

