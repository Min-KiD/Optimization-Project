# Contents
- [Production Scheduling: Introduction](#production-scheduling-introduction)
- [How to run algorithm](#how-to-run-algorithm)
- [Collaborators](#collaborators)
- [Files and Directories in the repository](#files-and-directories-in-the-repository)
# Production Scheduling: Introduction
Production scheduling includes setting up production schedules, coordinating and assigning labor to each person, group of people, and machine, and arranging the work order at each workplace to ensure production completion on schedule.

It is an essential tool for manufacturing and engineering, which can significantly impact a process's productivity. In manufacturing, the purpose of scheduling is to keep the due dates of customers and then minimize the production time and costs by telling a production facility when to make, with which staff, and on which equipment. Production scheduling aims to maximize the efficiency of the operation, utilize the maximum resources available and reduce costs.

Description of our project:
- An agricultural food-providing company needs to produce N products 1,2,3,..., N
- The proposed cost of producing 1 unit of product i is c(i)
- The area of field needed to produce 1 unit of products i is a(i)
- The profit obtained from producing 1 unit of product i is f(i)
- Know that m(i) is the minimum number of units of product i needed to produce when deciding to make that product
- The total area of the field is A

Goal: the profit is the maximum and the total cost of production is less than or equal to a value of C
For more details, please read in `Report.pdf` or `Optimization.pptx`

# How to run algorithm
Create a text file for the input called `test.txt`, the input includes:
- Line 1: N,A,C
- Line 2: c(1),c(2),….,c(N)
- Line 3: a(1),a(2),….,a(N)
- Line 4: f(1),f(2),….,f(N)
- Line 5: m(1),m(2),….,m(N)

Download algorithm in the `Algorithms`.<br> and run the file 
For example you can download file `test1.txt` of us from `DataSets`.<br>
Or you can generate random tests and adjust the size by file `generate_input.py` and read it by file `read_input.py`
# Collaborators
We are group 17, in Fundamental of Optimization class. Under the guidance of our lecturer, Bui Quoc Trung, we work together on this problem.
- Nguyen Minh Cuong
- Nguyen Viet Minh
- Nguyen Tuan Long
# Files and directories in the repository
`read_input.py`: read the input from text file to collect information.<br>
`generate_input.py`: generate random test.<br>
`Algorithms\ConstraintOptimization(Ortools).py`: use Constraint Programming to solve.<br>
`Algorithms\ExhaustiveSearch(DFS).py`: use Exhaustive Search to solve.<br>
`Algorithms\DynamicProgramming.py`: use Dynamic Programming to solve.<br>
`Algorithms\Mixed-IntegerProgramming(Gurobi).py`: use Mixed-Integer Programming to solve.<br>
`Algorithms\Heuristic1.0.py`: use first ideal Heuristic to solve.<br>
`Algorithms\Heuristic2.0.py`: use second ideal Heuristic in first way to solve.<br>
`Algorithms\Heuristic2.1.py`: use second ideal Heuristic in second way to solve.<br>
`Algorithms\Heuristic2.2.py`: use second ideal Heuristic in third way to solve.<br>
`DataSets`: folder with available tests that we use to test all algorithms.<br>
`test.txt`: the text file to collect input.<br>
