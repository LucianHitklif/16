cruinp = input("Агенты ЦРУ: ")
mi6inp = input("Агенты МИ-6: ")
kgbinp = input("Агенты КГБ: ")

cru_set = set(cruinp.split())
mi6_set = set(mi6inp.split())
kgb_set = set(kgbinp.split())

double_ag = cru_set & mi6_set
double_not_kgb = double_ag - kgb_set

sorted_res = sorted(double_not_kgb, reverse=True)

if sorted_res:
    print("".join(sorted_res))
else:
    print()
