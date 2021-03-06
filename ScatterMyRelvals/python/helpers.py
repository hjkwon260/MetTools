def architectures(tmpDir='/tmp/'):
  archDict = {}
  import os
  print "\nRetrieving information on architecture from scramv1"
  p = os.popen("/cvmfs/cms.cern.ch/common/scramv1 list -a CMSSW","r")
  while True:
    l = p.readline()
    if not l:break
    if not ('slc' in l and 'CMSSW' in l): continue
    l=l[:-1]
    s=l.split('/')
    arch = filter(lambda x:x.startswith('slc'),s)
    rel = filter(lambda x:x.startswith('CMSSW'),s)
    if not (len(arch)==1 and len(rel)>=1):
      print "Don't understand",l
    else:
      archDict[rel[0]]=arch[0]
#      print "[scramv1] Architecture:", rel[0],'->',arch[0] 

  print "\nRetrieving information on architecture from https://cmssdt.cern.ch/SDT/cgi-bin/ReleasesXML"
  os.system('wget https://cmssdt.cern.ch/SDT/cgi-bin/ReleasesXML -O '+tmpDir+'/ReleasesXML --no-check-certificate')
  from xml.dom import minidom
  xmldoc = minidom.parse(tmpDir+'/ReleasesXML')
  de=xmldoc.documentElement
  archs = de.getElementsByTagName('architecture')
  for a in archs:
    dict={str(r.getAttribute('label')): str(a.getAttribute('name')) for r in a.getElementsByTagName('project')}
    archDict.update(dict)
#    for k in dict.keys():
#      print "[ReleasesXML] Architecture:", k,'->',archDict[k]
  os.system('rm '+tmpDir+'/ReleasesXML')
  return archDict

def translatePdgIdToType(pdg): 
  apdg = abs(pdg)
  if apdg==211: return 1
  if apdg==11:  return 2
  if apdg==13:  return 3
  if apdg==22:  return 4
  if apdg==130: return 5
  if apdg==1:   return 6
  if apdg==2:   return 7
  return 0

import os
def getContent(dir, eos=False):
  if eos:
    eosCMD = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"
    p = os.popen(" ".join([eosCMD, "ls", dir]),"r")
  else:
    p = os.popen(" ".join(["ls", dir]),"r")
  all=[]
  while True:
    l = p.readline()
    if not l: break
    dn=l[:-1]
    all.append(dir+'/'+dn)
  return all 

def save(object, filename, protocol = -1):
  import cPickle, gzip
  """Save an object to a compressed disk file.
     Works well with huge objects.
  """
  file = gzip.GzipFile(filename, 'wb')
  cPickle.dump(object, file, protocol)
  file.close()

def load(filename):
  import cPickle, gzip
  file = gzip.GzipFile(filename, 'rb')
  object = cPickle.load(file)
  file.close()
  return object
