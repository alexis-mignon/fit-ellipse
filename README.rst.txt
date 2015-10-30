==================
2D Ellipse fitting
==================

Fits an ellipse to a set of points (x_i, y_i) using the canonical
representation:

.. math::
  a  x^2 + b  x  y + c  y^2 + d  x + e  y + f = 0

Provided features
-----------------

The module provides several function related to ellipses:

`fit_ellipse`:
  fits an ellipse from a set of points and return the parameters
  of the canonical representation (see above)
        
`get_parameters`:
  converts canonical parameters into intuitive representation i.e.
  major and minor radii

let a_ be the vector a_ = [a, b, c, d, e, f]'
    Let D be the (N x 6) design matrix:
        D = [z_1 z_2 ... z_n]'
        
        where 
        
        z_i = [ x_i^2, x_i * y_i, y_i^2, x_i, y_i, 1 ]'
    
    We want to minimize
    
        E = \sum_i (a_' * z_i)^2 = || D * a_ ||^2 = a_' * S * a
        
        where 
        
        S = D' * D
    If equation (1) corresponds to an ellipse we must have:
        
        4 * a * c - b^2 > 0
        
    Since equation (1) is unique up to a scaling factor we can impose:
        
        4 * a * c - b^2 = 1
        
    which can be written in matrix form as:
        
        a_' * C * a_ = 1
        
        with
        
        ::
        
            C = | 0 0  2 0 0 0 |
                | 0 -1 0 0 0 0 |
                | 2 0  0 0 0 0 |
                | 0 0  0 0 0 0 |
                | 0 0  0 0 0 0 |
                | 0 0  0 0 0 0 |
    So the problem reduces to:
        
        a_ = argmin a_' S a_
        s.t.                        (2)
            a_' * C * a_ = 1
        
    which is equivalent to solving:
        
        S a_ = l * C * a_           (3)
        
    where l is a Lagrange multiplier.
    
    Equation (2) is just a generalized eigen value problem. And the solution
    to (1) is the eigen vector corresponding to the smallest positive eigen
    value of (2).
    
    It can be prooved that (3) has 2 negative eigen values and one positive.
    The biggest eigen value the corresponds to the solution.
    
    Since C has negative eigen values solvers in scipy/numpy are not able
    to perform the eigen decomposition. To solve (2) we reduce the problem
    to a 3x3 eigen value problem for wich we can solve the problem
    analytically. For that, we split S and C into 3x3 blocks.    
    
    Let's define:
    
    ::
        
        S = | A  B |
            | B' E |
        
        C = | F  0 |
            | 0  0 |
            
        a_ = [x' y']'
        
    Rewritting (3) we get:
        
        A * x + B * y = l * F * x
        B'* x + E * y = 0
        
    which gives:
        
        y = - E^(-1) * B' * x
        (A - B * E^(-1) * B') * x = l * F * x (4)
    
    Equation (4) is a 3x3 eigen value problem that we can solve analytically.
    
    :Notes:
        Detailed explanations can be found in:
            
            *Direct Least square fitting of Ellipses*. A. Fitzgibbon, M. Pilu,
            and R. B. Fisher. Pattern Analysis and Machine Intelligence. 1999
    :Author: Alexis Mignon (c) 2012
    :E-mail: alexis.mignon@gmail.com
        
