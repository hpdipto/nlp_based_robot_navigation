

import sys
import model_loading

# curson hall > shahidullah hall > ekushey hall > fh hall > tsc


position_list = [(23.727603,90.400462), (23.725308,90.400351), (23.724079,90.403107), (23.7264259, 90.4028827), (23.7322261,90.3960900)]
zoom = 16

location_data = {
	"Curzon Hall": (23.727603,90.400462), "Dr. Muhammad Shahidullah Hall": (23.725308,90.400351),
	"Amar Ekushey Hall": (23.724079,90.403107), "Fazlul Haque Muslim Hall": (23.7264259, 90.4028827),
	"TSC": (23.7322261,90.3960900), "Shaheed Minar": (23.727377,90.397434), "Bangla Academy": (23.730142,90.398139),
	"Dhaka Medical College Hospital": (23.726179, 90.398670)
}



input_text = [sys.argv[1]]

locations = model_loading.get_location(input_text)
# locations = ["Dhaka Medical College Hospital", "Dr. Muhammad Shahidullah Hall", "Bangla Academy"]

# link = "https://www.mapquest.com/embed/directions/list/1/near-23.727603,90.400462/to/near-23.725308,90.400351/to/near-23.724079,90.403107/to/near-23.7264259,90.4028827/to/near-23.7322261,90.39609?center=23.728137063884265,90.39963550000003&zoom=17&maptype=map"


route_link = "https://www.mapquest.com/embed/directions/list/1/"
# link_extension = f"?center={position_list[0][0]},{position_list[0][1]}&zoom={zoom}&maptype=map"


if len(locations) > 1:
	for i, location in enumerate(locations):
		loc = location_data[location]

		add = f"near-{loc[0]},{loc[1]}/"
		if (i != len(locations)-1):
			add += "to/"
		route_link += add
else:
	lat = location_data[locations[0]][0]
	long_ = location_data[locations[0]][1]
	route_link = f"https://www.mapquest.com/embed/latlng/{lat},{long_}"

# route_link = route_link[:-1] + link_extension

print(route_link)
