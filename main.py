import geopy.distance

coords_1 = (40.6686937229748, 22.9142040721329) #device location
coords_2 = (40.67721956797799, 22.91907569168481) #others person location

print(geopy.distance.geodesic(coords_1, coords_2).km)