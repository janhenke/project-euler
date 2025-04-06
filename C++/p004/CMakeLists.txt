add_executable(
        p004
        main.cpp
)

set_target_properties(
        p004
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        POSITION_INDEPENDENT_CODE ON
        INTERPROCEDURAL_OPTIMIZATION ${LTO_SUPPORTED}
)

target_link_libraries(
        p004
        PUBLIC project_euler_common
)