from gps3 import agps3
gps_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()
gps_socket.HOST = 'localhost'
gps_socket.GPSD_PORT = '8000'
gps_socket.PROTOCOL = 'json'
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['alt'])
        print('Latitude = ', data_stream.TPV['lat'])