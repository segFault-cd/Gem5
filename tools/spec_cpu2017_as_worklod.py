import m5
from m5.objects import *

gem5_dir = '/cdt/gem5/'
spec_dir = '/cdt/cpu2017-1.1.9/benchspec/CPU/'
out_dir = '/cdt/gem5/m5out/skylake-spec2017/'

x86_suffix = '_base.mytest-m64'

flagsAndOperands = {
    'perlbench': {
        'cmd': ['600.perlbench_s/exe/perlbench_s'], 
        'test': ['-I', '-I./lib', spec_dir + '500.perlbench_r/data/test/input/' + 'makerand.pl', '>', out_dir + 'perlbench.' + 'makerand.out', '2>>', out_dir + 'perlbench.' + 'makerand.err'],
        'train': ['-I./lib', spec_dir + '500.perlbench_r/data/train/input/' + 'diffmail.pl', '2', '550', '15', '24', '23', '100', '>', out_dir + 'perlbench.' + 'diffmail.2.550.15.24.23.100.out', '2>>', out_dir + 'perlbench.' + 'diffmail.2.55.15.24.23.100.err'],
        'ref': ['-I./lib', spec_dir + '500.perlbench_r/data/refrate/input/' + 'checkspam.pl', '2500', '5', '25', '11', '150', '1', '1', '1', '1', '>', out_dir + 'perlbench.' + 'checkspam.2500.3.25.11.150.1.1.1.1.out', '2>>', out_dir + 'perlbench.' + 'checkspam.2500.5.25.11.150.1.1.1.1.err']
    },

    'gcc': {
        'cmd': ['602.gcc_s/exe/sgcc'],
        'test': ['-O3', '-finline-limit=50000', '-o', 't1.opts-O3_-finline-limit_50000.s', '>', out_dir + 'gcc.' + 't1.opts-O3_-finline-limit_50000.out', '2>>', out_dir + 'gcc.' + 't1.opts-O3_-finline-limit_50000.err'],
        'train': ['-O3', ' -finline-limit=50000', '-o', '200.opts-O3_-finline-limit_50000.s', '>', out_dir + 'gcc.' + '200.opts-O3_-finline-limit_50000.out', '2>>', out_dir + 'gcc.' + '200.opts-O3_-finline-limit_50000.err'],
        'ref': [spec_dir + '502.gcc_r/data/refspeed/input/' + 'gcc-pp.c', '-O5', ' -fipa-pta', '-o', 'gcc-pp.opts-O5_-fipa-pta.s', '>', out_dir + 'gcc.' + 'gcc-pp.opts-O5_-fipa-pta.out', out_dir + 'gcc.' + '2>>', ' gcc-pp.opts-O5_-fipa-pta.err']
    },

    'mcf': {
        'cmd': ['605.mcf_s/exe/mcf_s'],
        'test': [spec_dir + '505.mcf_r/data/test/input/' + 'inp.in', '>', out_dir + 'mcf.' + 'inp.out', '2>>', out_dir + 'mcf.' + 'inp.err'],
        'train': [spec_dir + '505.mcf_r/data/test/input/' + 'inp.in', '>', out_dir + 'mcf.' + 'inp.out', '2>>', out_dir + 'mcf.' + 'inp.err'],
        'ref': [spec_dir + '505.mcf_r/data/test/input/' + 'inp.in', '>', out_dir + 'mcf.' + 'inp.out', '2>>', out_dir + 'mcf.' + 'inp.err']
    },

    'omnetpp': {
        'cmd': ['620.omnetpp_s/exe/omnetpp_s'],
        'test': ['-c', spec_dir + '520.omnetpp_s/data/test/input/' + 'General', '-r', '0', '>', out_dir + 'onmetpp.' + 'omnetpp.General-0.out', '2>>', out_dir + 'onmetpp.' + 'omnetpp.General-0.err'],
        'train': ['-c', spec_dir + '520.omnetpp_s/data/test/input/' + 'General', '-r', '0', '>', out_dir + 'onmetpp.' + 'omnetpp.General-0.out', '2>>', out_dir + 'onmetpp.' + 'omnetpp.General-0.err'],
        'ref': ['-c', spec_dir + '520.omnetpp_s/data/test/input/' + 'General', '-r', '0', '>', out_dir + 'onmetpp.' + 'omnetpp.General-0.out', '2>>', out_dir + 'onmetpp.' + 'omnetpp.General-0.err']
    },

    'xalancbmk': {
        'cmd': ['623.xalancbmk_s/exe/xalancbmk_s'],
        'test': ['-v', spec_dir + '523.xalancbmk_r/data/test/input/' + 'test.xml', spec_dir + '523.xalancbmk_r/data/test/input/' + 'xalanc.xsl', '>', out_dir + 'xalancbmk.' + 'test-test.out', '2>>', out_dir + 'xalancbmk.' + 'test-test.err'],
        'train': ['-v', spec_dir + '523.xalancbmk_r/data/train/input/' + 'allbooks.xml', spec_dir + '523.xalancbmk_r/data/train/input/' + 'xalanc.xsl', '>', out_dir + 'xalancbmk.' + 'train-allbooks.out', '2>>', out_dir + 'xalancbmk.' + 'train-allbooks.err'],
        'ref': ['-v', spec_dir + '523.xalancbmk_r/data/refspeed/input/' + 't5.xml', spec_dir + '523.xalancbmk_r/data/refspeed/input/' + 'xalanc.xsl', '>', out_dir + 'xalancbmk.' + 'ref-t5.out', '2>>', out_dir + 'xalancbmk.' + 'ref-t5.err']
    },

    'x264': {
        'cmd': ['625.x264_s/exe/x264_s'],
        'test': ['--dumpyuv', '50', '--frames', '156', '-o', spec_dir + '525.x264_r/data/test/input/' + 'BuckBunny.264', spec_dir + '525.x264_r/data/test/input/' + 'BuckBunny.yuv', '1280x720', '>', out_dir + 'x264.' + 'run_000-156_x264.out', '2>>', out_dir + 'x264.' + 'run_000-156_x264.err'],
        'train': ['--dumpyuv', '50', '--frames', '142', '-o', spec_dir + '525.x264_r/data/test/input/' + 'BuckBunny.264', spec_dir + '525.x264_r/data/test/input/' + 'BuckBunny.yuv', '1280x720', '>', out_dir + 'x264.' + 'run_000-142_x264.out', '2>>', out_dir + 'x264.' + 'run_000-142_x264.err'],
        'ref': ['--pass', '1', '--stats', '']
    },

    'deepsjeng': {
        'cmd': ['631.deepsjeng_s/exe/deepsjeng_s'],
        'test': [spec_dir + '631.deepsjeng_s/data/test/input/' + 'test.txt', '>', out_dir + 'deepsjeng.' + 'test.out', '2>>', out_dir + 'deepsjeng.' + 'test.err'],
        'train': [spec_dir + '631.deepsjeng_s/data/train/input/' + 'train.txt', '>', out_dir + 'deepsjeng.' + 'train.out', '2>>', out_dir + 'deepsjeng.' + 'train.err'],
        'ref': [spec_dir + '631.deepsjeng_s/data/refspeed/input/' + 'ref.txt', '>', out_dir + 'deepsjeng.' + 'ref.out', '2>>', out_dir + 'deepsjeng.' + 'ref.err']
    },

    'leela': {
        'cmd': ['641.leela_s/exe/leela_s'],
        'test': [spec_dir + '541.leela_r/data/test/input/' + 'test.sgf', '>', out_dir + 'leela.' + 'test.out', '2>>', out_dir + 'leela.' + 'test.err'],
        'train': [spec_dir + '541.leela_r/data/train/input/' + 'train.sgf', '>', out_dir + 'leela.' + 'train.out', '2>>', out_dir + 'leela.' + 'train.err'],
        'ref': [spec_dir + '541.leela_r/data/ref/input/' + 'ref.sgf', '>', out_dir + 'leela.' + 'ref.out', '2>>', out_dir + 'leela.' + 'ref.err']
    },

    'exchange': {
        'cmd': ['648.exchange2_s/exe/exchange2_s'],
        'test': ['0', '>', out_dir + 'exchange2.' + 'exchange2.txt', '2>>', out_dir + 'exchange2.' + 'exchange2.err'],
        'train': ['1', '>', out_dir + 'exchange2.' + 'exchange2.txt', '2>>', out_dir + 'exchange2.' + 'exchange2.err'],
        'ref': ['6', '>', out_dir + 'exchange2.' + 'exchange2.txt', '2>>', out_dir + 'exchange2.' + 'exchange2.err']
    },

    'xz': {
        'cmd': ['657.xz_s/exe/xz_s'],
        'test': [spec_dir + '557.xz_r/data/all/input/' + 'cpu2006docs.tar.xz', '4', '055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae', ' 1548636', '1555348', '0', '>', out_dir + 'xz.' + 'cpu2006docs.tar-4-0.out', '2>>', out_dir + 'xz.' + 'cpu2006docs.tar-4-0.err'],
        'train': [spec_dir + '557.xz_r/data/all/input/' + ' input.combined.xz', '40', 'a841f68f38572a49d86226b7ff5baeb31bd19dc637a922a972b2e6d1257a890f6a544ecab967c313e370478c74f760eb229d4eef8a8d2836d233d3e9dd1430bf', '6356684', '-1', '9', '>', out_dir + 'xz.' + 'input.combined-40-8.out', '2>>', out_dir + 'xz.' + 'input.combined-40-8.err'],
        'ref': [spec_dir + '557.xz_r/data/all/input/' + 'cld.tar.xz', '160', '19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474', '59796407', '61004416', '6', '>', out_dir + 'xz.' + 'cld.tar-160-6.out', '2>>', out_dir + 'xz.' + 'cld.tar-160-6.err']
    },

    'bwaves': {
        'cmd': ['603.bwaves_s/exe/speed_bwaves'],
        'test': ['bwaves_1', '<', spec_dir + '503.bwaves_r/data/test/input' + 'bwaves_1.in', '>', out_dir + 'bwaves.' + 'bwaves_1.out', '2>>', out_dir + 'bwaves.' + 'bwaves_1.err'],
        'train': ['bwaves_1', '<', spec_dir + '503.bwaves_r/data/test/input' + 'bwaves_1.in', '>', out_dir + 'bwaves.' + 'bwaves_1.out', '2>>', out_dir + 'bwaves.' + 'bwaves_1.err'],
        'ref': ['bwaves_1', '<', spec_dir + '503.bwaves_r/data/test/input' + 'bwaves_1.in', '>', out_dir + 'bwaves.' + 'bwaves_1.out', '2>>', out_dir + 'bwaves.' + 'bwaves_1.err']
    },

    'cactuBSSN': {
        'cmd': ['607.cactuBSSN_s/exe/cactuBSSN_s'],
        'test': [spec_dir + '507.cactuBSSN_r/data/test/input/' + 'spec_test.par', '>', out_dir + 'cactuBSSN.' + 'spec_test.out', '2>>', out_dir + 'cactuBSSN.' + 'spec_test.err'],
        'train': [spec_dir + '507.cactuBSSN_r/data/train/input/' + 'spec_train.par', '>', out_dir + 'cactuBSSN.' + 'spec_train.out', '2>>', out_dir + 'cactuBSSN.' + 'spec_train.err'],
        'ref': [spec_dir + '507.cactuBSSN_r/data/ref/input/' + 'spec_ref.par', '>', out_dir + 'cactuBSSN.' + 'spec_ref.out', '2>>', out_dir + 'cactuBSSN.' + 'spec_ref.err']
    },

    'namd': {
        'cmd': ['508.namd_r/exe/namd_r'],
        'test': ['--input', spec_dir + '508.namd_r/data/all/input/' + 'apoa1.input', '--iterations', '1', '--output', spec_dir + '508.namd_r/data/all/output/' + 'apoa1.test.output', '>', out_dir + 'namd.' + 'namd.out', '2>>', out_dir + 'namd.' + 'namd.err'],
        'train': ['--input', spec_dir + '508.namd_r/data/all/input/' + 'apoa1.input', '--iterations', '7', '--output', spec_dir + '508.namd_r/data/all/output/' + 'apoa1.train.output', '>', out_dir + 'namd.' + 'namd.out', '2>>', out_dir + 'namd.' + 'namd.err'],
        'ref': ['--input', spec_dir + '508.namd_r/data/all/input/' + 'apoa1.input', '--iterations', '65', '--output', spec_dir + '508.namd_r/data/all/output/' + 'apoa1.ref.output', '>', out_dir + 'namd.' + 'namd.out', '2>>', out_dir + 'namd.' + 'namd.err']
    },

    'parest': {
        'cmd': ['510.parest_r/exe/parent_r'],
        'test': [spec_dir + '510.parest_r/data/test/input/' + 'test.prm', '>', out_dir + 'parest.' + 'test.out', '2>>', out_dir + 'parest.' + 'test.err'],
        'train': [spec_dir + '510.parest_r/data/train/input/' + 'train.prm', '>', out_dir + 'parest.' + 'train.out', '2>>', out_dir + 'parest.' + 'train.err'],
        'ref': [spec_dir + '510.parest_r/data/ref/input/' + 'ref.prm', '>', out_dir + 'parest.' + 'ref.out', '2>>', out_dir + 'parest.' + 'ref.err']
    },

    'povray': {
        'cmd': ['511.povray_r/exe/povray_r'],
        'test': [spec_dir + '511.povray_r/data/test/input/' + 'SPEC-benchmark-test.in', '>', out_dir + 'povray.' + 'test.out', '2>>', out_dir + 'parest.' + 'test.err'],
        'train': [spec_dir + '511.povray_r/data/train/input/' + 'SPEC-benchmark-train.in', '>', out_dir + 'povray.' + 'train.out', '2>>', out_dir + 'parest.' + 'train.err'],
        'ref': [spec_dir + '511.povray_r/data/ref/input/' + 'SPEC-benchmark-ref.in', '>', out_dir + 'povray.' + 'ref.out', '2>>', out_dir + 'parest.' + 'ref.err']
    },

    'lbm': {
        'cmd': ['619.lbm_s/exe/lbm_s'],
        'test': ['20', 'reference.dat', '0', '1', spec_dir + '619.lbm_s/data/test/input/' + '200_200_260_ldc.of', '>', out_dir + 'lbm.' + 'test.out', '2>>', out_dir + 'lbm.' + 'test.err'],
        'train': ['300', 'reference.dat', '0', '1', spec_dir + '619.lbm_s/data/train/input/' + '200_200_260_ldc.of', '>', out_dir + 'lbm.' + 'train.out', '2>>', out_dir + 'lbm.' + 'train.err'],
        'ref': ['3000', 'reference.dat', '0', '1', spec_dir + '619.lbm_s/data/ref/input/' + '200_200_260_ldc.of', '>', out_dir + 'lbm.' + 'train.out', '2>>', out_dir + 'lbm.' + 'ref.err']
    },

    'wrf': {
        'cmd': ['621.wrf_s/exe/wrf_s'],
        'test': ['>', out_dir + 'wrf.' + 'rsl.out.000', '2>>', out_dir + 'wrf.' + 'wrf.err'],
        'train': ['>', out_dir + 'wrf.' + 'rsl.out.000', '2>>', out_dir + 'wrf.' + 'wrf.err'],
        'ref': ['>', out_dir + 'wrf.' + 'rsl.out.000', '2>>', out_dir + 'wrf.' + 'wrf.err']
    },

    'blender': {
        'cmd': ['526.blender_r/exe/blender_r'],
        'test': [spec_dir + '526.blender_r/data/test/input' + 'cube.blend', '--render-output', 'cube_', '--threads', '1', '-b', '-F', 'RAWTGA', '-s', '1', '-a', '>', out_dir + 'blender.' + 'cube.1.spec.out', '2>>', out_dir + 'blender.' + 'cube.1.spec.err'],
        'train': [spec_dir + '526.blender_r/data/test/input' + 'sh5_reduced.blend', '--render-output', 'sh5_reduced_', '--threads', '1', '-b', '-F', 'RAWTGA', '-s', '234', '-e', '234', '-a', '>', out_dir + 'blender.' + 'sh5_reduced.234.spec.out', '2>>', out_dir + 'blender' + 'sh5_reduced.234.spec.err'],
        'ref': [spec_dir + '526.blender_r/data/test/input' + 'sh3_no_char.blend', '--render-output', 'sh3_no_char_', '--threads', '1', '-b', '-F', 'RAWTGA', '-s', '849', '-e', '849', '-a', '>', out_dir + 'blender.' + 'sh3_no_char.849.spec.out', '2>>', out_dir + 'blender' + 'sh3_no_char.849.spec.err']
    },

    'cam4': {
        'cmd': ['627.cam4_s/exe/cam4_s'],
        'test': ['>', out_dir + 'cam4.' + 'cam4.txt', '2>>', out_dir + 'cam4.' + 'cam4.err'],
        'train': ['>', out_dir + 'cam4.' + 'cam4.txt', '2>>', out_dir + 'cam4.' + 'cam4.err'],
        'ref': ['>', out_dir + 'cam4.' + 'cam4.txt', '2>>', out_dir + 'cam4.' + 'cam4.err']
    },

    'pop2': {
        'cmd': ['628.pop2_s/exe/speed_pop2'],
        'test': ['>', out_dir + 'pop2.' + 'pop2.out', '2>>', out_dir + 'pop2.' + 'pop2.err'],
        'train': ['>', out_dir + 'pop2.' + 'pop2.out', '2>>', out_dir + 'pop2.' + 'pop2.err'],
        'ref': ['>', out_dir + 'pop2.' + 'pop2.out', '2>>', out_dir + 'pop2.' + 'pop2.err']
    },

    'imagick': {
        'cmd': ['638.imagick_s/exe/imagick_s'],
        'test': ['-limit', 'disk', '0', spec_dir + '538.imagick_r/data/test/input/' + 'test_input.tga', '-shear', '25', '-resize', '640x480', '-negate', '-alpha', 'Off', spec_dir + '538.imagick_r/data/test/output/' + 'test_output.tga', '>', out_dir + 'imagick.' + 'test_convert.out', '2>>', out_dir + 'imagick.' + 'test_convert.err'],
        'train': ['-limit', 'disk', '0', spec_dir + '538.imagick_r/data/train/input/' + 'train_input.tga', '-resize', '320x240', '-shear', '31', '-edge', '140', '-negate', '-flop', '-resize', '900x900', '-edge', '10', spec_dir + '538.imagick_r/data/test/output/' + 'train_output.tga', '>', out_dir + 'imagick.' + 'train_convert.out', '2>>', out_dir + 'imagick.' + 'train_convert.err'],
        'ref': ['-limit', 'disk', '0', spec_dir + '538.imagick_r/data/refrate/input/' + 'refrate_input.tga', '-edge', '41', '-resample', '181%', '-emboss', '31', '-colorspace', 'YUV', '-mean-shift', '19x19+15%', '-resize', '30%', spec_dir + '538.imagick_r/data/refrate/output/' + 'refrate_output.tga', '>', out_dir + 'imagick.' + 'ref_convert.out', '2>>', out_dir + 'imagick.' + 'ref_convert.err']
    },

    'nab': {
        'cmd': ['644.nab_s/exe/nab_s'],
        'test': [spec_dir + '544.nab_r/data/test/input/hkrdenq/hkrdenq' '1930344093', '1000', '>', out_dir + 'nab.' + 'hkrdenq.out', '2>>', out_dir + 'nab.' + 'hkrdenq.err'],
        'train': [spec_dir + '544.nab_r/data/train/input/aminos/aminos' '391519156', '1000', '>', out_dir + 'nab.' + 'aminos.out', '2>>', out_dir + 'nab.' + 'aminos.err'],
        'ref': [spec_dir + '544.nab_r/data/refrate/input/1am0/1am0' '1122214447', '122', '>', out_dir + 'nab.' + '1am0.out', '2>>', out_dir + 'nab.' + '1am0.err']
    },

    'fotonik3d': {
        'cmd': ['649.fotonik3d_s/exe/fotonik3d_s'],
        'test': ['>', out_dir + 'fotonik3d.' + 'fotonik3d.log', '2>>', out_dir + 'fotonik3d.' + 'fotonik3d.err'],
        'train': ['>', out_dir + 'fotonik3d.' + 'fotonik3d.log', '2>>', out_dir + 'fotonik3d.' + 'fotonik3d.err'],
        'ref': ['>', out_dir + 'fotonik3d.' + 'fotonik3d.log', '2>>', out_dir + 'fotonik3d.' + 'fotonik3d.err']
    },

    'roms': {
        'cmd': ['654.roms_s/exe/sroms'],
        'test': ['<', spec_dir + '554.roms_r/data/test/input/ocean_benchmark0.in.x', '>', out_dir + 'roms.' + 'ocean_benchmark0.log', '2>>', out_dir + 'roms.' + 'ocean_benchmark0.err'],
        'train': ['<', spec_dir + '554.roms_r/data/train/input/ocean_benchmark1.in.x', '>', out_dir + 'roms.' + 'ocean_benchmark1.log', '2>>', out_dir + 'roms.' + 'ocean_benchmark1.err'],
        'ref': ['<', spec_dir + '554.roms_r/data/refrate/input/ocean_benchmark2.in.x', '>', out_dir + 'roms.' + 'ocean_benchmark2.log', '2>>', out_dir + 'roms.' + 'ocean_benchmark2.err']
    }
}

