from geolocation.main import GoogleMaps

def distance():

    origins = input('Please give the name of the city: ')
    destinations = input('Please give the name of the second city: ')
    
    google_maps = GoogleMaps(api_key='')
    
    items = google_maps.distance(origins, destinations).all()  
    
    for item in items:
        print('From: %s' % item.origin)
        print('To: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)

distance()