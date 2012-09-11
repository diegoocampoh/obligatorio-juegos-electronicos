#define VECTOR2_H

typedef float Real;
class Vector2
{
    public:
        Vector2();
        Vector2(const Real x, const Real y);
        virtual ~Vector2();
        Real x;
        Real y;
    protected:
    private:
};
