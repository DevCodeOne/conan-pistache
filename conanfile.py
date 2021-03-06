from conans import ConanFile, CMake, tools


class PistacheConan(ConanFile):
    name = "pistache"
    version = "1.0"
    license = "Apache License 2.0"
    url = "https://github.com/oktal/pistache"
    description = "A high-performance REST Toolkit written in C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/oktal/pistache")
        self.run("cd pistache")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="pistache")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="pistache/include")
        self.copy("*pistache.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["pistache"]

