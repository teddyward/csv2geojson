import argparse
import pandas as pd
from shapely.geometry import shape
from shapely.wkt import loads
from geojson import Feature, FeatureCollection

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        type=str,
        help='filepath to convert')
    parser.add_argument(
        'output_file', default='output',
        type=str,
        help='file to output to')
    args = parser.parse_args()
    file_path = args.file_path
    output_file = args.output_file
    features = []
    csv_features = pd.read_csv(file_path)
    for _i, feature in csv_features.iterrows():
        geometry = loads(feature['geometry'])
        del feature['geometry']
        features.append(
            Feature(geometry=geometry, properties=feature.dropna().to_dict()))
    collection = FeatureCollection(features)
    with open(f'{output_file}.json', 'w') as f:
        f.write('%s' % collection)