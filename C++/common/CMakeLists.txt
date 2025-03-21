
add_library(
        project_euler_common
        STATIC
        fibonacci.cpp
        fibonacci.hpp
)

generate_export_header(project_euler_common)

target_include_directories(
        project_euler_common
        PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
        PUBLIC ${CMAKE_CURRENT_BINARY_DIR}
)

set_target_properties(
        project_euler_common
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        POSITION_INDEPENDENT_CODE ON
        INTERPROCEDURAL_OPTIMIZATION ${LTO_SUPPORTED}
)