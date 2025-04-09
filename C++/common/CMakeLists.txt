
add_library(
        project_euler_common
        STATIC
        generators.cpp
        generators.hpp
        numeric_properties.hpp
)

generate_export_header(project_euler_common)

if (${CMAKE_CXX_COMPILER_ID} IN_LIST GCC_SYNTAX_COMPILER_IDS)
    target_compile_options(
            project_euler_common
            # Enable full optimisation for local CPU
            PUBLIC -march=native
            # Enable additional warnings
            PUBLIC -Wall -Wextra -Wpedantic -pedantic-errors
    )
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL "MSVC")
    target_compile_options(
            project_euler_common
            # Enable additional warnings
            PUBLIC /W4
    )
endif ()

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

target_link_libraries(
        project_euler_common
        PUBLIC PkgConfig::libcoro
)