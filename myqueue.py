from mytasks import tadd

result = tadd.delay(4, 4)
print "result: " + str(result.get())
