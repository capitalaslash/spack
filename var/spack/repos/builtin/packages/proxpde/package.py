# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Proxpde(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/capitalaslash/proxpde.git"
    url = "https://github.com/capitalaslash/proxpde.git"
    git = "https://github.com/capitalaslash/proxpde.git"

    maintainers("capitalaslash")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-2.0-or-later", checked_by="capitalaslash")

    version("master", branch="master")
    # version("1.2.3", md5="0123456789abcdef0123456789abcdef")

    # FIXME: Add dependencies if required.
    depends_on("eigen@3.4.0")
    depends_on("fmt")
    depends_on("ginkgo@1.7.0")
    depends_on("hdf5@1.10.3:~mpi")
    depends_on("pugixml@1.13")
    depends_on("suite-sparse@5.13")
    depends_on("yaml-cpp@0.7.0")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ["-DPROXPDE_ENABLE_SECONDDERIV=False"]
        return args