class c_Benchmark:
    def __init__(self, name):
        self.name = name
        self.test = None
        self.train = None
        self.reference = None
    
    def __str__(self):
        return self.name
    
    def set(self, dict):

        self.test = Process()
        self.test.executable = spec_dir + dict[self.name]['cmd'] + x86_suffix
        self.test.cmd = [self.test.executable] + dict[self.name]['test']

        self.train = Process()
        self.train.executable = spec_dir + dict[self.name]['cmd'] + x86_suffix
        self.train.cmd = [self.train.executable] + dict[self.name]['train']

        self.ref = Process()
        self.ref.executable = spec_dir + dict[self.name]['cmd'] + x86_suffix
        self.ref.cmd = [self.ref.executable] + dict[self.name]['ref']   
    
'''intspeed benchmarks'''
perlbench = c_Benchmark('perlbench')
perlbench.set(flagsAndOperands)

gcc = c_Benchmark('gcc')
gcc.set(flagsAndOperands)

mcf = c_Benchmark('mcf')
mcf.set(flagsAndOperands)

omnetpp = c_Benchmark('omnetpp')
omnetpp.set(flagsAndOperands)

xalancbmk = c_Benchmark('xalancbmk')
xalancbmk.set(flagsAndOperands)

x264 = c_Benchmark('x264')
x264.set(flagsAndOperands)

