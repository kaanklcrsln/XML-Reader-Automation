import os, xml.etree.ElementTree as ET, json

# XML dosyasından belirli bir yoldaki değeri al
def get_val(root, path):  
    tag = root.find(path)
    return tag.text.strip() if tag is not None and tag.text else "Unknown"

# İşleme parametrelerini bul ve değerini getir
def get_param(root, desc):  
    for p in root.findall(".//Processing_Parameter"):
        if get_val(p, "PROC_PARAMETER_DESC") == desc:
            return get_val(p, "PROC_PARAMETER_VALUE")
    return "Unknown"

# Ana klasör yolu
base = r"xml-otomasyon\seviyeler\L1"
data = {'package': {}, 'bands': {}}

# package.xml dosyasını oku - önce dosya var mı kontrol et
pkg_path = os.path.join(base, "package.xml")
if os.path.exists(pkg_path):
    try:
        p = ET.parse(pkg_path).getroot()
        print(f"Package XML kök elementi: {p.tag}")  # Debug için
        
        # Tüm etiketleri görelim
        for elem in p.iter():
            if elem.text and elem.text.strip():
                print(f"  {elem.tag}: {elem.text.strip()}")
        
        data['package'] = {
            'satellite': get_val(p, ".//DATASET_SERIES"),      
            'name': get_val(p, ".//DATASET_NAME"),             
            'date': get_val(p, ".//DATASET_PRODUCTION_DATE"),  
            'job_id': get_val(p, ".//JOB_ID"),                 
            'nbands': get_val(p, ".//NBANDS")                  
        }
    except Exception as e:
        print(f"Package XML hatası: {e}")
else:
    print(f"Package XML dosyası bulunamadı: {pkg_path}")

# Her band için (0,1,2,3) band.xml dosyasını oku
for i in map(str, range(4)):
    band_path = os.path.join(base, i, "band.xml")
    if os.path.exists(band_path):
        try:
            b = ET.parse(band_path).getroot()
            print(f"Band {i} XML kök elementi: {b.tag}")  # Debug için
            
            data['bands'][i] = {
                'band_id': get_val(b, ".//BAND_INDEX"),              
                'resolution': get_param(b, "SAMPLING_STEP_X"),       
                'gain': get_param(b, "GAIN"),                        
                'imaging_date': get_val(b, ".//IMAGING_DATE"),       
                'format': get_val(b, ".//DATA_FILE_FORMAT")          
            }
        except Exception as e:
            print(f"Band {i} XML hatası: {e}")
    else:
        print(f"Band {i} XML dosyası bulunamadı: {band_path}")

# Sonucu JSON formatında yazdır
print(json.dumps(data, indent=2, ensure_ascii=False))
