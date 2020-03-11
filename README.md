# Number of Islands

You are given a list of two-dimensional axis-aligned rectangular boxes that are either contained
within or disjoint from (non-overlapping with) one another. They therefore partition the plane into
a number of regions. The unbounded region, which lies outside all of the boxes, is classified as
“sea”. All other regions are classified either as “sea” or as “land”, subject to the constraint that no
two regions that share a boundary may share the same classification. The task is to output the
number of regions classified as “land”.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Assumptions

```
1) Assumption made that the input files will look like the text files I have in the zip file.
2) Assumption made that the only two input file types are text files and csv's.
```

### Prerequisites

What things you need to install the software and how to install them

```
Python 3
Pandas

If anaconda navigator is downloaded both of the previous requirements will be satisfied.
```

### Running the code

A step by step series of examples that tell you how to get the code running for the PDF Scenario

Opening the terminal

```
After the zip file is unzipped, the next step would be opening up a terminal tab at folder. 
I've set the python code to automatically run the PDF Scenario.
```

In the terminal

```
After the terminal is opened at the folder, simply type : python3 Islands.py.
The code will run and print out the output, which in this case is the number of islands (9).
```

End with an example of getting some data out of the system or using it for a little demo

## Test Case

A step by step series of examples that tell you how to get the code running for the Test Case

Opening the code.

```
After the PDF Scenario code is run, to run the test case simply open up the code and under the scope of the program,
change 'PDFScenario.txt' to 'test_case.txt' and save the code.
```

Repeat previous process

```
After the code is saved, all that needs to be done is to run: python3 Islands.py in the terminal and the answer will
be the number of islands for this scenario which is 8.
```

### Improvements

```
As this is very much a brute force method, one significant improvement/optimization that can be done would be to
utilize dynamic programming and memoizing to improve the code.
```