deepsjeng = c_Benchmark('deepsjeng')
deepsjeng.set(flagsAndOperands)

leela = c_Benchmark('leela')
leela.set(flagsAndOperands)

exchange2 = c_Benchmark('exchange2')
exchange2.set(flagsAndOperands)

xz = c_Benchmark('xz')
xz.set(flagsAndOperands)

'''fpspeed benchmarks'''
bwaves = c_Benchmark('bwaves')
bwaves.set(flagsAndOperands)

cactuBSSN = c_Benchmark('cactuBSSN')
cactuBSSN.set(flagsAndOperands)

lbm = c_Benchmark('lbm')
lbm.set(flagsAndOperands)

wrf = c_Benchmark('wrf')
wrf.set(flagsAndOperands)

cam4 = c_Benchmark('cam4')
cam4.set(flagsAndOperands)

pop2 = c_Benchmark('pop2')
pop2.set(flagsAndOperands)

imagick = c_Benchmark('imagick')
imagick.set(flagsAndOperands)

nab = c_Benchmark('nab')
nab.set(flagsAndOperands)

fotonik3d = c_Benchmark('fotonik3d')
fotonik3d.set(flagsAndOperands)

roms = c_Benchmark('roms')
roms.set(flagsAndOperands)

'''fprate benchmarks'''
namd = c_Benchmark('namd')
namd.set(flagsAndOperands)

parest = c_Benchmark('parest')
parest.set(flagsAndOperands)

povray = c_Benchmark('povray')
povray.set(flagsAndOperands)

blender = c_Benchmark('blender')
blender.set(flagsAndOperands)