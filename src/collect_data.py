import requests

countries = "AT+BE+BG+HR+CY+CZ+DK+EE+FI+FR+DE+EL+HU+IE+IT+LV+LT+LU+MT+NL+PL+PT+RO+SK+SI+ES+SE"

url = f"https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/prc_ppp_ind_1/A.VI_PPS_EU27_2020_HAB.GDP.{countries}"

params = {
    "format": "SDMX-CSV",
    "startPeriod": "2000",
    "endPeriod": "2025"
}
##Hämta data från API
response = requests.get(url, params=params)
#Se till att förfrågan lyckades
response.raise_for_status()

# Spara rådatan från Eurostat
with open("data/raw/gdp_pps.csv", "wb") as file:
    file.write(response.content)