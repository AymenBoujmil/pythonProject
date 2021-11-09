class Game:

    def up(self, liste):
        liste1=list(liste)
        pos = liste.index(0)
        if pos < 6:
            temp = liste[pos+3]
            liste1[pos] = temp
            liste1[pos+3] = 0
        return liste1

    def down(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos > 2:
            temp = liste[pos - 3]
            liste1[pos] = temp
            liste1[pos - 3] = 0
        return liste1

    def right(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 0:
            temp = liste[pos - 1]
            liste1[pos] = temp
            liste1[pos - 1] = 0
        return liste1

    def left(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 2:
            temp = liste[pos + 1]
            liste1[pos] = temp
            liste1[pos + 1] = 0
        return liste1


class DFS:
    init_state = [7,2,4,5,0,6,8,3,1]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def listToString(self,list1):

        str1 = ""

        for ele in list1:
            str1 += str(ele)

        return str1

    def parcours(self):
        game = Game()
        open = list()
        open.append(self.init_state)
        closed = {}
        i=0
        while len(open) != 0 and self.listToString(self.final_state) not in closed:
            temp = list(open)

            i=i+1

            #print("________________")
            #print(i)

            #print('open :',open)
            #print('closed :',closed)
            l=open.pop(0)
            closed[self.listToString(l)] = '1'

            j=0
            if self.listToString(game.right(l)) not in closed:
                open.insert(j, game.right(l))
                j = j + 1
            if self.listToString(game.up(l)) not in closed:
                open.insert(j,game.up(l))
                j=j+1
                #print(game.up(l))
            if self.listToString(game.down(l)) not in closed:
                open.insert(j,game.down(l))
                j=j+1

                #print(game.down(l))
            if self.listToString(game.right(l)) not in closed:
                open.insert(j,game.right(l))
                j=j+1

                #print(game.right(l))
            if self.listToString(game.left(l)) not in closed:
                open.insert(j,game.left(l))




                   # print(game.left(l))
       # print(open)
        print(closed )
        print(i)


def main():

    dfs = DFS()
    dfs.parcours()

if __name__ == '__main__':
    main()