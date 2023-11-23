from hbsir.core.metadata_reader import open_yaml
import sys

res = open_yaml("/home/tersetears/Sync/project/HBSIR/docs/scripts/tables.yaml")

def pretty(d, indent=1):
   for key, value in d.items():
      print('\n' + '#' * indent + " " + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\n' + str(value))

orig_stdout = sys.stdout
f = open('out.md', 'w')
sys.stdout = f
pretty(res)
sys.stdout = orig_stdout
f.close()
