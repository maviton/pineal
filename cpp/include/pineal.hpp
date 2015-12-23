#include <SFML/Graphics.hpp>

class Entity;
class Drawable;
class Surface;


class Entity {
};

class Drawable : public Entity {
    public:
        virtual ~Drawable();
        virtual void draw(sf::RenderTarget*);
};

class Surface : public Entity {
    public:
        void set_child(Drawable* _child);

    protected:
        Drawable* child;
};


class Window : public Surface {
    public:
        Window(const char* name);
        void display();
        bool is_open();
        static Window* memo(const char* name);

    private:
        sf::RenderWindow sf_window;
};

class Polygon : public Drawable {
    public:
        Polygon(int);
        void draw(sf::RenderTarget*);
        static Polygon* memo(int);

   private:
        sf::CircleShape sf_polygon;
};
