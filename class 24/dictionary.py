ln = {"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
      "base":"stations","main":{"temp":285.91,"feels_like":284.6,"temp_min":285.25,"temp_max":287.14,"pressure":1023,"humidity":52,"sea_level":1023,
                                "grnd_level":1019},"visibility":10000,"wind":{"speed":3.13,"deg":99,"gust":6.26},"clouds":{"all":75},"dt":1776702495,
                                "sys":{"type":2,"id":268730,"country":"GB","sunrise":1776660860,"sunset":1776711849},"timezone":3600,
                                "id":2643743,"name":"London","cod":200}
print (ln["main"]["temp"])
print (ln["main"]["humidity"])
print (ln["name"])
print (ln["main"]["feels_like"])

#access temp, humidity, city name, feels like