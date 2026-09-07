# Windows Commands

Jalankan semua perintah dari **root project**.

## Pemeriksaan awal
```powershell
python preflight.py
```

## Delivery checks bertahap
```powershell
python quality_checks/01_environment.py
python quality_checks/02_schema.py
python quality_checks/03_master.py
python quality_checks/04_relations.py
python quality_checks/05_full_pipeline.py
```

## Build dan validasi akhir
```powershell
python run_pipeline.py
python validate_delivery.py
```

## Notebook
```powershell
jupyter notebook notebooks\SQLite_Warehouse_Review.ipynb
```
