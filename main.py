


if __name__ == '__main__':

    liste = [2, 7, "texte", 4]

    # Gestion LBYL

    # for i in liste:
    #     if not str(i).isdigit():
    #         liste.remove(i)
    # total = sum(liste)
    # print(total)


    # Gestion EAFP

    # try:
    #     sum(liste)
    # except TypeError as e:
    #     total = 0
    #     print(total, e)
    #

    # Gestion hybride?
    try:
        sum(liste)
    except TypeError:
        for i in liste:
            if not str(i).isdigit():
                liste.remove(i)
        print("la somme des integer de la liste est:", sum(liste))
