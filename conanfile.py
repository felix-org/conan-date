from conans import ConanFile, CMake, tools


class DateConan(ConanFile):
    name = "Date"
    version = "2.4.1"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/HowardHinnant/date.git", "v2.4.1")

    def package(self):
        self.copy("*.h")

    def package_id(self):
        self.info.header_only()
