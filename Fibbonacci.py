parents, babies = (1, 1)
while babies < 1000000:
    print 'This generation has {0} babies'.format(babies)
    print parents
    print babies
    parents, babies = (babies, parents + babies)
