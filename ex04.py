def rfinal(nfs):

    return (

        [x for x in nfs if x[1] >= 5 and x[2] >= 75],
        [x for x in nfs if x[1] < 5 and x[2] >= 75],
        [x for x in nfs if x[1] >= 5 and x[2] < 75],
        [x for x in nfs if x[1] < 5 and x[2] < 75]

    )