# DaVinci

DaVinci Consumer Mobile API application built using Django Rest Framework

## Apps

- Authentication
- Horoscope
- Songs
- Mantras
- Match Making


#### Authentication:
#### Authenticate the device to use other apps.
- GET /Authentication​/DeviceLogin​/{device_auth}​/
- Device auth should be of 16 characters

### Horoscope:
#### Daily horoscope refers to predictions given for a day. Generally daily predictions are based on the Sun signs or the Zodiac signs. This method considers the position of the Sun in a particular zodiac sign at the time the person was born. A more precise method of writing daily horoscope is based on studying all the parameters of an individual’s birth chart including the movements of the fast and slow moving planets.
- POST /Horoscope/CheckAstrology/{device_auth}/
- Payload

```json
{
 "day":"today",
 "sign":"aries",
 "timezone":"Asia/Kolkata"
}
```
- Accepted signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]
-  Accepted days = [
    'today', 'tomorrow', 'yesterday'
]

### Songs:
#### Songs app to play devotional songs
- GET /Songs/Albums/{device_auth}/ to get albums
- GET /Songs/Songs/{album_id}/{device_auth}/ to get songs against album id
- GET /Songs/SongLyrics/{album_id}/{device_auth}/ to get lyrics against album id

### Mantras:
#### Mantras app to play Mantras
- GET /Mantras/MantrasAlbums/{device_auth}/ to get albums
- GET /Mantras/Mantras/{album_id}/{device_auth}/ to get songs against album id
- GET /Mantras/MantraLyrics/{album_id}/{device_auth}/ to get lyrics against album id


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
