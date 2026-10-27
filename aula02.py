import cv2
from pyzbar import pyzbar

imagem = cv2.imread('coca cola espumante.jpg')

if imagem is None:
    print('[erro] não foi possível carregar a imagem. Verifique o nome do arquivo.')
else:
    print('[sucesso] imagem carregada com sucesso')

codigos = pyzbar.decode(imagem)

if not codigos:
    print('[aviso] nenhum código foi encontrado na imagem.')
else:
    for codigo in codigos:
        dados_str = codigo.data.decode('utf-8')
        tipo_codigo = codigo.type

        print(f"[lido] tipo: {tipo_codigo} conteúdo: [{dados_str}]")

        (x, y, w, h) = codigo.rect

        cv2.rectangle(
            imagem,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        texto_exibicao = f"{tipo_codigo}: {dados_str}"

        cv2.putText(
            imagem,
            texto_exibicao,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

# Exibe a imagem final na tela e aguarda pressionar uma tecla para fechar
cv2.imshow('Rastreabilidade Industrial', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()