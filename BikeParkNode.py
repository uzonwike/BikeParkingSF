import math
EARTH_RADIUS=6371000

class BikeParkNode():
    def __init__(self,address,location,street_name,racks,spaces,placement,mo_installed, yr_installed,Lat,Long):
        self.location=location
        self.street_name=street_name
        self.racks=racks
        self.spaces=spaces
        self.yr_installed=yr_installed
        self.mo_installed=mo_installed
        self.Lat=Lat
        self.Long=Long
        self.placement=placement
        self.address=address

    def computeDistance(self,Lat, Long):
        "d=r*sqrt(theta1-square+theta2-square-2*theta1*theta2*cos(delta-gamma))"
        
        dif_Lat=math.radians(self.Lat)-math.radians(Lat)
        dif_Long=math.radians(self.Long)-math.radians(Long)
        theta_1=(math.pi/2)-math.radians(self.Lat)
        theta_2=(math.pi/2)-math.radians(Lat)
        dist_unfactored_square=(theta_1*theta_1)+(theta_2*theta_2)-((2*(theta_1*theta_2))*math.cos(dif_Long))
        dist_unfactored=math.sqrt(dist_unfactored_square)
        dist_factored=EARTH_RADIUS*dist_unfactored
        return dist_factored


"""def main():
#tester main
#should print the distance between lagos and new york
    Node1=BikeParkNode("a","b","c","d","e","f","g",6.4531,3.3958)
    Node2=BikeParkNode("a","b","c","d","e","f","g",40.7127,-74.0059)
    print Node1.computeDistance(Node2.Lat,Node2.Long)/1000

main()"""
        
        
        
