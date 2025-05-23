echo Reminder: Sind alle Team URL Datein up-to-date?
pause
cd scripts
python logoscraper_prm.py
python logoscraper_opl.py
echo Scraping fertig! (ob erfolgreich oder nicht, schaue in die obigen Nachrichten)
pause