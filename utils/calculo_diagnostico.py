


def determinar_diagnostico(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30):

    diagnostico = "-"


    if t1 < 29:
        trastorno_t1 = True
    if t2 < 29:
        trastorno_t2 = True
    if t3 < 28:
        trastorno_t3 = True
    if t4 < 31:
        trastorno_t4 = True
    if t5 < 24:
        trastorno_t5 = True
    if t6 < 23:
        trastorno_t6 = True
    if t7 < 20:
        trastorno_t7 = True
    if t8 < 22:
        trastorno_t8 = True
    if t9 < 15:
        trastorno_t9 = True
    if t10 < 5:
        trastorno_t10 = True
    if t11 < 19:
        trastorno_t11 = True
    if t12 < 30:
        trastorno_t12 = True
    if t13 < 31:
        trastorno_t13 = True
    if t14 < 26:
        trastorno_t14 = True
    if t15 < 29:
        trastorno_t15 = True
    if t16 < 19:
        trastorno_t16 = True
    if t17 < 7:
        trastorno_t17 = True
    if t18 < 9:
        trastorno_t18 = True
    if t19 < 7:
        trastorno_t19 = True
    if t20 <7:
        trastorno_t20 = True
    if t21 < 28:
        trastorno_t21 = True
    if t22 < 27:
        trastorno_t22 = True
    if t23 < 27:
        trastorno_t23 = True
    if t24 < 25:
        trastorno_t24 = True
    if t25 < 24:
        trastorno_t25 = True
    if t26 < 15:
        trastorno_t26 = True
    if t27 < 16:
        trastorno_t27 = True
    if t28 < 31:
        trastorno_t28 = True
    if t29 < 4:
        trastorno_t29 = True
    if t30 < 3:
        trastorno_t30 = True


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