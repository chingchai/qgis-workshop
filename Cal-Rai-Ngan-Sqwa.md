# การคำนวณเนื้อที่ไร่ งาน และตารางวา ในโปรแกรม QGIS
## 1. create field RAI NGAN and SQRWA in QGIS
  * RAI type integer length 5
  * NGAN type integer length 5
  * SQRWA type double length 10,2
  
## 2. calculate field RAI in QGIS
  ```c
    floor($area/1600)
  ```
## 3. calculate field NGAN in QGIS
   ```c
    floor((($area/1600)-"RAI")*4)
  ```  
## 4. calculate field SQRWA in QGIS
   ```c
     (((($area/1600)-"RAI")*4)-"NGAN")*100
