# geometry

A collection of code to generate, draw, and manipulate geometric figures

Source methods are in `geomlib.py`. Allows user to execute translation,
rotation, and reflection geometric transformations on numpy.matrix objects.
Also includes a few methods for computationally generating polygon coordinates.

To run example,

1. Make a new directory (Ex: temp/)
2. Run polygonDemo (Ex: `python polygonDemo.py`)
3. Feed the directory you made to the program (Ex: temp/)
4. Browse the .svg files created in the directory

I am aware that numpy is not planning on maintaining the matrix object for much
longer. This project was mostly made as a curiosity into linear transformations,
so I'm not planning on fixing the code to run on numpy array objects, but if anyone
wants me to, I will so just shoot me a message! For this reason, the documentation is
also a little sparse/inconsistent.
