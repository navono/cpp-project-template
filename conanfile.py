from conans import ConanFile

class CppBOILERPLATE(ConanFile):
  name = "CppBOILERPLATE"
  version = "0.1.0"
  description = "A demo of using Visual Studio's Cmake integration with Conan.io"
  # author = "SolvingJ/Bincrafters"
  generators = "cmake"
  url = "https://github.com/solvingj/vs-cmake-conan-demo"
  requires = "fmt/7.1.3"

