import sys
inputfile = sys.argv[1]
dataFile = open(inputfile).read()
liste = [i.split() for i in dataFile.split("\n")]
for i in liste:
    print(' '.join(i))
print("Your score is:0")
def fibonacci(n):
 a = 1
 b = 1
 fibonacci = [a, b]
 for i in range(n-2):
    a, b = b, a + b
    fibonacci.append(b)
 return fibonacci[-1]
def number_of_lists(x):
 f = lambda x: 0 if not isinstance(x, list) else (f(x[0]) + f(x[1:]) if len(x) else 1)
 m=f(x)-1
 return m
score=0
r=True
while r:
    kordinatlar = []
    p = number_of_lists(liste) - 1
    m = len(liste[0][:]) - 1
    d = input("Please enter a row and a column: " ).split(" ")
    if len(d) != 2:
        print("Please enter 2 integers")
    else:
     a = int(d[0]) - 1
     b = int(d[1]) - 1
     if a>=(p+1) or b>=(m+1) :
        print("Please enter correct row and column!")
     elif liste[a][b]==" ":
        print("Please enter a correct size!")
     else:
      e = True
      while e:
        p = number_of_lists(liste) - 1
        m = len(liste[0][:]) - 1
        if a <= p and b <= m:
            c = liste[a][b]
            if (a - 1) <= p and b <= m and (a - 1) >= 0 and b >= 0:
                if c == liste[a - 1][b]:
                    liste[a - 1][b] = " "
                    kordinatlar.append([(a - 1), b])
                    if liste[a][b] == c:
                        liste[a][b] = " "
                        kordinatlar.append([(a), (b)])
            if (a + 1) <= p and b <= m and (a + 1) >= 0 and b >= 0:
                if c == liste[a + 1][b]:
                    liste[a + 1][b] = " "
                    kordinatlar.append([(a + 1), b])
                    if liste[a][b] == c:
                        liste[a][b] = " "
                        kordinatlar.append([(a), (b)])
            if a <= p and (b - 1) <= m and a >= 0 and (b - 1) >= 0:
                if c == liste[a][b - 1]:
                    liste[a][b - 1] = " "
                    kordinatlar.append([a, (b - 1)])
                    if liste[a][b] == c:
                        liste[a][b] = " "
                        kordinatlar.append([(a), (b)])
            if a <= p and (b + 1) <= m and a >= 0 and (b + 1) >= 0:
                if c == liste[a][b + 1]:
                    liste[a][b + 1] = " "
                    kordinatlar.append([a, (b + 1)])
                    if liste[a][b] == c:
                        liste[a][b] = " "
                        kordinatlar.append([(a), (b)])
            if a < 0 or (b + 1) < 0 or a < 0 or (b - 1) < 0 or (a + 1) < 0 or b < 0 or (a - 1) < 0 or b < 0:
                e = False
            if a > p or (b + 1) > m or a > p or (b - 1) > m or (a + 1) > p or b > m or (a - 1) > p or b > m:
                e = False
            if a <= p and (b + 1) <= m and a <= p and (b - 1) <= m and (a + 1) <= p and b <= m and (
                        a - 1) <= p and b <= m:
                if c != liste[a - 1][b] and c != liste[a + 1][b] and c != liste[a][b + 1] and c != liste[a][b - 1]:
                    e = False
      for s in kordinatlar:
        b = True
        while b:
            u = int(s[0])
            w = int(s[1])
            if (u - 1) <= p and w <= m and (u - 1) >= 0 and w >= 0:
                if c == liste[u - 1][w]:
                    liste[u - 1][w] = " "
                    kordinatlar.append([(u - 1), w])
            if (u + 1) <= p and w <= m and (u + 1) >= 0 and w >= 0:
                if c == liste[u + 1][w]:
                    liste[u + 1][w] = " "
                    kordinatlar.append([(u + 1), w])
            if u <= p and (w + 1) <= m and u >= 0 and (w + 1) >= 0:
                if c == liste[u][w + 1]:
                    liste[u][w + 1] = " "
                    kordinatlar.append([u, w + 1])
            if u <= p and (w - 1) <= m and u >= 0 and (w - 1) >= 0:
                if c == liste[u][w - 1]:
                    liste[u][w - 1] = " "
                    kordinatlar.append([u, w - 1])
            if u < 0 or (w + 1) < 0 or u < 0 or (w - 1) < 0 or (u + 1) < 0 or w < 0 or (u - 1) < 0 or w < 0:
                b = False
            if u > p or (w + 1) > m or u > p or (w - 1) > m or (u + 1) > p or w > m or (u - 1) > p or w > m:
                b = False
            if u <= p and (w + 1) <= m and u <= p and (w - 1) <= m and (u + 1) <= p and w <= m and (
                        u - 1) <= p and w <= m:
                if c != liste[u - 1][w] and c != liste[u + 1][w] and c != liste[u][w + 1] and c != liste[u][w - 1]:
                    b = False
      n=len(kordinatlar)
      # sildirme bitti
      p = number_of_lists(liste) - 1
      m = len(liste[0][:]) - 1
      sildirme = []
      for a in range(p - 1, -1, -1):
        for b in range(0, m + 1):
            sildirme.append([a, b])
      for k in sildirme:
        a = k[0]
        b = k[1]
        d = liste[a][b]
        if d != " " and liste[a + 1][b] == " " and (a + 2) <= p and liste[a + 2][b] != " ":
            liste[a + 1][b] = d
            liste[a][b] = " "
        elif d != " " and (a + 1) == p and liste[a + 1][b] == " ":
            liste[p][b] = d
            liste[a][b] = " "
        elif d != " " and liste[a + 1][b] == " " and (a + 2) <= p and liste[a + 2][b] == " ":
            for h in range(p, a + 1, -1):
                if liste[h][b] == " ":
                    liste[h][b] = d
                    liste[a][b] = " "
                    break

      # indirme bitti
      for p in range(len(liste)):
       for a in liste:
        t = []
        for b in a:
            if b == " ":
                t.append(1)
        if len(t) == (m + 1):
            liste.remove(a)
      # satır sildirme bitti
      j = len(liste[0])
      son = []
      z=True
      while z:
       for k in range(len(liste[0])-1,-1,-1):
        a = []
        bas=[]
        o = len(liste[0])
        for i in range(len(liste)):
                if liste[i][k] == " ":
                    a.append([i, k])
                    if len(a) == len(liste):
                        for b in a:
                            u = b[0]
                            w = b[1]
                            del liste[u][w]
                        son.append(w)
                    if len(a) != len(liste):
                        z=False


      game_over = []
      for x in range(len(liste)):
         for y in range(len(liste[0])):
             if liste[x][y] != " ":
                 d = liste[x][y]
                 if x - 1 >= 0:
                     if liste[x - 1][y] == d:
                         game_over.append(1)
                 if x + 1 <= (len(liste) - 1):
                     if liste[x + 1][y] == d:
                         game_over.append(1)
                 if y - 1 >= 0:
                     if liste[x][y - 1] == d:
                         game_over.append(1)
                 if y + 1 <= (len(liste[0]) - 1):
                     if liste[x][y + 1] == d:
                         game_over.append(1)
      if len(game_over) == 0:
         c = int(c)
         for i in liste:
             print(' '.join(i))
         if n != 0:
             score += c * fibonacci(n)
         print("YOUR TOTAL SCORE İS :", score)
         print("*****GAME OVER*****")
         r=False
      else:
         c=int(c)
         for i in liste:
          print(' '.join(i))
         if n !=0:
            score+=c*fibonacci(n)
         print("your score is :",score)