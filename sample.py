from QPclasses import Engrave
from QPclasses import Create
CourseObjectives=["To understand the basics of algorithmic notion","To understand and apply the algorithm analysis techniques.","To critically analyze the efficiency of alternative algorithmic solutions for the same problem","To understand different algorithm design techniques.","To understand the limitations of Algorithmic power."]
#Engrave.partA()
CourseOutcomes=["C213.1","To analyze the time and space complexities of a given problem using suitable mathematical techniques","C213.2","To design efficient algorithms for a given problem using appropriate algorithmic paradigm","C213.3","The student will be able to critically analyze different algorithm design techniques for the same problem using dynamic programming and greedy technique","C213.4","The student will be able to improvise the solutions for a given problem using Iterative Improvement","C213.5","The student will be familiarized with the limitations of algorithmic solutions to various problems."]
cout_code=["C213.1","C213.2","C213.3","C213.4","C213.5"]
cout=["To analyze the time and space complexities of a given problem using suitable mathematical techniques","To design efficient algorithms for a given problem using appropriate algorithmic paradigm","The student will be able to critically analyze different algorithm design techniques for the same problem using dynamic programming and greedy technique","The student will be able to improvise the solutions for a given problem using Iterative Improvement","The student will be familiarized with the limitations of algorithmic solutions to various problems."]
l=["testpassinglist"]
BTlvl=["K1","K2","K3","K4","K5"]

Engrave.header(0,1,4,2022,7,"CS 8451","Design and Analysis of Algorithm",0,0,0,2,4)
Engrave.courseObjectives(CourseObjectives)
Engrave.courseOutcomes(cout_code,cout)
Engrave.partc_is_available(1)
partA=["Write the charcteristics~~$CIT Logo Simple - PNG.png~~of an algoritm.~~$logo1.png~~","How to measure algorithm running time?","Write the non-recursive algorithm to find the largest element in the list of numbers.","What is mean by Algorithm Visualization?","Define recurrance relation."]
Engrave.partA(partA,cout_code,BTlvl,cout_code)
partb6a=["Write the charcteristics~~$CIT Logo Simple - PNG.png~~of an algoritm.~~$logo1.png~~"]
Engrave.PartB6a(partb6a,cout_code,BTlvl,cout_code,cout_code)
partb6b=["Write the charcteristics~~$CIT Logo Simple - PNG.png~~of an algoritm.~~$logo1.png~~","Write the charcteristics~~$CIT Logo Simple - PNG.png~~of an algoritm.~~$logo1.png~~"]
Engrave.PartB6b(partb6b,cout_code,BTlvl,cout_code,["10","2"])
partb7a=["Explain Asymptomatic Notations"]
Engrave.PartB7a(partb7a,cout_code,BTlvl,cout_code,["12"])
partb7b=["Illustrate mathematical Analysis on recursive Algorithms"]
Engrave.PartB7b(partb7b,cout_code,BTlvl,cout_code,["12"])

Engrave.PartB8a(CourseObjectives,cout_code,BTlvl,cout_code,cout_code)
Engrave.PartB8b(CourseObjectives,cout_code,BTlvl,cout_code,cout_code)

partca=["Write the Asymptomatic notationsused for worst-case,best-case and the average case analysis of algorithms. Write an algorithm for sequential search. Give worst-case, best-case and average case complexities."]

Engrave.partCa(partca,cout_code,BTlvl,cout_code,["16"])
partcb=["Write the charcteristics~~$CIT Logo Simple - PNG.png~~of an algoritm.~~$logo1.png~~"]
Engrave.partCb(partcb,cout_code,BTlvl,cout_code,["16"])

Create()