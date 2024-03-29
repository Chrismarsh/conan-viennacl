from conans import ConanFile, CMake, tools
import os
from conans.tools import download, unzip

class ViennaCLConan(ConanFile):
    name = "viennacl"
    description = "ViennaCL is a free open-source linear algebra library for computations on many-core architectures (GPUs, MIC) and multi-core CPUs. "
    version = "1.7.1"
    generators = "cmake"
    license = "http://viennacl.sourceforge.net/doc/manual-license.html"
    url="http://viennacl.sourceforge.net"
    settings = None
    options = { 
        "with_opencl" :[True, False],
        "with_cuda": [True, False],
        "with_omp" :[True, False],
        "examples":  [True, False]
    }

    default_options = { 
        "with_opencl" :False,
        "with_cuda": False,
        "with_omp" :False,
        "examples":  False
    }

    _source_subfolder = 'viennacl'

    # def requirements(self):
    #     self.requires("netcdf-c/4.6.2")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("ViennaCL-{}".format(self.version), self._source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)

        cmake.definitions["ENABLE_OPENCL"] = self.options.with_opencl
        cmake.definitions["ENABLE_CUDA"] = self.options.with_cuda
        cmake.definitions["ENABLE_OPENMP"] = self.options.with_omp
        cmake.definitions["BUILD_EXAMPLES"] = self.options.examples
        cmake.configure(source_folder=self._source_subfolder)
        return cmake
        
    def build(self):

        cmake = self.configure_cmake()
        cmake.build()

        return cmake

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        return
