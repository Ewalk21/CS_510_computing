# CS510 HW 6

**Author(s):** **CHANGEME**

[![Build Status](https://travis-ci.com/chapman-cs510-2017f/hw-06-YOURNAME.svg?token=CHANGEME&branch=master)](https://travis-ci.com/chapman-cs510-2017f/hw-06-YOURNAME)

## Specification

1. Complete the classwork, in collaboration with your group (using Slack as needed).
1. Copy the python modules from CW06 into this repository. Create a python module ```cplane-np-hw.py``` that imports ```cplane-np```.
1. In your python module ```cplane-np-hw.py```, create a function ```julia(c, max=100)``` that takes a complex parameter ```c``` and an optional positive integer ```max```, and returns a **function** specified by the following algorithm:
    * The returned function should take one complex parameter ```z``` as an input, and return one positive integer as an output.
    * If the input number ```z``` has a magnitude ```abs(z)``` larger than 2, the function should output the integer 1.
    * Otherwise, set a counter ```n=1```.
    * Increment ```n``` by 1, then transform the input ```z``` according to the formula ```z = z**2 + c```. Check the resulting magnitude ```abs(z)```: If the magnitude now exceeds 2, then return the value of ```n```; If the magnitude does not yet exceed 2, repeat this step.
    * If the positive integer ```max``` is reached before the magnitude of ```z``` exceeds 2, the preceding loop should abort and return the output integer 0.
1. Create a new class ```JuliaPlane``` that subclasses your ```ArrayComplexPlane``` class. We are going to extend that class with interesting functionality:
    * Change the ```__init__``` method to accept only a single argument ```c```, which is a complex number. Have the init call the ```___init___``` method of the parent class, assuming the default values ```xmin=ymin=-2``` and ```xmax=ymax=2``` and ```xlen=ylen=1000```. Have the init call also immediately apply the function ```julia``` to the plane, using the input argument ```c``` used to initialize the class. (Note that the transformed plane will now be a 2D array of positive integers, and ```fs``` will now contain one function.)
    * Change the ```refresh``` method to accept only a single argument ```c```, which is a complex number. Have this function regenerate a fresh plane and empty the ```fs``` list as before, but then apply the function ```julia``` to the plane with the updated argument ```c``` analogously to the initialization. (The ```zoom``` and ```apply``` methods should work the same as before.)
    * Find a way to test that the resulting output is correct. (Hint: What happens when ```c=0```?)
    * Create a new method ```toCSV(self, filename)``` that exports the transformed plane of integers to a ```.csv``` file in a sensible way. Make sure that the file stores all the needed parameters for the plane, including the value of ```c``` and the current zoom settings (```xmin```, etc.).
    * Create a new method ```fromCSV(self, filename)``` that imports a ```.csv``` file previously exported by the class. This method should reset the plane parameters to match the settings in the file, and refresh the plane array to the values stored in the ```.csv``` file directly.
1. In a module ```test_cplane-np-hw.py``` write suitable test functions to verify that you accomplished your goals correctly.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
