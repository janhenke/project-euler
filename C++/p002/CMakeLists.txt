add_executable(
        p002
        main.cpp
)

set_target_properties(
        p002
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        POSITION_INDEPENDENT_CODE ON
        INTERPROCEDURAL_OPTIMIZATION ${LTO_SUPPORTED}
)

target_link_libraries(
        p002
        PUBLIC project_euler_common
)