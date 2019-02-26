import subprocess
from pytest import approx

def test_duration(fnin,fnout):
  	

	result1 = duration = subprocess.check_output(['ffprobe', '-i', fnin, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
	
	result1 = result1 [:-2]
	

	result2 = duration = subprocess.check_output(['ffprobe', '-i', fnout, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])

	#dest_duration = [x for x in result.stdout.readlines() if "Duration" in x]

	result2 = result2 [:-2]
	print(type(result1),result2)
	assert result1 == approx(result2)
