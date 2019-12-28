def get_L_ranges(iL):
    """
    Appends the "from" and "to" positions whenever integers 
    in iterable `iL` are found that aren't consecutive.
    
    e.g. get_L_ranges([0, 1, 2, 4, 5, 6]) -> [(0, 3), (4, 7)]
    """
    L = []
    from_ = None
    to = None
    
    for x in iL:
        if from_ is None:
            from_ = x
            to = x
            
        elif x != to+1:
            #print x, from_
            L.append((from_, to+1))
            from_ = x # CHECK ME!
            to = x # CHECK ME!
            
        else:
            to = x
    
    if to != None:
        L.append((from_, to+1))
    #print L
    return L


#print get_L_ranges([0, 1, 2, 4, 5, 6])
