import sys
sys.path.append('/home/rishi/icp_ws/src/static_marker/test')
from marvelmind_interfaces.msg import HedgePos, HedgeImuFusion
import testable_marker
from testable_marker import MarkerArrayPublisher
from visualization_msgs.msg import MarkerArray, Marker
marker = MarkerArrayPublisher()

# Testfall 3:  Überprüfung der korrekten Darstellung der Ampel 1 entsprechend seiner Position
def test_ampel_1():
    msg = Marker()
    msg.id = 1
    output = marker.publish_marker_array(msg)
    #print(output[0])
    assert output == "Ampel1"
    
# Testfall 4:  Überprüfung der korrekten Darstellung der Ampel 2 entsprechend seiner Position
def test_ampel_2():
    msg = Marker()
    msg.id = 2 
    output = marker.publish_marker_array(msg)
    assert output == "Ampel2"


# Testfall 5:  Überprüfung der korrekten Darstellung der Ampel 3 entsprechend seiner Position
def test_ampel_3():
    msg = Marker()
    msg.id = 3   
    output = marker.publish_marker_array(msg)
    assert output == "Ampel3"

# Testfall 6:  Überprüfung der korrekten Darstellung der Ampel 4 entsprechend seiner Position
def test_ampel_4():
    msg = Marker()
    msg.id = 4    
    output = marker.publish_marker_array(msg)
    assert output == "Ampel4"

# Testfall 7:  Überprüfung der korrekten Darstellung der Ampel 5 entsprechend seiner Position
def test_ampel_5():
    msg = Marker()
    msg.id = 5    
    output = marker.publish_marker_array(msg)
    assert output == "Ampel5"

# Testfall 8:  Überprüfung der korrekten Darstellung der Ampel 8 entsprechend seiner Position
def test_ampel_8():
    msg = Marker()
    msg.id = 8
    output = marker.publish_marker_array(msg)
    assert output == "Ampel8"

# Testfall 9:  Überprüfung der korrekten Darstellung der Ampel 9 entsprechend seiner Position
def test_ampel_9():
    msg = Marker()
    msg.id = 9
    output = marker.publish_marker_array(msg)
    assert output == "Ampel9"