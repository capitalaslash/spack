# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libogg(AutotoolsPackage):
    """Ogg is a multimedia container format, and the native file and stream
    format for the Xiph.org multimedia codecs."""

    homepage = "https://www.xiph.org/ogg/"
    url      = "http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz"

    version('1.3.2', sha256='e19ee34711d7af328cb26287f4137e70630e7261b17cbe3cd41011d73a654692')
