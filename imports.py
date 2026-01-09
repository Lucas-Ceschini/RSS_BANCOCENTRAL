from datetime import datetime, date
import glob
import os
import hashlib
import requests
import pandas as pd 
import re
import sqlite3
import mysql.connector
import feedparser

global username
username = os.getenv('USERNAME')

# URL do feed RSS do Banco Central (exemplo: notícias)
RSS_URL1 = "https://www.bcb.gov.br/api/feed/sitebcb/sitefeeds/noticias?ano=2024"
RSS_URL2 = "https://www.bcb.gov.br/api/feed/app/normativos/normativos?ano=2021"
RSS_URL3 = "https://www.bcb.gov.br/api/feed/sitebcb/sitefeeds/notasImprensa?ano=2021"

# Faz o parsing do feed RSS 
feeds_bacen = {
    'noticias': RSS_URL1,
    'normativos':RSS_URL2,
    'notas_imprensa':RSS_URL3
}

# Pastas e destinatários 
arquivos = ['noticias', 'normativos', 'notas_imprensa']

