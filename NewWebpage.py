#! /usr/bin/python
import cgitb; cgitb.enable()
from flask import Flask
from flask import render_template

TheContentHeader = 'Content-type: text/html\n\n'
TheHTMLHeader = '<html><head>'
TheBeginningOfBody = '</head><body>'
TheHTMLFooter = '</body></html>'

app = Flask(__name__)

import cgi
@app.route("/")
def mainpage():
    return render_template("Pokemon.html")

info = cgi.FieldStorage()

@app.route("/search")
def main():
    print TheContentHeader + TheHTMLHeader
    print '<title>Information!</title>'
    print TheBeginningOfBody
    if info['SearchType'].value == 'basic':
        if info['SearchBy'].value == 'ID':
            if 'ID' not in info:
                print '<center><font size=7>Fill in the Blank.</center></font>'
            elif info['ID'] > 649 or info['ID'] == 0:
                print '<center><font size=7>There are not that many pokemon.</center></font>'
            else:
                a = open('data.txt').read().split('\n')
                if info['ID'] < 387:
                    n = a[int(info['ID'].value)]
                n = n.split(',')
                print '<table border=1><font size=8>' + '<tr><td bgcolor=FF99FF><b>ID:</b></td><td bgcolor=6699FF>' + str(n[0])+'</td></tr>'
                print '<tr><td bgcolor=33FF99>' + '<b>Name:</b></td><td bgcolor=FFFF00>' + str(n[1]) + '</td></tr>'
                print '<tr><td bgcolor=FF99FF>' + '<b>HP:</b></td><td bgcolor=6699FF>' + str(n[2]) + '</td></tr>'
                print '<tr><td bgcolor=33FF99>' + '<b>Attack:</b></td><td bgcolor=FFFF00>' + str(n[3]) +'</td></tr>'
                print '<tr><td bgcolor=FF99FF>' + '<b>Defense:</b></td><td bgcolor=6699FF>' + str(n[4])+'</td></tr>'
                print '<tr><td bgcolor=33FF99>' + '<b>Special Attack:</b></td><td bgcolor=FFFF00>' + str(n[5])+'</td></tr>'
                print '<tr><td bgcolor=FF99FF>' + '<b>Special Defense:</b></td><td bgcolor=6699FF>' + str(n[6])+'</td></tr>'
                print '<tr><td bgcolor=33FF99>' + '<b>Speed:</b></td><td bgcolor=FFFF00>' + str(n[7])+'</td></tr>'
                print '<tr><td bgcolor=FF99FF>'+ '<b>Total:</b></td><td bgcolor=6699FF>' + str(n[8])+'</td></tr>'
                print '</table>'
                print "<center><img src=pkmn_ico/"+str(n[0])+'.gif></center>'
        else:
            if 'PokemonName' not in info:
                print '<center><font size=7>Fill in the Blank.</center></font>'
            else:
                a = open('data.txt').read().split('\n')
                del a[0]
                z = 0
                p = 0
                while z < len(a):
                    if a[z] == "":
                        del a[z]
                    else:
                        z += 1      
                for n in a:
                        n = n.split(',')
                        if n[1].upper() == info['PokemonName'].value.upper():
                            print '<table border=1><font size=8>' + '<tr><td bgcolor=FF99FF><b>ID:</b></td><td bgcolor=CC66FF>' + str(n[0])+'</td></tr>'
                            print '<tr><td bgcolor=6666FF>' + '<b>Name:</b></td><td bgcolor=6699FF>' + str(n[1])+'</td></tr>'
                            print '<tr><td bgcolor=FF99FF>' + '<b>HP:</b></td><td bgcolor=CC66FF>' + str(n[2])+'</td></tr>'
                            print '<tr><td bgcolor=6666FF>' + '<b>Attack:</b></td><td bgcolor=6699FF>' + str(n[3])+'</td></tr>'
                            print '<tr><td bgcolor=FF99FF>' + '<b>Defense:</b></td><td bgcolor=CC66FF>' + str(n[4])+'</td></tr>'
                            print '<tr><td bgcolor=6666FF>' + '<b>Special Attack:</b></td><td bgcolor=6699FF>' + str(n[5])+'</td></tr>'
                            print '<tr><td bgcolor=FF99FF>' + '<b>Special Defense:</b></td><td bgcolor=CC66FF>' + str(n[6])+'</td></tr>'
                            print '<tr><td bgcolor=6666FF>' + '<b>Speed:</b></td><td bgcolor=6699FF>' + str(n[7])+'</td></tr>'
                            print '<tr><td bgcolor=FF99FF>' + '<b>Total:</b></td><td bgcolor=CC66FF>' + str(n[8])+'</td></tr>'
                            print '</table>'
                            print "<center><img src=pkmn_ico/"+str(n[0])+'.gif></center>'
                            p = 1
                if p == 0:
                    print '<center><font size=7>There is no such Pokemon.</center></font>'
    else:
        D = {}
        a = open('data.txt').read().split('\n')
        del a [0]
        if info['type1'].value == 'N/A' and info['type2'].value == 'N/A':
            pass
        else:
            if info['type1'].value == info['type2'].value:
                z = info['type1'].value
                j = 0
            elif info['type1'].value == 'N/A':
                z = info['type2'].value
                j = 0
            elif info['type2'].value == 'N/A':
                z = info['type1'].value
                j = 0
            else:
                z = info['type1'].value
                j = info['type2'].value
            b = 0
            if j == 0:
                while b < len(a):
                    c = a[b].split(',')
                    if c[9] != z:
                        del a[b]
                    else:
                        b += 1
            else:
                while b < len(a):
                    c = a[b].split(',')
                    if (c[9] != z or c[10] != j) and (c[9] != j or  c[10] != z):
                        del a[b]
                    else:
                        b += 1
        if info['sort'].value == 'Total':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[8]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=66CC00>TOTAL</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=009966>'+str(x) + ':</td><td bgcolor=FFCCCC>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'ID':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[0]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=33CCCC>ID NUMBER</b></font>'
            while x < P:
                if str(x) in E:
                        print '<table border=1><tr><td bgcolor=99FF99>' + str(x) + ':</td><td bgcolor=FF99CC>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'Speed':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[7]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=660099>SPEED</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=FF9933>'+str(x) + ':</td><td bgcolor=33CC66>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'Special Defense':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[6]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=3366FF>SPECIAL DEFENSE</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=FFCCFF>'+str(x) + ':</td><td bgcolor=FF9900>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'Special Attack':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[5]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=33FF99>SPECIAL ATTACK</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=99FF99>'+str(x) + ':</td><td bgcolor=66CCFF>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'Defense':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[4]
            P = 0      
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=33FF99>DEFENSE</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=FFCCCC>'+str(x) + ':</td><td bgcolor=FFCC66>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1 
        if info['sort'].value == 'Attack':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[3]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=CC0000>ATTACK</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=CCCCFF>' +str(x) + ':</td><td bgcolor=CC99FF>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1
        if info['sort'].value == 'HP':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[2]
            P = 0     
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=0066CC>HP</b></font>'
            while x < P:
                if str(x) in E:
                        print '<table border=1><tr><td bgcolor=FF6633>' + str(x) + ':</td><td bgcolor=FF9933>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1
        if info['sort'].value == 'Height':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[11]
            P = 0     
            E ={}
            for n in D:
                a = D[n].split("'")
                a = (int(a[0]) * 12) + int(a[1][0]) + int(a[1][1])
                D[n] = a      
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]        
            for x in E:
                if x > P:
                    P = x
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=FFCCFF>HEIGHT</b></font>'
            while x < P:
                if x in E:
                        print '<table border=1><tr><td bgcolor=CCFF66>'+ str(x) + 'inches' + ':</td><td bgcolor=FFFF66>'
                        for n in E[x]:
                            if n != E[x][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1
        if info['sort'].value == 'Weight':
            for n in a:
                 n = n.split(',')
                 D[n[1]] = n[12]
            P = 0      
            E ={}
            for n in D:
                L = D[n]
                if L in E:
                    E[L].append(n)
                else:
                    E[L] = [n]       
            for x in E:
                if int(x) > P:
                    P = int(x)
            x = 0
            print '<font size=5><b>SORTED BY: </font><font size=5 color=FF3399>WEIGHT</b></font>'
            while x < P:
                if str(x) in E:
                        print  '<table border=1><tr><td bgcolor=99FFFF>'+str(x) + 'lbs:' + '</td><td bgcolor=99CCFF>'
                        for n in E[str(x)]:
                            if n != E[str(x)][-1]:
                                print n + ', '
                            else:
                                print n
                        print'</td></tr>'
                        print '</table>'
                x += 1                 
    print TheHTMLFooter

if __name__ == "__main__":
    app.run(debug=True)
else: main()
