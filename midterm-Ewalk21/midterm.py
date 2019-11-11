#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import cplane_np_midterm
import sys
import cmath
#import csv

from cplane_np_midterm import ArrayComplexPlane

###
# Name: Evan A Walker
# Student ID: 001932978
# Email: walke208@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Midterm
###

def f(z):
    """
    f(z) is a complex valued polynomial
    Args:
        z (complex): complex number for f(z) to evaluate at
    Returns:
        f(z) (complex): the output of the polynomial
    """
    return 35*(z**9) - 180*(z**7) + 378*(z**5) - 420*(z**3) + 315*z

def fprime(z):
    """
    fprime(z) is a complex valued polynomial and is the derivative of f(z)
    Args:
        z (complex): complex number for fprime(z) to evaluate at
    Returns:
        fprime(z) (complex): the output of the derivative polynomial
    """
    return 35*9*(z**8) - 180*7*(z**6) + 378*5*(z**4) - 420*3*(z**2) + 315

def update(z):
    """
    computes z(n+1) from the Newton-Raphson sequence fiven z(n)
    Args:
        z (complex): complex number z(n) used to find z(n+1)
    Returns:
        update(z) (complex): the next term of the Newton-Raphson sequence
    """
    if fprime(z) == 0:
        return 0
    return z - f(z)/fprime(z)

class NewtonRaphson(ArrayComplexPlane):
    dx = 0
    dy = 0
    e = 0
    znA = []
    nA = []
    rootCount = 0
    roots = []
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        ArrayComplexPlane.__init__(self,xmin, xmax, xlen, ymin, ymax, ylen)
        self.dx = (abs(self.xmax) + abs(self.xmin))/self.xlen
        self.dy = (abs(self.ymax) + abs(self.ymin))/self.ylen
        self.e = np.sqrt(self.dx**2 + self.dy**2)
        self.vectRepUpdate()
        self.vectRootFinder()

    def getDx(self):
        """
        getter fxn for dx
        Args:
            None:
        Returns:
            dx (float): private var dx
        """
        return self.dx

    def getDy(self):
        """
        getter fxn for dy
        Args:
            None:
        Returns:
            dy (float): private var dy
        """
        return self.dy

    def getE(self):
        """
        getter fxn for e
        Args:
            None:
        Returns:
            e (float): private var e
        """
        return self.e

    def getznA(self):
        """
        getter fxn for znA
        Args:
            None:
        Returns:
            znA (array): private var znA
        """
        return self.znA

    def getnA(self):
        """
        getter fxn for nA
        Args:
            None:
        Returns:
            nA (array): private var nA
        """
        return self.nA

    def getRootCount(self):
        """
        getter fxn for rootCount
        Args:
            None:
        Returns:
            rootCount (int): private var rootCount
        """
        return self.rootCount

    def getRoots(self):
        """
        getter fxn for roots
        Args:
            None:
        Returns:
            roots (array): private var roots
        """
        return self.roots

    def repUpdate(self, z, max=1000):
        """
        repeatedly applies the update function until the distance between
        two consecutive points in the Newton-Raphson method are at least epsilon away
        Args:
            z (complex): complex number for fprime(z) to evaluate at
            max (int),(optional): in case the sequence is not convergent,
                                  repupdate will not iterate more than the max argument, default value 1000
        Returns: (as a tuple)(zn,n)
            zn (complex): the first point in the Newton-Raphson sequence where
                          the distance between it and the previous point is less than epsilon
            n (int): number of iterations of update until zn was reached
        """
        zn = update(z)
        n = 1
        while (abs(zn - z) > self.e):
            z = zn
            zn = update(zn)
            if zn == 0: #or n == max:
                break
            n += 1
        return (zn,n)

    def vectRepUpdate(self):
        """
        vectorizes the repUpdate function using numpy, then applies the vectorized function to self.plane
        to set the private vars znA and nA as lists. now we can think of each point in znA as the convergence
        of the Newton-Raphson method at that point, or as the approximated root of f(z) at z in self.plane
        Args:
            None:
        Returns:
            None:
        """
        vf = np.vectorize(self.repUpdate)
        self.znA, self.nA = vf(self.plane)

    def vectRootFinder(self):
        """
        vectorizes the rootFinder function and applies it to all values of znA, rootFinder takes in one parameter z,
        then truncates it and adds it to self.roots if z is not already in self.roots, then returns an assigned integer for
        the specific z value
        Args:
            None:
        Returns:
            None:
        """
        rf = np.vectorize(self.rootFinder)
        self.znA = rf(self.znA)

    def rootFinder(self,z):
        """
        truncates z to a specific precision given by the mesh spacing and adds it self.roots if it is not already in self.roots.
        then returns the index of z in self.roots, which acts like assigning each root to an integer
        Args:
            z (complex): a complex value, intended to be taken from self.znA
        Returns:
            roots.index(z) (int): index of z in self.roots
        """
        z = self.trunc(z)
        if z not in self.roots:
            self.roots.append(z)
            self.rootCount += 1
        return self.roots.index(z)

    def trunc(self,z):
        """
        takes a complex value z and truncates both the real and imaginary part to a specific precision given by the
        mesh spacing.
        Args:
            z (complex): a complex value, intended to be taken from self.znA
        Returns:
            trunc(z) (complex): truncated complex value z
        """
        prec = int(10**(np.round_(abs(np.log10(self.e))+.5)))
        flr = int(np.round_(np.floor(abs(z.real*prec))))
        flri = int(np.round_(np.floor(abs(z.imag*prec))))
        if z.real < 0 and z.imag < 0:
            return (-1)*flr/prec - (flri/prec)*1j
        elif z.real < 0:
            return (-1)*flr/prec + (flri/prec)*1j
        elif z.imag < 0:
            return flr/prec - (flri/prec)*1j
        else:
            return flr/prec + (flri/prec)*1j

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function changes the plane size using given input values,
        and re-applys all f in self.fs. this is achieved by calling setPlane and
        applyAllF, see also these fxns
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        self.dx = (abs(self.xmax) + abs(self.xmin))/self.xlen
        self.dy = (abs(self.ymax) + abs(self.ymin))/self.ylen
        self.e = np.sqrt(self.dx**2 + self.dy**2)
        self.vectRepUpdate()
        self.vectRootFinder()

    def show(self):
        """
        Uses matplotlib to plot self.znA using imshow. Where each root in znA has been transformed to a specific int.
        Args:
            None:
        Returns:
            None:
        """
        plt.figure(figsize=(12, 12))
        plt.imshow(self.znA, cmap=plt.cm.jet)   #colormap = inferno,magma,plasma,viridis,gist_rainbow
        #plt.scatter(self.roots)
        plt.colorbar()

        plt.xticks(())
        plt.yticks(())
        plt.show()







