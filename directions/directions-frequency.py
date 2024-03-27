from pyconcepticon import Concepticon
from csvw import UnicodeDictReader, UnicodeWriter

# example
# concepts = [
#         ["ARM", "HAND"],
#         ["FOOT", "LEG"]
#         ]

with UnicodeDictReader("bo-colexifications.tsv", delimiter="\t") as reader:
    concepts = []
    for row in reader:
        concepts += [row]

graph = {}
for a, b in concepts:
    graph[a, b] = 0

con = Concepticon()
cl = con.conceptlists["List-2023-1308"]
id2cgl = {c.id: c.concepticon_gloss for c in cl.concepts.values()}
for c in cl.concepts.values():
    gloss_a = c.concepticon_gloss
    for itm in c.attributes["target_concepts"]:
        gloss_b = id2cgl[itm["ID"]]
        if (gloss_a, gloss_b) in graph:
            graph[gloss_a, gloss_b] = itm["AffixLngs"]
table = [["Source", "Target", "Count"]] + [[a, b, c] for (a, b), c in graph.items()]
with UnicodeWriter("directions.tsv", delimiter="\t") as writer:
    for row in table:
        writer.writerow(row)