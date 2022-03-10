import search
import eqparser
import helperfns

s=input("eq>")
v=input("var>")
p = eqparser.parse(s)
pbm = search.equationSolver(initial=p,variable=v)

print(pbm.astar_search(pbm))
