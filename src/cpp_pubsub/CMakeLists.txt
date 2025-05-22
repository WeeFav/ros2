cmake_minimum_required(VERSION 3.8)
project(cpp_pubsub)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(mypublisher src/mypublisher.cpp)
ament_target_dependencies(mypublisher rclcpp std_msgs)
add_executable(mysubscriber src/mysubscriber.cpp)
ament_target_dependencies(mysubscriber rclcpp std_msgs)

install(TARGETS
  mypublisher
  mysubscriber
  DESTINATION lib/${PROJECT_NAME})

ament_package()
