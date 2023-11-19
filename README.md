# Pygame Basics

This is a very brief walkthrough of [how to set up the Pygame library](#installation), and a [list of resources](#resources) that you might find useful for using Pygame to make things.

## Important Concepts

Before you get started even installing Pygame, please check your understanding on the following tools and concepts. They are prevalent across Pygame as a library and its typical use cases, and used often throughout this whole tutorial.

* The terminal (or command-line interface)
* Objects, Classes, and Inheritance
* Functions
* Global and local variables
* Loops
* Data Structures: Lists, Dictionaries, Tuples

## Installation

Just open your terminal and type one of the following:

```bash
pip install pygame
# OR
pip3 install pygame
```

Once it has finished downloading, make sure it's actually installed by running one of the examples. There are several, but the official Pygame setup tutorial recommends the following:

```bash
python -m pygame.examples.aliens
# OR
python3 -m pygame.examples.aliens
```

If the game starts up, you're good to go!

### Note for Mac Users *Without* Apple Silicon

 ``python3`` and ``python`` (and ``pip``/``pip3``) both refer to some Python version on your computer. If you have a Mac without Apple Silicon, there's a good chance that you have Python 2 *in addition to Python 3* on your computer. ``python`` or ``python2``, and ``pip``, will usually refer to your Python 2 installation, but not always.

You can check which Python is run where with the following commands:

```bash
python --version
python3 --version
```

If ``python --version`` outputs ``Python 3.x.x``, then you're in the clear. Otherwise, you'll have to use ``python3`` to run commands.

### DISCLAIMER

Please note that this is not necessarily how you *should* set up Pygame (or other Python libraries) while coding. Normally, you would use something called a "virtual environment" - but that isn't necessary, and makes things a little bit more complicated than they need to be for now.

If you *really* want to know, ask a TA, or you can try [this tutorial](https://realpython.com/python-virtual-environments-a-primer/). **Please remember, though this is by no means necessary for your final project!**

## Coding with Pygame

Once you've installed Pygame, bust open your code editor and create a folder for your project, and make a Python file.

I'll be using [this tutorial code](https://www.pygame.org/docs/) from the official Pygame docs as an introduction to some of the important components of this library.

### Setting Up Pygame

The first few things you want to put in your document are as following, with explanatory comments:

```python
import pygame # Necessary to use pygame at all

# Set up global variables
## Start all the pygame modules you use in your code.
pygame.init()

## This creates your game window. The tuple inside determines the size, in pixels, of the window. I don't recommend it, but you can leave this blank; it will set your window to the size of your screen.
screen = pygame.display.set_mode((500, 300))

# Not always necessary. pygame.time is used to control framerate and things related to it.
clock = pygame.time.Clock() 

# Typically, all pygame updates are run in a single loop. We use the running variable to maintain and eventually stop it.
running = True 
while running:
    # This loop basically just checks to see if your user exited the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Your code will go here, once you start building!

    # Update the display with any changes you've made.
    pygame.display.flip()

    # limits FPS to 60. Not always necessary.
    clock.tick(60)

# Once your loop is finished (i.e. your game is done), remember to close the pygame modules.
pygame.quit()
```

This code doesnt actually do anything yet. Let's get it to do something!

### Moving an Object Around

This isn't going to be exciting or anything, we're just going to have a thing move around on the screen.

Let's start by putting in a background and creating something for the player to use:

```python
while running:
    ...

    # In addition to changing the "background," filling the screen "erases" anything from the previous frame.
    screen.fill("purple")

    # This line draws a yellow circle in the middle of the screen.
    # A Vector2 is an (x,y) pair that pygame uses to put things on a screen.
    # Note also that we can get the screen's width and height using its appropriate getter methods.
    # pygame.draw.circle( <display to draw to> , <color fill> , <center position> , <radius/size> )
    pygame.draw.circle(screen, "yellow", pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 40)
```

Great! Now we have a yellow circle in the center of the window. But it just sits there. Let's have the player move it around.

To do that, we have to refactor our code a little bit: we want to make sure that we store the position of the circle so that we can draw it in a different place every frame -- which will let us move it.

```python
# We move our position vector into a variable. This will let us change it between frames (loop iterations).
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True 
while running:
    ...

    screen.fill("purple")

    # Here, we replace our previous Vector2 with our new variable.
    pygame.draw.circle(screen, "yellow", player_pos, 40)
```

This code should work the same as your last one. *Now* we're ready to let the player do some movement!

Pygame can read keyboard input via ``pygame.key.get_pressed()``. It returns a dictionary containing pygame key-codes as keys, and booleans as values. Let's use that to have our player move around with WASD:

```python
while running:
    ...
    pygame.draw.circle(screen, "yellow", player_pos, 40)

    # First, we get all the keys on our keyboard:
    keys = pygame.key.get_pressed()

    # Then, we check to see if any of WASD are pressed.
    # If they are, we change player_pos in the appropriate direction by adding or subtracting from x or y.

    # See these pygame.K_<char> items? Each of these represents a key on your keyboard.
    # A full table of these items can be found in the references section below.

    if keys[pygame.K_w]:
        # Vector2 has an attribute for y...
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        # and for x!
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10

    # Note that the y value is inverted from what you might expect: to move up, we need to *subtract*. Smaller numbers are further up.
    # In other words, pygame's (0, 0) position is in the *top left*, not the *bottom left* like a typical graph.
```

And you're done! You've created a pygame program where a player can move a circle around on the screen.

The full code for this tutorial (without hints) is in [example.py](example.py). You can also explore an advanced version of this example, [example+.py](example+.py), which has one or two extra things that might make your code a little cleaner and cover "edge cases" that might be helpful for your game (with explanatory comments, of course).

## Resources

This is only the start of your journey! Below are some resources that you might find helpful. Pygame has been around for YEARS, so you should have no shortage of hints and tutorials to use.

You can also look to pygame's various built-in examples that come with with your installation.

* [Pygame Official Documentation](https://www.pygame.org/docs/)
  * [List of built-in example files](https://www.pygame.org/docs/ref/examples.html)
  * [How colors work](https://www.pygame.org/docs/ref/color.html)
  * [Keyboard functionality and keystroke code table](https://www.pygame.org/docs/ref/key.html)
  * [Surfaces: Images!](https://www.pygame.org/docs/ref/surface.html)
* [A Newbie Guide to pygame (from the Pygame documentation)](https://www.pygame.org/docs/tut/newbieguide.html)
* [Pygame Official Wiki: Tutorials](https://www.pygame.org/wiki/tutorials)
* Potentially helpful built-in Python modules
  * [math](https://devdocs.io/python/library/math)
  * [random](https://devdocs.io/python/library/random)
* If it's not here, [just Google it!](https://www.google.com/)
