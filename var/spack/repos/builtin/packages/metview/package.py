##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Metview(CMakePackage):
    """ECMWF interactive meteorological application."""

    homepage = "https://confluence.ecmwf.int/display/METV/Metview"
    url      = "https://confluence.ecmwf.int/download/attachments/3964985/Metview-5.0.1-Source.tar.gz"

    version('5.9.0', sha256='6bbcf15602a21c8fee4276ec11179c6f95247eeaf08a870181ec339a7c5b80ba')
    version('5.7.2', sha256='8cc1c156902b62c5a2eeb6d51cc7c898878ee616973ea3903d2fafbe5283c532')
    version('5.6.1', sha256='5e1abf46e290911fe90cb35957c45ab61901c285b9a70e195a04d17608b86fd0')
    version('5.5.0', sha256='3841b097de7bc68e467a0cf7b829cdd0ac4485768eec9ae6426865ce56a48652')
    version('5.3.0', sha256='c9b7a1f9b11b027b49c937d1de804f7e8da23bc7dc30f19c2284cd6ddffceff1')
    version('5.1.1', 'eca65b682b4106f0962d878ad2b9e4e1')
    version('5.1.0', '12d3fb2f1e7b618f365338731d40d7615609b3b1')
    version('5.0.3', '2e206ba7ca96db2538dce9f99d92437fd5b0af06')
    version('5.0.1', '93f0c01c72e6b52d4dd196bc937c55a5d740a2a7')
    #version('4.8.7', '79ebe622c3d6480f3940d524f21db302')

    variant('build_type', default='Production',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo', 'Production'))

    # Non-optional dependencies
    depends_on('eccodes +fortran +pthreads')
    depends_on('magics grib=eccodes +metview +qt +netcdf +cairo')
    depends_on('netcdf-cxx')
    depends_on('libtirpc')

    patch('string.patch')

    def cmake_args(self):
        spec = self.spec
        args = []
        # args.append('-Deccodes_DIR=%s' % spec['eccodes'].prefix)
        # args.append('-Dlibemos_DIR=%s' % spec['libemos'].prefix)
        # args.append('-DMAGICS_PATH=%s' % spec['magics'].prefix)
        args.append('-DENABLE_QT5=ON')
        args.append('-DCMAKE_C_FLAGS=-I/usr/include/tirpc')
        args.append('-DCMAKE_CXX_FLAGS=-I/usr/include/tirpc')
        args.append('-DCMAKE_EXE_LINKER_FLAGS=/usr/lib/libtirpc.so')

        return args
