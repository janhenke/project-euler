
add_library(
        project_euler_common
        STATIC
        library.cpp
)

target_include_directories(
        project_euler_common
        PUBLIC ${CMAKE_SOURCE_DIR}
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