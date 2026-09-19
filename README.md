# forall x: Calgary — Introdução à lógica formal

[![REALMat — verificar livro](https://github.com/projetorealmat/forallx-yyc/actions/workflows/book-ci.yml/badge.svg)](https://github.com/projetorealmat/forallx-yyc/actions/workflows/book-ci.yml)

Este repositório contém a tradução e adaptação brasileira, em preparação, de *forall x: Calgary: Uma introdução à lógica formal*. A edição REALMat parte da [edição original em inglês](https://github.com/rzach/forallx-yyc) e preserva a atribuição, os créditos e a licença da obra-fonte.

**Tradutor e responsável pela edição REALMat:** Carlos André Duarte Costa.

A tradução está em desenvolvimento e revisão editorial. O trabalho é organizado em lotes; sugestões e correções são bem-vindas por meio das [issues](https://github.com/projetorealmat/forallx-yyc/issues) e dos *pull requests*.

## Sobre o livro

*forall x: Calgary* é um manual abrangente de lógica formal. Ele apresenta noções fundamentais como consequência e validade de argumentos; a sintaxe da lógica proposicional verofuncional (LVF) e sua semântica por tabelas-verdade; a sintaxe da lógica de predicados de primeira ordem (LPO) com identidade e as interpretações de primeira ordem; a simbolização de argumentos em linguagem natural em LVF e LPO; e sistemas de dedução natural no estilo Fitch para LVF e LPO.

O livro também aborda tópicos avançados, como lógica modal, correção (*soundness*) e completude funcional. Há exercícios com soluções, mantidos nos arquivos correspondentes da edição REALMat.

## Arquivos principais

- [Fonte principal em LaTeX](forallxyyc.tex)
- [Conteúdo do livro](forallx-yyc-content.tex)
- Variantes para [acessibilidade](forallxyyc-accessible.tex), [impressão](forallxyyc-print.tex) e [papel carta](forallxyyc-letter.tex)
- [Soluções dos exercícios](solutions/forallxyyc-solutions.tex)
- [Configuração do livro no REALMat](.realmat/book.json)
- [Metadados de citação](CITATION.cff)
- [Licença](LICENSE.md)
- [Histórico de alterações](CHANGELOG.md)
- [Lançamentos e versões anteriores](https://github.com/projetorealmat/forallx-yyc/releases)
- [Execuções dos fluxos de trabalho](https://github.com/projetorealmat/forallx-yyc/actions)

## Publicações

<!-- realmat-release:start -->
- Lançamento REALMat atualmente recomendado: [v0.1.0](https://github.com/projetorealmat/forallx-yyc/releases/tag/v0.1.0).
- [HTML de leitura da edição Calgary](https://forallx.openlogicproject.org/html/index.html)
- [PDF da versão atualmente recomendada](https://github.com/projetorealmat/forallx-yyc/releases/download/v0.1.0/forallxyyc.pdf)
<!-- realmat-release:end -->

O PDF oficial de cada versão é compilado e publicado automaticamente depois da incorporação da respectiva **Release PR**. O arquivo `forallxyyc.pdf` não é mantido como arquivo versionado na raiz do repositório. Enquanto não houver um lançamento REALMat, não há PDF ou HTML traduzido publicado para baixar.

## Versão em desenvolvimento, lançamentos e arquivos-fonte

A versão atualmente recomendada é `v0.1.0`, ainda em revisão editorial.

O versionamento segue estas regras:

- `v0.x.y`: tradução em revisão;
- `v1.0.0`: primeira tradução aprovada;
- `v1.0.1`: correção técnica ou editorial pequena;
- `v1.1.0`: adaptação ou acréscimo compatível com a mesma edição;
- `v2.0.0`: nova edição, com mudança estrutural ou editorial ampla.

Cada versão publicada preserva:

- o PDF correspondente à versão;
- os arquivos-fonte automáticos da tag;
- o pacote-fonte reproduzível;
- os metadados usados na compilação;
- o arquivo `SHA256SUMS`.

Para consultar uma versão anterior, abra [Lançamentos](https://github.com/projetorealmat/forallx-yyc/releases), escolha a versão desejada e baixe o PDF ou os arquivos-fonte. Os commits e as tags preservam também estados intermediários do projeto.

## Compilação local

Com uma instalação do TeX Live que inclua pdfLaTeX e **latexmk**, execute na raiz do repositório:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error forallxyyc.tex
~~~

O comando gera `forallxyyc.pdf` e os arquivos auxiliares da compilação. Para compilar outra variante, substitua `forallxyyc.tex` por `forallxyyc-accessible.tex`, `forallxyyc-print.tex` ou `forallxyyc-letter.tex`. O `latexmk` executa as passagens necessárias, inclusive a geração do glossário.

Para limpar os arquivos auxiliares, use:

~~~sh
latexmk -C forallxyyc.tex
~~~

## Conversão para HTML

Para converter o livro para HTML:

- instale o [LaTeXML](https://github.com/brucemiller/LaTeXML);
- instale o [BookML](https://vlmantova.github.io/bookml/) e suas dependências;
- execute `make -f Bookml.mk` na raiz do repositório.

Os arquivos HTML serão gerados em `auxdir/html/forallxyyc-html/`, e o pacote SCORM em `SCORM.forallxyyc-html.zip`.

## Edição original em inglês

Os links desta seção apontam deliberadamente para a edição original em inglês; eles não são arquivos da tradução REALMat para baixar:

- [Repositório original](https://github.com/rzach/forallx-yyc)
- [README da edição original](https://github.com/rzach/forallx-yyc/blob/master/README.md)
- [HTML da edição original](https://forallx.openlogicproject.org/html/)
- [PDF principal da edição original](https://forallx.openlogicproject.org/forallxyyc.pdf)
- [Sistema Carnap](https://carnap.io/) e [exercícios de exemplo](https://carnap.io/shared/rzach@ucalgary.ca/forall%20x:%20Calgary.md)

Para o histórico de edições e as informações sobre cópias impressas da edição original, consulte o [README em inglês](https://github.com/rzach/forallx-yyc/blob/master/README.md).

## Créditos e licença

*forall x: Calgary* baseia-se em [*forall x: Cambridge*](https://www.homepages.ucl.ac.uk/~uctytbu/OERs.html), de [Tim Button](https://www.homepages.ucl.ac.uk/~uctytbu/index.html), utilizada sob a licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Essa obra baseia-se, por sua vez, em [*forall x*](https://www.fecundity.com/logic/), de [P. D. Magnus](https://www.fecundity.com/job/), e foi remixada, revisada e ampliada por [Aaron Thomas-Bolduc](https://phil.ucalgary.ca/profiles/aaron-thomas-bolduc) e [Richard Zach](https://richardzach.org/).

A edição original também inclui material adicional de *forall x*, de P. D. Magnus, e de [*Metatheory*](https://www.homepages.ucl.ac.uk/~uctytbu/OERs.html), de Tim Button, ambos utilizados sob a licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); de [*forall x: Lorain County Remix*](https://github.com/rob-helpy-chalk/openintroduction), de [Cathal Woods](https://sites.google.com/site/cathalwoods/) e J. Robert Loftis, utilizado com permissão; e de [*A Modal Logic Primer*](http://www.rtrueman.com/uploads/7/0/3/2/70324387/modal_logic_primer.pdf), de [Robert Trueman](http://www.rtrueman.com/), utilizado com permissão.

[![Licença Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Esta tradução e adaptação brasileira é uma obra derivada distribuída sob a [Licença Creative Commons Atribuição 4.0 Internacional](https://creativecommons.org/licenses/by/4.0/). Ela não é uma publicação oficial da University of Calgary nem do Open Logic Project.

O código-fonte desta edição está disponível no [repositório REALMat](https://github.com/projetorealmat/forallx-yyc). A atribuição completa da obra-fonte deve ser preservada.

## Integração com o REALMat

Este repositório integra o projeto [REALMat](https://projetorealmat.github.io/). A tradução e a adaptação são desenvolvidas aqui; as versões publicadas podem ser consultadas nos [lançamentos deste repositório](https://github.com/projetorealmat/forallx-yyc/releases) e catalogadas no [portal REALMat](https://projetorealmat.github.io/).
