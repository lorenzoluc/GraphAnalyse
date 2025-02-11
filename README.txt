Attention: I had to set os.environ["PATH"] with a specific path for it to work on my machine. I commented on this at the end before sending it.

The code has a single input file: "testfile.csv".

Some assumptions were made in this file:
	-The values retrieved are Id, X coordinate, Y coordinate, and width.
	-Id can be either a number or "highway." If it is a number and its last digit is 2, it means it is a warehouse.
	-Buildings are represented by an X coordinate and a Y coordinate.
	-Highways are represented by three points: X1, X2, and Y or X, Y1, and Y2. The double-value variables are provided as a list:
		--Example: (92,100) → This means the highways goes from coordinate 92 to coordinate 100 in one direction, while the other remains fixed.

Next, the code reads the user input and processes it, performing some checks:
	-Whether the values in the first column are integers or "highway".
	-Whether the values in the second and third columns are integers or integer tuples.
	-Whether the values in the fourth column are integers.
	-Whether buildings with the same Id are contiguous.
	-It is possible to obtain all points in the graph that highways pass through and their associated width values (often referred to as price here).
		--Example: (92,100), 92, 1 will return something like: (92,92), (93,92)... (100,92) and 1,1...1.
	-The assumption is that highways with width 1 are less desirable than highways with width 2. So, in the end, the path with the highest value is considered the most interesting.

After that, objects are created for each element, and these objects are stored in a variable.

In the next step, the graph starts being generated. For drawing, there are two categories:

	-Buildings or warehouses: All points associated with the same Id are created, and then these points are connected.
	-Highways: highways are created using three coordinates, followed by a check to see if a highway intersects another.

In the final step, it is possible to check if there's a way between two buildings. A simulation is run to check the connection between building 4 and building 1 (which has no connection) and between building 1 and warehouse 2, where there are at least three possible paths, one for each of the three intersection points between the warehouse and the highway