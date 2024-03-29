import mimetypes
import os
from pip._vendor.distlib.compat import raw_input
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import geojson

opdracht = 5
geojsonphotos = ""
outputfile = "photos.json"

### FROM https://gist.github.com/erans/983821
def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data

def _get_if_exist(data, key):
    if key in data:
        return data[key]

    return None

def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return lat, lon

def welcome():
    print("Welkom bij opdracht " + str(opdracht))
    print("Op het moment bevind u zich in: " + os.getcwd() + "\n")
    ansdir = raw_input("Welke map wil je afscannen? ")
    scandir(ansdir)


def isjpeg(item):
    if str(mimetypes.guess_type(item)[0]) == "image/pjpeg":
        return True
    else:
        return False


def prepairjson(jsonfile):
        f = open(jsonfile,'w')
        f.write('{"type": "FeatureCollection","features": [')
        f.close()


def endjson(jsonfile):
        f = open(jsonfile,'a')
        f.write(']}')
        f.close()


def prepairpointer(jsonfile):
        f = open(jsonfile,'a')
        f.write('{"type": "Feature","properties": {},"geometry": {')
        f.close()


def endpointer(jsonfile):
    print("okdoei")


def scandir(dir):
    for itemindir in os.listdir(dir):
        try:
            # print("Map is: " + dir)
            # print("Bestand is: " + itemindir)
            totaalpad= dir + "\\" + itemindir
            # print(totaalpad)
            if itemindir != "Thumbs.db":
                plaatje = Image.open(totaalpad)
                exif_data = get_exif_data(plaatje)
                coords = get_lat_lon(exif_data)
                print(itemindir + " " + str(geojson.Point((coords[0],coords[1]))))
                # f = open("photos.json",'a')
                # f.write(str(geojson.Point((coords[0],coords[1]))))
                # f.close()
        except

welcome()