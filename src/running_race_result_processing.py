
import statistics
class ResultProcess:
    def __init__(self):
        pass
    def calculate_average_time(self, file):
        f = open("race_results.txt","r")
        lines = f.readlines()
        result=[]
        for x in lines:
          time_column = (x.split(',')[4])
          minutes_and_seconds = str.strip(time_column)
          minutes = minutes_and_seconds.split(':')[0]
          seconds = minutes_and_seconds.split(':')[1]
          num = int(minutes) * 60 + int(seconds)
          result.append(num)
        print str(int(statistics.mean(result)) / 60) + " " + str(int(statistics.mean(result)) % 60)





        f.close()
        # readline  get 5th column of the file
        # converti it to second and calcualte the average
        # convert it back to min and seconds
if __name__ == '__main__':
    resultProcess = ResultProcess()
    resultProcess.calculate_average_time("race_results.txt")