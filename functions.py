from imports import *

def salvar_sqlite(registros, db_path='noticias.db'):
    if not registros:
        return 0

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paginas_html (
            id TEXT PRIMARY KEY,
            fonte TEXT,
            titulo TEXT,
            link TEXT,
            html TEXT,
            resumo TEXT,
            data_publicacao TEXT,
            envio INTEGER DEFAULT 0
        )
    """)

    inseridos = 0
    for r in registros:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO paginas_html
                (id, fonte, titulo, link, html, resumo, data_publicacao, envio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                r['id'],
                r['fonte'],
                r['titulo'],
                r['link'],
                r.get('html', ''),
                r.get('resumo', ''),
                r.get('data_publicacao', ''),
                r['envio']
            ))
            inseridos += cursor.rowcount
        except Exception as e:
            print(f"❌ Erro ao inserir {r['titulo']}: {e}")

    conn.commit()
    conn.close()
    return inseridos


def coleta_RSS(feeds, db_path='noticias.db'):
    """Coleta feeds JSON do BCB e salva no SQLite"""
    todos_registros = []

    for nome_base, url in feeds.items():
        print(f"\n🔹 Processando feed: {nome_base} ({url})")
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"❌ Erro ao carregar o feed: {url} | {e}")
            continue

        registros = []

        # Ajustar conforme a estrutura JSON de cada feed
        if nome_base == 'noticias':
            items = data.get('items', [])
        elif nome_base == 'normativos':
            items = data.get('normativos', [])
        elif nome_base == 'notas_imprensa':
            items = data.get('notas', [])
        else:
            items = []

        for item in items:
            titulo = item.get('titulo') or item.get('assunto') or 'Sem título'
            link = item.get('link') or ''
            data_pub = item.get('dataPublicacao') or ''
            resumo = item.get('resumo') or ''

            hash_id = hashlib.md5((titulo + link).encode('utf-8')).hexdigest()

            # Opcional: baixar HTML da página
            try:
                html = requests.get(link).text if link else ''
            except:
                html = ''

            registros.append({
                'fonte': nome_base,
                'titulo': titulo,
                'link': link,
                'data_publicacao': data_pub,
                'resumo': resumo,
                'html': html,
                'id': hash_id,
                'envio': 0
            })

        if registros:
            novos = salvar_sqlite(registros, db_path)
            print(f"💾 {novos} novos registros inseridos no SQLite para {nome_base}")
            todos_registros.extend(registros)
        else:
            print("⚠️ Nenhum item encontrado neste feed.")

    if todos_registros:
        print(f"\n📊 Total de registros processados: {len(todos_registros)}")
    else:
        print("\n⚠️ Nenhum dado novo para processar.")
