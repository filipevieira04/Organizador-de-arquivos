import os
import shutil

EXTENSOES = {
    # Documentos de texto
    ".txt": "Textos",
    ".doc": "Word",
    ".docx": "Word",
    ".odt": "Word",
    ".rtf": "Word",
    ".pdf": "PDF",

    # Planilhas
    ".xls": "Excel",
    ".xlsx": "Excel",
    ".xlsm": "Excel",
    ".ods": "Excel",
    ".csv": "Excel",

    # Apresentações
    ".ppt": "PowerPoint",
    ".pptx": "PowerPoint",
    ".odp": "PowerPoint",

    # Imagens
    ".jpg": "Fotos",
    ".jpeg": "Fotos",
    ".png": "Fotos",
    ".gif": "Fotos",
    ".bmp": "Fotos",
    ".svg": "Fotos",
    ".webp": "Fotos",
    ".tiff": "Fotos",
    ".ico": "Fotos",

    # Áudio
    ".mp3": "Audios",
    ".wav": "Audios",
    ".flac": "Audios",
    ".aac": "Audios",
    ".ogg": "Audios",
    ".m4a": "Audios",

    # Vídeo
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",

    # Compactados
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
    ".tar": "Compactados",
    ".gz": "Compactados",

    # Executáveis e instaladores
    ".exe": "Executaveis",
    ".msi": "Executaveis",
    ".apk": "Executaveis",

    # Código / Desenvolvimento
    ".py": "Codigo",
    ".js": "Codigo",
    ".html": "Codigo",
    ".css": "Codigo",
    ".java": "Codigo",
    ".c": "Codigo",
    ".cpp": "Codigo",
    ".json": "Codigo",
    ".xml": "Codigo",
    ".sql": "Codigo",

    # Fontes
    ".ttf": "Fontes",
    ".otf": "Fontes",
}


def organizar_pasta(caminho_base):
    if not os.path.isdir(caminho_base):
        print("Esse caminho não existe ou não é uma pasta.")
        return

    pastas_ja_criadas = set()

    # pega apenas os arquivos que já existem na pasta antes de começar,
    # evitando reprocessar arquivos que acabaram de ser movidos
    itens = os.listdir(caminho_base)

    for item in itens:
        caminho_item = os.path.join(caminho_base, item)

        # ignora o que não for arquivo (ex: pastas que já existiam)
        if not os.path.isfile(caminho_item):
            continue

        _, extensao = os.path.splitext(item)
        extensao = extensao.lower()

        categoria = EXTENSOES.get(extensao)

        if categoria is None:
            print(f"Extensão não reconhecida, ignorando: {item}")
            continue

        caminho_categoria = os.path.join(caminho_base, categoria)

        # só cria a pasta se ainda não foi criada nessa execução
        if categoria not in pastas_ja_criadas:
            os.makedirs(caminho_categoria, exist_ok=True)
            pastas_ja_criadas.add(categoria)

        destino = os.path.join(caminho_categoria, item)
        shutil.move(caminho_item, destino)
        print(f"Movido: {item} -> {categoria}")


if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta a ser organizada: ").strip().strip('"').strip("'")
    organizar_pasta(caminho)
    print("\nOrganização concluída!")