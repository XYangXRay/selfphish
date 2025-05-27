import numpy as np
import tifffile
import matplotlib.pyplot as plt
from selfphish_torch.utils import angles, nor_tomo
from selfphish_torch.ganrec import GANtomo

prj = tifffile.imread("./test_data/shale_prj.tiff")
nang, px = prj.shape
ang = angles(nang)
prj = nor_tomo(prj)
rec = GANtomo(prj, ang, iter_num=1000).recon()
tifffile.imwrite("./test_results/recon_shale.tiff", rec)
