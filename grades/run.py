from main import grades
import json
with open('result.txt', 'a') as r :
    r.write("\n")
    r.write(json.dumps(grades(), indent=4))


