parent('Edward VII','George V'). 
parent('Victoria','Edward VII'). 
parent('Alexandra','George V'). 
parent('George VI','Elizabeth II'). 
parent('George V','George VI'). 
parent('William','George'). 
parent('William','Charlotte'). 
parent('Kate','George'). 
parent('Kate','Charlotte'). 
grandparent('x','y'):-parent('x','z'),parent('z','y'). 
male('George V'). 
male('George VI'). 
male('Edward VII'). 
female('Alexandra'). 
female('Victoria').  
father('x','y'):-male('x'),parent('x','y').  