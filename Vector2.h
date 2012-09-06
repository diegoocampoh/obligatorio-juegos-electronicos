#define VECTOR2_H

typedef float real;
class Vector2
{
    public:
        Vector2();
        Vector2(const real x, const real y);
        virtual ~Vector2();
        real x;
        real y;
    protected:
    private:
};
