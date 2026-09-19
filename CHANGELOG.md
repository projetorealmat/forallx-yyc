# Resumo das alterações

## Alterações da edição do outono de 2025

- A terminologia para _demonstravelmente equivalentes_ foi substituída por _interderiváveis_.
- A discussão da relação entre noções semânticas e teóricas da prova foi cuidadosamente revisada.
- Regras para subprovas foram acrescentadas ao apêndice de referência rápida.
- Muitos erros de digitação e erros menores foram corrigidos.

## Alterações da edição do outono de 2023

- Versão HTML plenamente acessível e pacotes SCORM usando BookML
  ([issue 23](https://github.com/rzach/forallx-yyc/issues/23)). Isso
  exigiu muitas alterações internas; veja a [publicação sobre os
  detalhes técnicos](https://richardzach.org/2023/07/converting-latex-to-html-technical-notes/).
- As provas agora identificam premissas por PR e suposições por AS (o que
  ajuda na acessibilidade e aproxima o livro das convenções do Carnap).
- Novo capítulo 13 (Limitações da Lógica da Linguagem Formal), baseado em parte na seção 12.5 da edição F21.
- Novo capítulo 35 (Propriedades das relações).
- Remoção do esboço confuso da prova de correção do capítulo 22 ([issue 66](https://github.com/rzach/forallx-yyc/issues/66)).
- A seção 30.4 (Satisfação de fórmulas) foi transferida para a seção 32.2 (Expressibilidade) e ampliada.
- Soluções acrescentadas aos exercícios dos capítulos 7 e 29 (Ambiguidade).
- Explicação acrescentada sobre a restrição de quantificadores ao final da seção 25.4 ([issue 57](https://github.com/rzach/forallx-yyc/issues/57)).
- Material acrescentado à seção 27.3 sobre quantificação vacuamente verdadeira; as definições de substituição foram revistas para substituir apenas ocorrências livres de variáveis; e a seção 36.6 foi acrescentada para explicar o que pode dar errado quando não se toma cuidado com a substituição ([issue 77](https://github.com/rzach/forallx-yyc/issues/77)).
- Revisões da seção 4.2 para alinhá-la à terminologia do capítulo 3.
- Breve discussão acrescentada sobre o uso assimétrico de “e” na seção 5.2.
- Muitas revisões menores, correções de erros de digitação e ajustes de formatação.

## Alterações da edição do outono de 2021

- Acrescentado o capítulo 45, sobre cadeias de equivalências.
- Acrescentada ao capítulo uma discussão sobre “somente” e “exceto”.
- Muitas correções de ortografia e gramática.
- Notas para instrutores no Prefácio.

## Alterações da edição do outono de 2020

- Reorganização interna dos arquivos (por exemplo, agora usa um `fitch.sty` padrão; `forallxyyc-style.sty` contém apenas os elementos de formatação separados de `forallxyyc.sty`, para que este último possa ser usado em slides Beamer).
- “Expressivamente adequado” foi renomeado como “funcionalmente completo”.
- Incorporação de algumas alterações da versão de Cambridge.
- O capítulo “Sentenças da LPO” foi movido para antes do capítulo “Descrições definidas”.
- Acrescentados dois capítulos sobre ambiguidade (7 e 28).
- Acrescentado “somente” à seção 23.1.
- O capítulo sobre formas normais e completude funcional foi dividido em dois.
- Corrigidos alguns erros de digitação.

## Alterações da edição do outono de 2019

- Novo projeto de capa de Mark Lyall.
- Capítulos 1–3 reescritos/revisados, evitando a modalidade ao definir validade e falando, em vez disso, de “casos” (como fazem JC Beall e Shay Logan em seu livro _Logic: The Basics_).
- A sintaxe da LPO foi alterada: as fórmulas agora são F(x, y), em vez de Fxy. Isso pode ser personalizado em `forallxyyc-local.sty`.
- Alterada parte da terminologia: “consistência lógica” passou a ser “satisfazibilidade” (e cognatos), e “verdades lógicas” passaram a ser “valididades”.
- Letras sentenciais agora são permitidas nas fórmulas da LPO.
- A reiteração passou a ser uma regra básica, de modo que as provas podem estar em forma normal.
- O capítulo 28 agora define a satisfação de uma fórmula por um objeto, para que as condições de verdade dos quantificadores possam ser formuladas de maneira mais clara.
- Novos capítulos 16 e 33 sobre estratégias para construir provas.
- Acrescentados três capítulos sobre lógica modal (sistema de prova de dedução natural e semântica de Kripke). Eles se baseiam em _A Modal Logic Primer_, de Rob Trueman (University of York), que foi generoso ao compartilhá-lo. O sistema de prova foi alterado para usar as regras modais de Fitch. Ele aborda os fundamentos de K, T, S4 e S5.
- Acrescentado um capítulo sobre correção das provas da Lógica da Linguagem Formal, baseado na _Metatheory_, de Tim Button.
- Corrigidos vários erros e acrescentados diversos esclarecimentos.
