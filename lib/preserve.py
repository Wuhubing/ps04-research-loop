"""Retain previous stage outputs before a replay; never mix policy versions."""
import shutil
from common import *
r=Path(sys.argv[1]);names=sys.argv[2:];existing=[r/n for n in names if (r/n).exists()]
if existing:
 dest=r/'history'/uuid.uuid4().hex;dest.mkdir(parents=True)
 for p in existing:
  if p.is_dir():shutil.copytree(p,dest/p.name)
  else:shutil.copyfile(p,dest/p.name)
