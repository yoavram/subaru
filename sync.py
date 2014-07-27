import sys
import datetime 

DATE_FORMAT = '%H:%M:%S,%f'
zero = datetime.datetime.strptime('2000:00:00:00,000', '%Y:' + DATE_FORMAT)

def shift(time_str, seconds):
  time = datetime.datetime.strptime('2000:' + time_str, '%Y:' + DATE_FORMAT)
  time_plus_seconds = time + datetime.timedelta(seconds=seconds)
  if time_plus_seconds < zero:
    time_plus_seconds = zero
  back_to_string = datetime.datetime.strftime(time_plus_seconds, DATE_FORMAT)[:-3]
  return back_to_string

file_name = sys.argv[1]
seconds = int(sys.argv[2])
output_name = file_name[:-4] + '_shifted.srt'
print "Shifting", file_name, "by", seconds, "seconds"
print "Writing output to",output_name
f = open(file_name, 'r')
f_new = open(output_name, 'w')

for line in f:
  if '-->' in line:
    #print(line);
    from_string = line[:12]
    from_string_plus_seconds = shift(from_string, seconds)
    
    to_string = line[17:-1]
    to_string_plus_seconds = shift(to_string, seconds)
  
    f_new.write(from_string_plus_seconds + ' --> ' + to_string_plus_seconds + '\n')
  else:
    f_new.write(line);

f.close()
f_new.close()
print "Finished"