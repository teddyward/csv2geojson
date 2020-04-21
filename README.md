# csv2geojson

Converts a CSV with WKT features to geojson

I wrote this in 5 minutes and will therefore probably not provide support if anyone stumbles across this.

[Mapbox's tool](https://github.com/mapbox/csv2geojson) may "magically" handle more edge cases, but they can't support really big files, so it doesn't work for my use case.

Usage:

```
python csv2geojson.py -f ~/path/to/your/file.csv
```

or

```
python csv2geojson.py path/to/file.csv [new_file].geojson
```
