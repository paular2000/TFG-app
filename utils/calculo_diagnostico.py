


def determinar_diagnostico(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30):

    


    trastorno_t1 = t1 < 29
    trastorno_t2 = t2 < 29
    trastorno_t3 = t3 < 28
    trastorno_t4 = t4 < 31
    trastorno_t5 = t5 < 24
    trastorno_t6 = t6 < 23
    trastorno_t7 = t7 < 20
    trastorno_t8 = t8 < 22
    trastorno_t9 = t9 < 15
    trastorno_t10 = t10 < 5
    trastorno_t11 = t11 < 19
    trastorno_t12 = t12 < 30
    trastorno_t13 = t13 < 31
    trastorno_t14 = t14 < 26
    trastorno_t15 = t15 < 29
    trastorno_t16 = t16 < 19
    trastorno_t17 = t17 < 7
    trastorno_t18 = t18 < 9
    trastorno_t19 = t19 < 7
    trastorno_t20 = t20 < 7
    trastorno_t21 = t21 < 28
    trastorno_t22 = t22 < 27
    trastorno_t23 = t23 < 27
    trastorno_t24 = t24 < 25
    trastorno_t25 = t25 < 24
    trastorno_t26 = t26 < 15
    trastorno_t27 = t27 < 16
    trastorno_t28 = t28 < 31
    trastorno_t29 = t29 < 4
    trastorno_t30 = t30 < 3

    diagnostico = "-"

    if (trastorno_t6 and trastorno_t7 and trastorno_t8 and trastorno_t9 and trastorno_t3 
        and trastorno_t15 and trastorno_t23 and trastorno_t21 and trastorno_t22 and trastorno_t24 and trastorno_t25):

        diagnostico = "Trastorno semántico"

    elif (trastorno_t6 and trastorno_t7 and trastorno_t8 and trastorno_t9 and trastorno_t10 
        and trastorno_t21 and trastorno_t22 and trastorno_t23 and trastorno_t24 and trastorno_t25
        and trastorno_t1 and trastorno_t2 and trastorno_t3 and trastorno_t4 and trastorno_t5):

        diagnostico = "Anomia léxica"
    elif (trastorno_t4 and trastorno_t5 and trastorno_t6 and trastorno_t7 and trastorno_t8 and trastorno_t9 and trastorno_t10
          and trastorno_t13 and trastorno_t14 and trastorno_t21 and trastorno_t22 and trastorno_t23 and trastorno_t24 and trastorno_t25
          and trastorno_t1 and trastorno_t2 and trastorno_t3):
        
        diagnostico = "Anomia fonológica"


    return diagnostico