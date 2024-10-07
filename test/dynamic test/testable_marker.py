import rclpy
from rclpy.node import Node
from visualization_msgs.msg import MarkerArray, Marker

class MarkerArrayPublisher(Node):
    def __init__(self):
        rclpy.init()
        super().__init__('marker_array_publisher')
        self.publisher = self.create_publisher(MarkerArray, 'ampel', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        
    def publish_marker_array(self,msg):     
        
        self.marker_array_msg = MarkerArray()
        self.ampel1_r = Marker()
        self.ampel1_r.header.frame_id = "map"
        self.ampel1_r.ns = "traffic_signal_red"
        self.ampel1_r.id = 1
        self.ampel1_r.type = Marker.MESH_RESOURCE
        self.ampel1_r.action = Marker.ADD
        self.ampel1_r.pose.position.x = 3.8
        self.ampel1_r.pose.position.y = 4.1
        self.ampel1_r.pose.position.z = 0.001
        self.ampel1_r.scale.x = 0.025
        self.ampel1_r.scale.y = 0.025
        self.ampel1_r.scale.z = 0.025
        self.ampel1_r.color.r = 0.0
        self.ampel1_r.color.g = 0.0
        self.ampel1_r.color.b = 1.0
        self.ampel1_r.color.a = 1.0
        self.ampel1_r.pose.orientation.z =  0.0
        self.ampel1_r.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t5r.stl"
        self.marker_array_msg.markers.append(self.ampel1_r)

        self.ampel1_g = Marker()
        self.ampel1_g.header.frame_id = "map"
        self.ampel1_g.ns = "traffic_signal_green"
        self.ampel1_g.id = 21
        self.ampel1_g.type = Marker.MESH_RESOURCE
        self.ampel1_g.action = Marker.ADD
        self.ampel1_g.pose.position.x = 3.78
        self.ampel1_g.pose.position.y = 4.0
        self.ampel1_g.pose.position.z = 0.001
        self.ampel1_g.scale.x = 0.025
        self.ampel1_g.scale.y = 0.025
        self.ampel1_g.scale.z = 0.025
        self.ampel1_g.color.r = 0.0
        self.ampel1_g.color.g = 0.0
        self.ampel1_g.color.b = 1.0
        self.ampel1_g.color.a = 1.0
        self.ampel1_g.pose.orientation.z =  0.0
        self.ampel1_g.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t43.stl"
        self.marker_array_msg.markers.append(self.ampel1_g)

        self.ampel2 = Marker()
        self.ampel2.header.frame_id = "map"
        self.ampel2.ns = "ampel2"
        self.ampel2.id = 2
        self.ampel2.type = Marker.MESH_RESOURCE
        self.ampel2.action = Marker.ADD
        self.ampel2.pose.position.x = 3.8
        self.ampel2.pose.position.y = 2.2
        self.ampel2.pose.position.z = 0.001
        self.ampel2.scale.x = 0.015
        self.ampel2.scale.y = 0.015
        self.ampel2.scale.z = 0.015
        self.ampel2.color.r = 0.0
        self.ampel2.color.g = 0.0
        self.ampel2.color.b = 1.0
        self.ampel2.color.a = 1.0
        self.ampel2.pose.orientation.z =  0.0  # -90 deg in Euler
        self.ampel2.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t43.stl"
        self.marker_array_msg.markers.append(self.ampel2)

        self.ampel3 = Marker()
        self.ampel3.header.frame_id = "map"
        self.ampel3.ns = "ampel3"
        self.ampel3.id = 3
        self.ampel3.type = Marker.MESH_RESOURCE
        self.ampel3.action = Marker.ADD
        self.ampel3.pose.position.x = 2.8
        self.ampel3.pose.position.y = 2.3
        self.ampel3.pose.position.z = 0.001
        self.ampel3.scale.x = 0.015
        self.ampel3.scale.y = 0.015
        self.ampel3.scale.z = 0.015
        self.ampel3.color.r = 0.0
        self.ampel3.color.g = 0.0
        self.ampel3.color.b = 1.0
        self.ampel3.color.a = 1.00
        self.ampel3.pose.orientation.z =  0.0
        self.ampel3.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t43.stl"
        self.marker_array_msg.markers.append(self.ampel3)

        self.ampel4 = Marker()
        self.ampel4.header.frame_id = "map"
        self.ampel4.ns = "ampel4"
        self.ampel4.id = 4
        self.ampel4.type = Marker.MESH_RESOURCE
        self.ampel4.action = Marker.ADD
        self.ampel4.pose.position.x = 2.8
        self.ampel4.pose.position.y = 3.3
        self.ampel4.pose.position.z = 0.001
        self.ampel4.scale.x = 0.015
        self.ampel4.scale.y = 0.015
        self.ampel4.scale.z = 0.015
        self.ampel4.color.r = 0.0
        self.ampel4.color.g = 0.0
        self.ampel4.color.b = 1.0
        self.ampel4.color.a = 1.00
        self.ampel4.pose.orientation.z =  0.0
        self.ampel4.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t44.stl"
        self.marker_array_msg.markers.append(self.ampel4)

        self.ampel5 = Marker()
        self.ampel5.header.frame_id = "map"
        self.ampel5.ns = "ampel5"
        self.ampel5.id = 5
        self.ampel5.type = Marker.MESH_RESOURCE
        self.ampel5.action = Marker.ADD
        self.ampel5.pose.position.x = 0.9
        self.ampel5.pose.position.y = 3.3
        self.ampel5.pose.position.z = 0.001
        self.ampel5.scale.x = 0.015
        self.ampel5.scale.y = 0.015
        self.ampel5.scale.z = 0.015
        self.ampel5.color.r = 0.0
        self.ampel5.color.g = 0.0
        self.ampel5.color.b = 1.0
        self.ampel5.color.a = 1.00
        self.ampel5.pose.orientation.z =  0.0
        self.ampel5.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t45.stl"
        self.marker_array_msg.markers.append(self.ampel5)

        self.ampel8 = Marker()
        self.ampel8.header.frame_id = "map"
        self.ampel8.ns = "ampel8"
        self.ampel8.id = 8
        self.ampel8.type = Marker.MESH_RESOURCE
        self.ampel8.action = Marker.ADD
        self.ampel8.pose.position.x = 0.9
        self.ampel8.pose.position.y = 2.2
        self.ampel8.pose.position.z = 0.001
        self.ampel8.scale.x = 0.015
        self.ampel8.scale.y = 0.015
        self.ampel8.scale.z = 0.015
        self.ampel8.color.r = 0.0
        self.ampel8.color.g = 0.0
        self.ampel8.color.b = 1.0
        self.ampel8.color.a = 1.00
        self.ampel8.pose.orientation.z =  0.0
        self.ampel8.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t48.stl"
        self.marker_array_msg.markers.append(self.ampel8)    
        
        self.ampel9 = Marker()
        self.ampel9.header.frame_id = "map"
        self.ampel9.ns = "ampel9"
        self.ampel9.id = 9
        self.ampel9.type = Marker.MESH_RESOURCE
        self.ampel9.action = Marker.ADD
        self.ampel9.pose.position.x = 0.0
        self.ampel9.pose.position.y = 3.2
        self.ampel9.pose.position.z = 0.001
        self.ampel9.scale.x = 0.015
        self.ampel9.scale.y = 0.015
        self.ampel9.scale.z = 0.015
        self.ampel9.color.r = 0.0
        self.ampel9.color.g = 0.0
        self.ampel9.color.b = 1.0
        self.ampel9.color.a = 1.00
        self.ampel9.pose.orientation.z =  0.0
        self.ampel9.mesh_resource = "file:///home/rishi/icp_ws/src/pose2car/marker/model/t49.stl"
        self.marker_array_msg.markers.append(self.ampel9)
        
        z = msg.id #Klasse des Objektes

        if z == 1:
           self.ampel1_r.id = 1
           self.ampel1_r.pose.position.x = 3.8
           self.ampel1_r.pose.position.y = 4.1
           self.ampel1_r.pose.position.z = 0.001
           classe = "Ampel1"
        elif z == 2:
            self.ampel2.id = 2
            self.ampel2.pose.position.x = 3.8
            self.ampel2.pose.position.y = 2.2
            self.ampel2.pose.position.z = 0.001
            classe = "Ampel2"
        elif z == 3:
            self.ampel3.id = 3
            self.ampel3.pose.position.x = 2.8
            self.ampel3.pose.position.y = 2.3
            self.ampel3.pose.position.z = 0.001
            classe = "Ampel3"
        elif z == 4:
            self.ampel4.id = 4
            self.ampel4.pose.position.x = 2.8
            self.ampel4.pose.position.y = 3.3
            self.ampel4.pose.position.z = 0.001
            classe = "Ampel4"
        elif z == 5:
            self.ampel5.id = 5
            self.ampel5.pose.position.x = 0.9
            self.ampel5.pose.position.y = 3.3
            self.ampel5.pose.position.z = 0.001
            classe = "Ampel5"
        elif z == 8:
            self.ampel8.id = 8
            self.ampel8.pose.position.x = 0.9
            self.ampel8.pose.position.y = 2.2
            self.ampel8.pose.position.z = 0.001
            classe = "Ampel8"
        elif z == 9:
            self.ampel9.id = 9
            self.ampel9.pose.position.x = 0.0
            self.ampel9.pose.position.y = 3.2
            self.ampel9.pose.position.z = 0.001
            classe = "Ampel9"     


        self.publisher.publish(self.marker_array_msg)
        return classe

    def timer_callback(self):
        self.publish_marker_array()

def main(args=None):
    rclpy.init(args=args)
    marker_array_publisher = MarkerArrayPublisher()
    rclpy.spin(marker_array_publisher)
    marker_array_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
