cmake_minimum_required(VERSION 3.30)
project(ProjectEuler)

include(GenerateExportHeader)
include(CheckIPOSupported)
# check for LTO support in the compiler
check_ipo_supported(RESULT LTO_SUPPORTED)

set(GCC_SYNTAX_COMPILER_IDS AppleClang Clang GNU)

find_package(PkgConfig REQUIRED)
pkg_check_modules(libcoro REQUIRED IMPORTED_TARGET libcoro)

add_subdirectory(common)

add_subdirectory(p001)
add_subdirectory(p002)
add_subdirectory(p003)
add_subdirectory(p004)
