# BigData_CitiBike_Statistics

This project used Python’s generators and streaming. Here I used the Citibike dataset citibike.csv file which can be downloaded from the CitiBike website https://www.citibikenyc.com/system-data    it was corrected recently to have all the records sorted by starting time. This is needed for task 2 of this project.

##TASK 1
The first task is to compute the median age of the Citibike’s subscribed customers. Here we can only read data
line by line and are not allowed to store the entire data set in memory. Indeed, we should not have any
containers (e.g. list, dictionary, DataFrame, etc.) with more than 100 elements in memory. We use the
citibike.csv data file for testing here, but we will evaluate this code on a much larger input to ensure its streaming capability.

We will make a stand-alone Python program named proj_task1.py (i.e. just a single .py file, no notebooks)
that takes a CSV file as arguments and print out a single number showing the median age of the subscribed
customers in that file.

EXAMPLE:
$ python proj_task1.py citibike.csv
Output:
39


##TASK 2
This task is to write a generator to extract the first ride of the day from a Citibike data stream. The data
stream is sorted based on starting times (similar to the citibike.csv file). The first ride of the day is interpreted as the ride with the earliest starting time of a day. For the sample data, which is a week worth of citibike records, the generator will generate 7 items (one for each day).  The generator currently takes in csv.DictReader generator and output its first element. The output of the generator must be in the same format as csv.DictReader. We can think of this generator as a filter only passing certain records out.

We will make a stand-alone Python program named proj_task2.py (i.e. just a single .py file, no notebooks)
that takes a CSV file as arguments and print out a single number showing the median age of the subscribed
customers in that file.

EXAMPLE:
$ python proj_task2.py citibike.csv
Output:
1,,801,2015-02-01 00:00:00+00,2015-02-01 00:14:00+00,521,8 Ave & W 31
St,40.75044999,-73.99481051,423,W 54 St & 9 Ave,40.76584941,-
73.98690506,17131,Subscriber,1978,2
...
...
...
