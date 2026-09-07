# Windows Engineering Runbook

Jalankan semua perintah dari **root project**.

## Repository preflight
```powershell
python preflight.py
```

## Incremental quality gates
```powershell
python quality_checks/01_environment.py
python quality_checks/02_schema.py
python quality_checks/03_master.py
python quality_checks/04_relations.py
python quality_checks/05_full_pipeline.py
```

## Clean build dan final validation
```powershell
python run_pipeline.py
python validate_delivery.py
```

## Review console
```powershell
jupyter notebook notebooks\SQLite_Warehouse_Review.ipynb
```
