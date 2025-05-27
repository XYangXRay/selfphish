__author__ = """Xiaogang Yang"""
__email__ = "yangxg@bnl.gov"
__version__ = "0.1.0"

from selfphish_torch.ganrec import *
from selfphish_torch.utils import *
from selfphish_torch.models import *
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
