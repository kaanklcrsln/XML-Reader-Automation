# XML Metadata Automation Script

This Python script extracts key metadata from satellite processing XML files and outputs the results in a structured JSON format.  
It is designed to read `package.xml` and multiple `band.xml` files located in a defined directory hierarchy.

## Features
- Parses satellite metadata from XML files  
- Extracts specific values such as dataset name, production date, band information, and processing parameters  
- Handles missing or malformed XML files gracefully  
- Outputs consolidated data as formatted JSON

## Directory Structure
xml-otomasyon/
└── seviyeler/
└── L1/
├── package.xml
├── 0/band.xml
├── 1/band.xml
├── 2/band.xml
└── 3/band.xml

## Usage
1. Place the XML files under the specified directory (`xml-otomasyon/seviyeler/L1`).  
2. Run the script:
   ```bash
   python main.py

## Output Example
{
  "package": {
    "satellite": "Pleiades-1A",
    "name": "L1_DATASET_001",
    "date": "2025-04-01T12:00:00",
    "job_id": "12345",
    "nbands": "4"
  },
  "bands": {
    "0": {
      "band_id": "1",
      "resolution": "0.5",
      "gain": "1.2",
      "imaging_date": "2025-04-01",
      "format": "GeoTIFF"
    }
  }
}

#Requirements
Python 3.8 or higher
No external dependencies (uses only built-in libraries)
